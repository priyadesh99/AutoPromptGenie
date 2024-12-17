import json
import os
import pandas as pd



if __name__ == "__main__":
    input_file = os.path.expanduser("~/AutoPromptGenie/data/train.json")      # Input JSON file
    output_file = os.path.expanduser("~/AutoPromptGenie/results/generated_promptsCoT.csv")  # Output file for results
    with open(input_file, "r") as train_file:
        train_data = json.load(train_file)
    prompts  = list(train_data.keys())
    stories = list(train_data.values())
    df = pd.DataFrame([prompts, stories], columns=['Prompt', 'Human Story'])
    df['CotPrompt'] = "Please think step by step and generate a story for the following prompt:" + df['Prompt']
    df.to_csv(output_file, index=False)
    print("Prompts saved..")
                                                   


    
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

