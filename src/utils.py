import cohere
from dotenv import load_dotenv
import os
import numpy as np
# Load environment variables from .env file
load_dotenv()

# Initialize the Cohere client with the API key from env.
cohere_api_key = os.getenv("COHERE_API_KEY")


def generate_story_with_cohere(input_prompt, cohere_api_key, temperature=0.2):
    """
    Generate a story from the given input prompt using Cohere's language model.
    
    Parameters:
    - input_prompt (str): The prompt to start the story with.
    - cohere_api_key (str): Your Cohere API key.
    - max_tokens (int): The maximum number of tokens for the generated story (default is 200 tokens).
    - temperature (float): Controls the randomness of the predictions (default is 0.2).
    
    Returns:
    - str: The generated story based on the input prompt.
    """
    co = cohere.Client(cohere_api_key)
    final_prompt = "Choose branches from the following prompt structure to create an interesting story: " + input_prompt+ "The result should include the final story and not the structure. The final story should be around 500 words"
     
    # Generate the story
    response = co.generate(
        prompt=final_prompt,
        temperature=temperature,
    )
    
    # Extract the generated story from the response
    generated_story = response.generations[0].text.strip()
    
    return generated_story

def evaluate_with_cohere(prompt, story, cohere_api_key):
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
    You are an evaluator. I will provide you with a prompt and a submission. 
    I will also provide a question for each of those metrics, and you will return 1 if the answer is positive, 
    0 if negative, as a score for that metric. Just answer with the name of the metric and the score, nothing else.
    
    Prompt: 
    {prompt}
    
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
    formatted_prompt = template.format(prompt=prompt, story=story)
    
    # Generate the evaluation using Cohere
    response = co.generate(
        prompt=formatted_prompt,
        max_tokens=500,  # Enough tokens to evaluate all metrics
        temperature=0.01
    )
    
    evaluation = response.generations[0].text.strip()
    
    # Parse the response into a dictionary (assuming it's in a structured format)
    # Example expected output:
    # Helpfulness: 1
    # Directness: 0
    # Grammaticality: 1
    # Relevance: 1
    # Edge: 0
    # Supposition: 1
    # Creativity: 0
    # Coherence: 1
    scores = {}
    try:
        for line in evaluation.split('\n'):
            metric, score = line.split(": ")
            scores[metric] = int(score)
    except ValueError as e:
        print(f"Error parsing line: {line} | Exception: {e}")
        scores[line] = None  # Insert None for lines that don't match the expected format

    
    return scores


"""
Calculate the average scores of the different scores returned by LLM judge
"""
def calculate_average_scores(prompt, story_1, story_2, cohere_api_key):
    
    story_1_scores = evaluate_with_cohere(prompt, story_1, cohere_api_key)
    story_2_scores = evaluate_with_cohere(prompt, story_2, cohere_api_key)
    story_1_scores_array = np.array(list(story_1_scores.values()))
    story_2_scores_array = np.array(list(story_2_scores.values()))
    
    # Calculate average scores for each story
    avg_scores_story_1 = np.mean(story_1_scores_array)
    avg_scores_story_2 = np.mean(story_2_scores_array)
    
    return {
        "story_1_scores": story_1_scores,
        "story_2_scores": story_2_scores,
        "average_scores_story_1": avg_scores_story_1,
        "average_scores_story_2": avg_scores_story_2
    }
