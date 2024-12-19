# AutoPromptGenie

Contributors: Triyasha Ghosh Dastidar and Priya Deshpande


Prompting has emerged as a cornerstone of modern natural language processing (NLP), especially with the rise of large language models (LLMs). By crafting specific, well-designed prompts, users can guide LLMs to generate more accurate, creative, and contextually relevant responses. This "prompt engineering" process enables diverse applications, from content creation and data summarization to answering complex queries and solving industry-specific problems. As LLMs become more capable, effective prompting is key to unlocking their potential, making it an essential skill for leveraging AI systems efficiently.

However, this process is bottlenecked because not all users know the prompting techniques. Additionally, the way LLMs react to prompts is non-trivial.
Hence, we were inspired to create this Automatic Prompt Generation tool using advanced reasoning techniques like Tree-of-Thought(ToT) or Graph-of-Thought(GoT).

---

## Reasoning Techniques

The initial LLMs are Human-Level Prompt Engineers was the main motivation behind our application and serves as the extension to that idea. 
The automatic prompt synthesis was done using the chain of thought reasoning technique and served pretty good results. There have been improvements in reasoning techniques which when incorporated into this process can yield better results for the tasks which did not include only linear thought.

## Use Case

We use the Automatic Prompt Engineer for the "Creative Writing Task". Stories are generally non-linear whose essence is not captured by the linear thoughts captured by CoT. Creative writing requires more non-linear complex thought pipelines for which GoT and ToT are better suited.
Hence we decided to choose "Creative Writing" as our target benchmark.

The other possible options were: Maths Problem Solving, Maths Quiz Problems, Puzzles etc.

## Prompts

Generation of prompts was one of the challenging tasks and we went through a series of iterations to finalize on the final prompts.

### Prompt for generating Chain of Thought Prompt
According to prior literature, we appended "Let's think step by step" to generate CoT prompts since it was proven this way they could work as Zero Shot Learners.

### Prompt for generating Tree of Thought Prompt
The prompt promotes creating different levels and branches to have non-linear thoughts which are effective for creative writing.

```Imagine you are a prompt creator for a Large Language Model. Your task is to create a "tree of thought" prompt for generating a story. The goal is to break down the story creation process into multiple layers or steps, with each layer containing several branching ideas that explore different possibilities.

Here are the steps to create the tree of thought prompt:

1. **Character Development**:
   - Start by defining the main character(s). Who are they, and what makes them unique?
     - Branch 1: [Insert characteristic or trait of character].
     - Branch 2: [Insert another potential trait or backstory of character].
     - Branch 3: [Another direction for character development].

2. **Setting**:
   - Now, create the setting of the story. Where does the story take place, and what is the environment like?
     - Branch 1: [Describe one potential setting].
     - Branch 2: [Describe an alternative setting].
     - Branch 3: [Another possible setting].

3. **Conflict/Problem**:
   - Introduce the main conflict or problem that the character(s) will face. What challenges or obstacles will they encounter?
     - Branch 1: [First potential conflict or problem].
     - Branch 2: [Second possible conflict or problem].
     - Branch 3: [Another possible conflict or problem].

4. **Resolution/Action**:
   - How does the character resolve the conflict or take action? What decisions or actions do they take?
     - Branch 1: [First possible resolution or action].
     - Branch 2: [Second potential resolution or action].
     - Branch 3: [Another way to resolve the conflict].

5. **Conclusion**:
   - Finally, conclude the story by showing the outcome. How does the story end, and what impact does it have on the character or the world?
     - Branch 1: [First possible ending or outcome].
     - Branch 2: [Second possible ending].
     - Branch 3: [Another potential outcome].
Now, use this structure to generate the final tree of thought prompt for {input_text}. DO NOT ADD ANY EXTRA INFORMATION
```
### Prompt for generating Graph of Thought Prompt

