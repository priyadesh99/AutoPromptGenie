import cohere
import pandas as pd
import time
import numpy as np
import csv
import argparse


from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Initialize the Cohere client with the API key from env.
cohere_api_key = os.getenv("COHERE_API_KEY")

cohere_client = cohere.Client(cohere_api_key)

def rank_prompts_with_cohere(starting_prompt, generated_prompts):
    """
    Rank prompts using Cohere's LLM as a judge for relevance and diversity.

    Parameters:
    - starting_prompt: The original prompt used to generate new prompts.
    - generated_prompts: List of generated prompts to evaluate.

    Returns:
    - ranked_prompts: List of tuples (prompt, final_score, relevance_score, diversity_score) sorted by final score.
    """
    if not isinstance(generated_prompts, list) or not generated_prompts:
        raise ValueError("Generated prompts should be a non-empty list.")

    evaluation_template = """
    You are an expert evaluator tasked with scoring prompts based on their relevance and diversity compared to the starting prompt. 
    I will provide you with a starting prompt and candidate prompt. I will also provide you with a metric name and a question for each of those on a scale of 0-5.
    Just answer with the name of the metric and the score, nothing else.
    
    Starting Prompt: {starting_prompt}
    Candidate Prompt : {candidate_prompt}
    
    Metrics:
    Relevance: How closely the prompt relates to the starting prompt (scale: 0 to 5).
    Diversity: How unique and distinct the prompt is compared to other prompts (scale: 0 to 5).
    """

    scored_prompts = []

    for i, candidate_prompt in enumerate(generated_prompts):
        formatted_prompt = evaluation_template.format(starting_prompt=starting_prompt, candidate_prompt=candidate_prompt)

        response = cohere_client.generate(
            prompt=formatted_prompt,
            max_tokens=200,
            temperature=0.01  # Deterministic output
        )
        
        response_text = response.generations[0].text.strip()
        
        # Print the raw response for debugging
        print(f"Response for prompt {i+1}: {response_text}")
        
        try:
            # Safely parse the response manually (e.g., if it's in a structured text format)
            lines = response_text.split("\n")
            relevance_score = None
            diversity_score = None

            for line in lines:
                if "Relevance" in line:
                    relevance_score = int(line.split(":")[1].strip())
                elif "Diversity" in line:
                    diversity_score = int(line.split(":")[1].strip())

            if relevance_score is None or diversity_score is None:
                raise ValueError(f"Failed to extract scores from response: {response_text}")

        except Exception as e:
            raise ValueError(f"Error parsing Cohere's response for prompt {i+1}: {e}")

        final_score = 0.8 * relevance_score + 0.2 * diversity_score  # Weighted score
        scored_prompts.append((candidate_prompt, final_score, relevance_score, diversity_score))

    # Sort prompts by final score (descending)
    ranked_prompts = sorted(scored_prompts, key=lambda x: -x[1])

    return ranked_prompts

def process_and_rank_prompts(input_csv, output_csv):
    """
    Read starting prompt and generated prompts (Response 1, Response 2, Response 3) from a CSV,
    calculate relevance, diversity scores, and latency using Cohere, and store the results in an output CSV.
    """
    df = pd.read_csv(input_csv)

    output_data = []

    # Iterate through each row in the CSV
    for index, row in df.iterrows():
        print(f"Processing Prompt {index}")
        starting_prompt = row['Prompt']
        human_story = row['Human Story']
        generated_prompts = [row['Response 1'], row['Response 2'], row['Response 3']]
        start_time = time.time()
        try:
            ranked_prompts = rank_prompts_with_cohere(starting_prompt, generated_prompts)
        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue
        latency = time.time() - start_time

        row_data = [starting_prompt]
        row_data.append(human_story)
        
        best_prompt = None
        best_score = float('-inf')

        # Add each prompt's score and the latency
        for prompt, final_score, relevance, diversity in ranked_prompts:
            row_data.append(prompt)
            row_data.append(relevance)
            row_data.append(diversity)
            row_data.append(final_score)

            if final_score > best_score:
                best_score = final_score
                best_prompt = prompt

        row_data.append(best_prompt)
        row_data.append(best_score)
        row_data.append(latency)

        output_data.append(row_data)

    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ['Starting Prompt', 'Human Story', 'Prompt 1', 'Relevance Score 1', 'Diversity Score 1', 'Final Score 1', 
                  'Prompt 2', 'Relevance Score 2', 'Diversity Score 2', 'Final Score 2', 
                  'Prompt 3', 'Relevance Score 3', 'Diversity Score 3', 'Final Score 3', 
                  'Best Prompt', 'Best Prompt Score', 'Latency']
        writer.writerow(header)
        writer.writerows(output_data)

    print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Rank prompts using Cohere's API based on relevance and diversity.")
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
        process_and_rank_prompts(input_csv, output_csv)
        print(f"Processing completed. Results saved to '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred during processing: {e}")