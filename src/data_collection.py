import os
import kagglehub
import json

# For running this file you need add your KaggleHub API key to the system

def fetch_dataset():
    print("Fetching dataset..")
    path = kagglehub.dataset_download("ratthachat/writing-prompts")
    print(path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    data = ["train", "test", "valid"]
    for name in data:
        file_path = os.path.join(path, f"writingPrompts/{name}.wp_target")
        if os.path.exists(file_path):
                print(f"Processing {name} split...")
                with open(file_path, 'r') as f:
                    # Write the cleaned-up stories in chunks to avoid memory issues
                    output_file = os.path.join(output_dir, f"{name}.json")
                    with open(output_file, 'w') as o:
                        stories = []
                        for line in f:
                            # Clean up the story by trimming it to 2500 words
                            story = " ".join(line.split()[0:2500])
                            stories.append(story)

                            # If the list reaches 1000 stories, dump them to the file and reset the list
                            if len(stories) >= 1000:
                                json.dump(stories, o)
                                o.write("\n")  # Separate each batch of stories by a newline
                                stories = []  # Reset the list for the next batch

                        # Dump any remaining stories after finishing the file
                        if stories:
                            json.dump(stories, o)
                            o.write("\n")

                print(f"Saving {name} split to {output_file}...")
        else:
                print(f"File {file_path} not found!")



if __name__ == "__main__":
    # Define the output directory to save the raw data
    output_dir = os.path.expanduser("~/AutoPromptGenie/data/raw")
    fetch_dataset()
    print(f"Dataset saved to {output_dir}")