```
Imagine you are a prompt creator for a Large Language Model.
Your task is to create a "graph of thought" prompt for generating a story.
The goal is to interconnect multiple ideas, where each idea (node) can have connections to multiple related ideas,
forming a web-like structure. These connections should highlight dependencies and possibilities that may influence
the story's flow.

Here are the steps to create the graph of thought prompt:

1. **Core Idea (Central Node)**:
   - Start by identifying the central theme or concept of the story.
     - Node: [Insert central theme or concept of the story].

2. **Character Network**:
   - Develop the main character(s) and explore their relationships with others.
     - Node 1: [Describe main character and a key trait or role].
       - Connected Node: [Another character closely tied to Node 1].
       - Connected Node: [A conflict or shared history between Node 1 and this character].
     - Node 2: [Describe another important character].
       - Connected Node: [A secondary connection to Node 1 or another plot thread].

3. **Setting and Context (Environment Nodes)**:
   - Create the setting and its impact on the story.
     - Node 1: [Primary setting description].
       - Connected Node: [How this setting affects the main character or conflict].
       - Connected Node: [Alternative setting or background detail tied to Node 1].
     - Node 2: [Describe a secondary setting or environmental detail].
       - Connected Node: [Link between this setting and another part of the story].

4. **Conflict Web**:
   - Introduce the central conflict and branch out to explore related sub-conflicts or dilemmas.
     - Node 1: [Main conflict or problem].
       - Connected Node: [A complication or escalation related to this conflict].
       - Connected Node: [A character's reaction or role in this conflict].
     - Node 2: [Sub-conflict or secondary challenge].
       - Connected Node: [How this connects back to the main conflict or another character].

5. **Resolution Paths**:
   - Map out different possible resolutions or outcomes and their interconnected effects.
     - Node 1: [First potential resolution or action].
       - Connected Node: [Effect or consequence of this resolution on the characters or world].
       - Connected Node: [Alternate perspective or reaction to this resolution].
     - Node 2: [Second potential resolution or action].
       - Connected Node: [Another outcome or branching story effect].

6. **Conclusion and Impact**:
   - Conclude by showing multiple potential endings and their ripple effects.
     - Node 1: [First possible ending].
       - Connected Node: [How this ending ties back to earlier elements in the graph].
     - Node 2: [Second possible ending].
       - Connected Node: [Another perspective or impact of this ending on the story].

Now, use this structure to generate the final graph of thought prompt for {input_text}.
DO NOT ADD ANY EXTRA INFORMATION.
```
## Dataset and Preprocessing

### Dataset
We used the **"Writing Prompts"** dataset, which contains a large collection of human-written stories paired with writing prompts. This dataset enables hierarchical story generation.  
- [Dataset Link](https://www.kaggle.com/datasets/ratthachat/writing-prompts/data)

#### Data Preprocessing
1. **Text Normalization**:  
   - Removed extra characters and spaces to clean the text.
2. **Prompt Length Filtering**:  
   - Excluded excessively long input prompts, as humans generally write shorter prompts.
3. **Thematic Balance**:  
   - Selected an equal mix of themes, including:
     - Writing prompts  
     - Realistic fiction  
     - Thought-provoking prompts


## LLM Selection
For the purpose of this project, we wanted to run a trial with one human annotator for the outputs of different models and run all the stages through the one ranked highest.

| **Model**                     | **Rank** |
|--------------------------------|----------|
| Generate prompt and story using ChatGPT 4o model   | 1       |
| Generate prompt and story using Cohere API | 2       |
| Generate prompt and story using Koala (Finetuned for Creative Writing)        | 3        |
| Generate prompt and story using Claude| 4        |

*Note: Ranking is based on the evaluation metrics such as relevance, creativity, coherence, and grammaticality.*

### Key Observations:
1. A general purpose LLM seems to perform better than LLM finetuned for the task(Koala).
2. Even though ChatGPT 4o model created better prompts, it is not open-sourced and due to resource constraints we used Cohere API (command-r plus) model for our experiments

## Generating Prompts using CoT, ToT, GoT
For the purpose of our experiments we used 1000 prompts from the WritingPrompts Dataset and then pre-processed them to remove the token and other text normalization techniques.
For the purpose of our tutorial, you can pass in your {<PROMPT>: <STORY>} in the json present at `data/train.json`

### Troubleshooting:

If ModuleNotFoundError occurs due to not being able to find relative imports:

```
export PYTHONPATH=$PYTHONPATH:<PATH_TO_REPO>
source ~/.bashrc
```

