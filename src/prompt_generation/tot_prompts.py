import pandas as pd
import cohere
import json
import os
import time
import re


from dotenv import load_dotenv
from src.prompt_generation.prompt_template import TEMPLATE_TOT



template_tot = TEMPLATE_TOT

# Load environment variables from .env file
load_dotenv()

# Initialize the Cohere client with the API key from env.
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)


def generate_responses_with_metrics(prompts, stories, num_calls=3, max_tokens=1000, temperature=0.7):
    """
    Process prompts, generate responses, and add metrics along with human-provided stories.

    Args:
    - prompts: List of prompts (ToT-generated prompts).
    - stories: List of human-written stories corresponding to prompts.
    - num_calls: Number of API calls for each prompt.
    - model: Cohere model to use.
    - max_tokens: Maximum tokens for each response.
    - temperature: Sampling temperature for the API.

    Returns:
    - metrics_df: DataFrame containing prompts, human stories, responses, and metrics.
    - throughput: Throughput in API calls per second.
    - total_time: Total time for all API calls.
    """
    results = []  # Store results
    latencies = []  # Store latencies for each API call
    throughput_start = time.time()  # Start time to calculate throughput

    # Total epochs to iterate (defined by number of prompts)
    total_epochs = len(prompts)

    print("Starting prompt generation...")

    for epoch, (prompt, story) in enumerate(zip(prompts, stories), start=1):
        print(f"\n[Epoch {epoch}/{total_epochs}] Processing prompt {epoch}...")

        human_story = story  # Corresponding human-written story
        prompt_responses = []  # Responses for this prompt
        prompt_latencies = []  # Latencies for this prompt's calls

        for i in range(num_calls):
            try:
                start_time = time.time()  # Start timing the API call
                prompt = template_tot.format(input_text="'" + prompt+ "'")
                #print(prompt)

                # Generate text using Cohere API
                response = co.generate(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature
                )

                end_time = time.time()  # End timing the API call
                latency = end_time - start_time  # Calculate latency for this call
                prompt_latencies.append(latency)  # Store latency

                # Store the response
                response_text = response.generations[0].text.strip()
                #print(response_text)
                prompt_responses.append(response_text)
                print(f"   [Call {i+1}/{num_calls}] Response generated. Latency: {latency:.2f}s")

            except Exception as e:
                # Handle exceptions and append an error message
                prompt_responses.append(f"Error during API call {i+1}: {str(e)}")
                prompt_latencies.append(None)  # No latency for failed calls
                print(f"   [Call {i+1}/{num_calls}] Error occurred: {e}")

        # Add human story, prompt, responses, and latencies as a row in the results
        results.append([prompt, human_story] + prompt_responses)

        latencies.append(prompt_latencies)

        # Intermediate progress update after each epoch
        print(f"\n[Epoch {epoch}/{total_epochs}] Completed. Prompt processed with {len(prompt_responses)} responses.")

    # Calculate throughput
    throughput_end = time.time()
    total_time = throughput_end - throughput_start
    total_calls = len(prompts) * num_calls
    throughput = total_calls / total_time  # API calls per second

    # Create a DataFrame
    response_columns = [f'Response {i+1}' for i in range(num_calls)]
    latency_columns = [f'Latency {i+1} (s)' for i in range(num_calls)]
    df = pd.DataFrame(results, columns=['Prompt', 'Human Story'] + response_columns)
    latency_df = pd.DataFrame(latencies, columns=latency_columns)
    metrics_df = pd.concat([df, latency_df], axis=1)

    # Print metrics summary
    print("\n=== Metrics Summary ===")
    print(f"Total API Calls: {total_calls}")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Throughput: {throughput:.2f} API calls/second")
    print(f"Average Latency per API call: {pd.DataFrame(latencies).mean().mean():.2f} seconds")

    return metrics_df, throughput, total_time

# Main execution
if __name__ == "__main__":
    input_file = os.path.expanduser("~/AutoPromptGenie/data/train.json")      # Input JSON file
    output_file = os.path.expanduser("~/AutoPromptGenie/results/generated_promptsToT.csv")  # Output file for results
    with open(input_file, "r") as train_file:
        train_data = json.load(train_file)
    prompts  = list(train_data.keys())
    stories = list(train_data.values()) 

    
    # Uncomment if the data is in the format [WP]....
    # count = 0
    # prompt_list = []
    # story_list = []
    # for idx, item in enumerate(prompts[:500]):
    #     if len(item) <= 150 and len(item) >= 50:  # Adjust this condition to match your desired length
    #         try:
    #             parts = item.split("[")
    #             token = parts[1].split("]")[0].strip()  # Extracting the token inside the brackets
    #             if token == 'WP': continue
    #             sentence = parts[1].split("]", 1)[1].strip()
    #             sentence = re.sub(r'[^A-Za-z0-9\s]', '', sentence)
    #             if sentence != '':
    #                 prompt_list.append(sentence)
    #                 story_list.append(stories[idx])

    #             #if "prompt" in sentence.lower(): continue
    #         except IndexError:
    #             continue

    #         count +=1
    # Wp -> Writing prompts, TT -> Though provoking Themes, Realistic fiction

    metrics_df, throughput, total_time = generate_responses_with_metrics(prompts, stories)
    metrics_df = metrics_df.iloc[:, 1:]  # Drop the first column by selecting all others

    # Insert the prompts list as the first column
    metrics_df.insert(0, "Prompt", prompts)

    # Display the updated DataFrame
    print(metrics_df)

    metrics_df.to_csv(output_file, index=False)
    print("Prompts saved..")

