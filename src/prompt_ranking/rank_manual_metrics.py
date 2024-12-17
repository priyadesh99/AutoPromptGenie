import numpy as np
from sentence_transformers import util
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import time
import csv
import argparse
import os

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast sentence embedding technique

def rank_prompts_using_eval_metrics(starting_prompt, generated_prompts, alpha=0.8, beta=0.2):
    """
    Rank generated prompts based on relevance and diversity scores.

    Parameters:
    - starting_prompt: The original prompt used to generate new prompts.
    - generated_prompts: List of generated prompts to evaluate.
    - alpha: Weight for relevance score (default=0.8).
    - beta: Weight for diversity score (default=0.2).

    Returns:
    - ranked_prompts: List of tuples (prompt, score) sorted by the final score.
    """
    # Ensure input validity
    if not starting_prompt or not generated_prompts:
        raise ValueError("Starting prompt or generated prompts are empty.")

    # Encode starting prompt and generated prompts
    starting_embedding = model.encode(starting_prompt, convert_to_tensor=True)
    generated_embeddings = model.encode(generated_prompts, convert_to_tensor=True)

    # Compute relevance scores (cosine similarity with the starting prompt)
    relevance_scores = util.cos_sim(starting_embedding, generated_embeddings)[0].cpu().numpy()

    # Compute pairwise cosine similarity for diversity
    pairwise_similarities = util.cos_sim(generated_embeddings, generated_embeddings).cpu().numpy()

    # Compute diversity score: Use entropy or average similarity for better assessment
    # Diversity score as 1 - average pairwise similarity
    diversity_scores = 1 - np.mean(pairwise_similarities, axis=1)
    

    # Combine the relevance and diversity scores with the given weights
    final_scores = alpha * relevance_scores + beta * diversity_scores

    # Rank prompts by the combined score
    ranked_indices = np.argsort(-final_scores)  # Sort in descending order
    ranked_prompts = [(generated_prompts[i], final_scores[i], relevance_scores[i], diversity_scores[i]) for i in ranked_indices]

    return ranked_prompts

def process_and_rank_prompts(input_csv, output_csv, model):
    """
    Read starting prompt and generated prompts (prompt1, prompt2, prompt3) from a CSV,
    calculate relevance, diversity scores, and latency, and store the results in an output CSV.
    """
    df = pd.read_csv(input_csv)

    output_data = []

    # Iterate through each row in the CSV
    for index, row in df.iterrows():
        starting_prompt = row['Prompt']
        human_story = row['Human Story']
        generated_prompts = [row['Response 1'], row['Response 2'], row['Response 3']]  # Get prompts from columns prompt1, prompt2, prompt3

        start_time = time.time()
        ranked_prompts = rank_prompts_using_eval_metrics(starting_prompt, generated_prompts)
        latency = time.time() - start_time

        row_data = [starting_prompt]
        row_data.append(human_story)
        
        best_prompt = None
        best_score = float('-inf')

        # Add each prompt's score and the latency
        for prompt, relevance, diversity, final_score in ranked_prompts:
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
    parser = argparse.ArgumentParser(description="Rank prompts using manual metrics like relevance.")
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
        process_and_rank_prompts(input_csv, output_csv, model)
        print(f"Processing completed. Results saved to '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
