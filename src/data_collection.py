import os
import kagglehub
import json
from tqdm import tqdm

NUM_WORDS = 500  # Limit to 500 words for faster processing

def fetch_dataset():
    print("Fetching dataset..")
    path = kagglehub.dataset_download("ratthachat/writing-prompts")
    print(path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    data = ["train", "test", "valid"]
    for name in tqdm(data, desc="Processing dataset splits"):
        file_path = os.path.join(path, f"writingPrompts/{name}.wp_target")
        prompt_file_path = os.path.join(path, f"writingPrompts/{name}.wp_source")

        # Check if both the target and source files exist
        if os.path.exists(file_path) and os.path.exists(prompt_file_path):
            print(f"Processing {name} split...")
            with open(file_path, 'r') as f, open(prompt_file_path, 'r') as fp:
                stories = f.readlines()
                prompts = fp.readlines()

                # Check the length of prompts and stories
                print(f"Length of prompts: {len(prompts)}")
                print(f"Length of stories: {len(stories)}")

                if len(prompts) != len(stories):
                    print(f"Skipping {name} split due to mismatch in number of prompts and stories")
                    continue
                
                prompt_stories = {}
                for i in range(len(stories)):
                    prompt_stories[prompts[i].rstrip()] = " ".join(stories[i].split()[0:NUM_WORDS])

                output_file = os.path.join(output_dir, f"{name}_pairs.json")
                with open(output_file, 'w') as o:
                    json.dump(prompt_stories, o)

                print(f"Saved combined data for {name} split to {output_file}...")

                # Combine prompts with the first NUM_WORDS of the story
                new_stories = [
                    prompts[i].rstrip() + " <endprompts> " + " ".join(stories[i].split()[0:NUM_WORDS])
                    for i in range(len(stories))
                ]
                
                # Write the combined stories to a new file
                output_file = os.path.join(output_dir, f"{name}_combined.json")
                with open(output_file, 'w') as o:
                    for line in new_stories:
                        o.write(line.strip() + "\n")

                print(f"Saved combined data for {name} split to {output_file}...")

        else:
            print(f"Files for {name} split not found!")

if __name__ == "__main__":
    # Define the output directory to save the raw data
    output_dir = os.path.expanduser("~/AutoPromptGenie/data/raw")
    fetch_dataset()
    print(f"Dataset saved to {output_dir}")
