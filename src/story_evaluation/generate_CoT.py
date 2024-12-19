import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
import pandas as pd
from typing import List
import time
from src.utils import generate_story_with_cohere, calculate_average_scores

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the Cohere client with the API key from env.
cohere_api_key = os.getenv("COHERE_API_KEY")

def evaluate_stories(
    input_csv: str,
    output_csv: str,
    cohere_api_key: str,
):
    """
    Evaluates stories from a CSV file by generating stories using a prompt, scoring them, and saving the results.

    Parameters:
        input_csv (str): Path to the input CSV containing prompts and human stories.
        output_csv (str): Path to save the output CSV.
        cohere_api_key (str): API key for the Cohere service.

    Returns:
        None
    """
    # Read the input CSVs
    df = pd.read_csv(input_csv)

    # Initialize output lists
    output_scores_human = []
    output_scores_gen = []
    generated_stories = []
    latencies = []

    # Iterate through each row in the CSV
    for index, row in df.iterrows():
        # Generate stories and calculate scores
        start_time = time.time()
        prompt = row['Prompt']
        human_story = row['Human Story']
        generated_story = generate_story_with_cohere(row['CotPrompt'], cohere_api_key)
        scores = calculate_average_scores(prompt, human_story, generated_story, cohere_api_key)
        latency = time.time() - start_time

        # Append results
        generated_stories.append(generated_story)
        output_scores_human.append(scores['average_scores_story_1'])
        output_scores_gen.append(scores['average_scores_story_2'])
        latencies.append(latency)

        # Optional delay to avoid API rate limits
        time.sleep(30)

    # Update the DataFrame with results
    df["Human Story Score"] = output_scores_human
    df["Generated Story Score"] = output_scores_gen
    df["Generated Story"] = generated_stories
    df["Evaluation Latency CoT"] = latencies

    # Save the output DataFrame to a CSV
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate and evaluate stories based on CoT Prompt.")
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
        print("Starting to evaluate generated stories...")
        evaluate_stories(input_csv, output_csv, cohere_api_key)
        print(f"Evaluation completed. Results saved to '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred during evaluation: {e}")

