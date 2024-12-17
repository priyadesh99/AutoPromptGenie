import argparse
import os
import numpy as np
import cohere
from typing import List, Tuple, Dict
import pandas as pd


from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the Cohere client with the API key from env.
cohere_api_key = os.getenv("COHERE_API_KEY")

def evaluate_with_cohere_story_from_prompt(prompt: str, story: str, template_story: str, cohere_api_key: str) -> Dict[str, int]:
    """
    Evaluate a submission based on predefined metrics using Cohere's API.
    
    Parameters:
    - prompt (str): The prompt given for the story.
    - story (str): The story submission to evaluate.
    - cohere_api_key (str): Your Cohere API key.
    
    Returns:
    - dict: A dictionary containing evaluation scores for each metric.
    """
    co = cohere.Client(cohere_api_key)
    
    # Define the evaluation template
    template = """
    You are an evaluator. I will provide you with a prompt , a template story and a submission. 
    I will also provide a question for each of those metrics, and you will return 1 if the submission is better than the template story, 
    0 if template story is better than submission, as a score for that metric. Just answer with the name of the metric and the score, nothing else.
    
    Prompt: 
    {prompt}
    
    Template story:
    {template_story}
    
    Submission: 
    {story}
    
    Metrics:
    Helpfulness: Does the story contribute to the plot, character development, or themes?
    Directness: Does the story stay focused and move the plot forward?
    Grammaticality: Is the story grammatically correct and easy to read?
    Relevance: Does the story stay on-topic and relevant to its theme or prompt?
    Edge: Does the story include unique or surprising elements?
    Supposition: Does the story explore hypothetical situations or provoke analysis?
    Creativity: How original and imaginative is the story?
    Coherence: Is the language in the story coherent for the reader?
    """
    
    # Format the template with the actual prompt and stories
    formatted_prompt = template.format(prompt=prompt, story=story, template_story=template_story)
    
    # Generate the evaluation using Cohere
    response = co.generate(
        prompt=formatted_prompt,
        max_tokens=500,  # Enough tokens to evaluate all metrics
        temperature=0.01
    )
    
    # The response will contain the evaluation output
    evaluation = response.generations[0].text.strip()
    
    # Parse the response into a dictionary (assuming it's in a structured format)
    scores = {}
    for line in evaluation.split('\n'):
        metric, score = line.split(": ")
        scores[metric] = int(score)
    
    return scores

def rank_prompts_post_generation_LLM(input_prompt: str, candidate_prompts: List[str], human_story: str, api_key: str) -> Tuple[List[Dict], Dict]:
    """
    Rank prompts based on their evaluated scores using Cohere's API.
    
    Parameters:
    - input_prompt (str): The initial input prompt.
    - candidate_prompts (list): List of candidate prompts to evaluate.
    - human_story (str): The reference human-written story.
    - api_key (str): Your Cohere API key.
    
    Returns:
    - tuple: A list of ranked prompts with their scores and the best prompt.
    """
    prompt_ranking = []
    
    for prompt in candidate_prompts:
        story = evaluate_with_cohere_story_from_prompt(prompt, api_key)
        scores_generated = evaluate_with_cohere_story_from_prompt(prompt, story, human_story, api_key)
        avg_score_generated = np.mean(np.array(list(scores_generated.values())))
        
        # Add the prompt, individual scores, and average score to the ranking list
        prompt_ranking.append({
            "prompt": prompt,
            "evaluation_scores": scores_generated,
            "average_score": avg_score_generated
        })
    
    # Rank the prompts based on average score
    ranked_prompts = sorted(prompt_ranking, key=lambda x: x['average_score'], reverse=True)
    
    # Identify the best prompt
    best_prompt = ranked_prompts[0]

    return ranked_prompts, best_prompt

import argparse
import os
import pandas as pd
import numpy as np
from cohere import Client

def process_and_rank_prompts(input_csv: str, output_csv: str, cohere_api_key: str):
    """
    Process prompts from a CSV file, evaluate them, and save the ranked results to an output CSV.

    Parameters:
    - input_csv (str): Path to the input CSV file.
    - output_csv (str): Path to the output CSV file to save results.
    - cohere_api_key (str): API key for Cohere's service.
    """
    try:
        df = pd.read_csv(input_csv)
    except Exception as e:
        print(f"Error reading input CSV file: {e}")
        return

    required_columns = ['Prompt', 'Human Story', 'Response 1', 'Response 2', 'Response 3']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: Missing one or more required columns: {required_columns}")
        return

    output_data = []  # Collect data for all rows

    for index, row in df.iterrows():
        starting_prompt = row['Prompt']
        human_story = row['Human Story']
        generated_prompts = [row['Response 1'], row['Response 2'], row['Response 3']]

        try:
            ranked_prompts, best_prompt = rank_prompts_post_generation_LLM(
                starting_prompt, generated_prompts, human_story, cohere_api_key
            )

            for entry in ranked_prompts:
                output_data.append({
                    "Starting Prompt": starting_prompt,
                    "Generated Prompt": entry['prompt'],
                    "Average Score": entry['average_score']
                })

        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue

    # Save the collected data to the output CSV
    output_df = pd.DataFrame(output_data)
    try:
        output_df.to_csv(output_csv, index=False)
        print(f"Results saved to '{output_csv}'.")
    except Exception as e:
        print(f"Error saving output CSV file: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rank prompts by generating stories using Cohere's API based on relevance and diversity.")
    parser.add_argument("--input_csv", type=str, required=True, help="Path to the input CSV file containing prompts.")
    parser.add_argument("--output_csv", type=str, required=True, help="Path to the output CSV file to save results.")

    args = parser.parse_args()

    input_csv = args.input_csv
    output_csv = args.output_csv

    # Validate the existence of the input CSV file
    if not os.path.exists(input_csv):
        print(f"Error: Input file '{input_csv}' does not exist.")
        exit(1)

    try:
        print("Starting the prompt ranking process...")
        process_and_rank_prompts(input_csv, output_csv, cohere_api_key)
        print("Processing completed.")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
