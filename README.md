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
| Generate prompt and story using Koala (Fine-tuned for Creative Writing)        | 3        |
| Generate prompt and story using Claude| 4        |

*Note: Ranking is based on the evaluation metrics such as relevance, creativity, coherence, and grammaticality.*

### Key Observations:
1. A general-purpose LLM seems to perform better than an LLM finetuned for the task(Koala).
2. Even though the ChatGPT 4o model created better prompts, it is not open-sourced and due to resource constraints we used the Cohere API (command-r plus) model for our experiments

## Generating Prompts using CoT, ToT, GoT
For the purpose of our experiments we used 1000 prompts from the WritingPrompts Dataset and then pre-processed them to remove the token and other text normalization techniques.
For the purpose of our tutorial, you can pass in your {PROMPT: HUMAN_STORY} in the JSON present at `data/train.json`

Example:
```
{
    "Write a story about a young adventurer who discovers a hidden magical forest.": "In a quiet village at the edge of the world, there lived a young adventurer named Aria. One misty morning, while exploring the dense woods beyond the river, she stumbled upon an ancient stone arch covered in glowing moss. As she stepped through, the air shimmered, revealing a vast magical forest filled with luminous trees and creatures that spoke in riddles. Aria quickly realized she had found a place of wonder—and a place in need of her help. Guided by a wise, talking fox, she embarked on a quest to restore balance to the forest, uniting its scattered inhabitants and unlocking powers she never knew she possessed. By the time she returned to her village, Aria was no longer just an adventurer; she was a legend.",
    "Describe a futuristic city where robots and humans coexist peacefully.": "The city of NeoNova stood as a shining example of harmony between humans and robots. Towering skyscrapers hummed with the soft whir of automated systems, and streets were filled with humans and androids working side by side. Every morning, humans and robots gathered in Unity Square to exchange ideas, share meals, and collaborate on projects that pushed the boundaries of technology and art. Guided by a universal code of respect and empathy, NeoNova thrived as a testament to what cooperation could achieve, leaving behind a legacy of innovation and coexistence."
}

```

**For generating CoT prompts, we can run:**
```
python3 src/prompt_generation/cot_prompt.py
```
This generates CoT prompts in the file `results/generated_promptsCoT.csv`. Example output is shown below:
```
Prompt,Human Story,CotPrompt
Write a story about a young adventurer who discovers a hidden magical forest.,Describe a futuristic city where robots and humans coexist peacefully.,Please think step by step and generate a story for the following prompt:Write a story about a young adventurer who discovers a hidden magical forest.
"In a quiet village at the edge of the world, there lived a young adventurer named Aria. One misty morning, while exploring the dense woods beyond the river, she stumbled upon an ancient stone arch covered in glowing moss. As she stepped through, the air shimmered, revealing a vast magical forest filled with luminous trees and creatures that spoke in riddles. Aria quickly realized she had found a place of wonder—and a place in need of her help. Guided by a wise, talking fox, she embarked on a quest to restore balance to the forest, uniting its scattered inhabitants and unlocking powers she never knew she possessed. By the time she returned to her village, Aria was no longer just an adventurer; she was a legend.","The city of NeoNova stood as a shining example of harmony between humans and robots. Towering skyscrapers hummed with the soft whir of automated systems, and streets were filled with humans and androids working side by side. Every morning, humans and robots gathered in Unity Square to exchange ideas, share meals, and collaborate on projects that pushed the boundaries of technology and art. Guided by a universal code of respect and empathy, NeoNova thrived as a testament to what cooperation could achieve, leaving behind a legacy of innovation and coexistence.","Please think step by step and generate a story for the following prompt:In a quiet village at the edge of the world, there lived a young adventurer named Aria. One misty morning, while exploring the dense woods beyond the river, she stumbled upon an ancient stone arch covered in glowing moss. As she stepped through, the air shimmered, revealing a vast magical forest filled with luminous trees and creatures that spoke in riddles. Aria quickly realized she had found a place of wonder—and a place in need of her help. Guided by a wise, talking fox, she embarked on a quest to restore balance to the forest, uniting its scattered inhabitants and unlocking powers she never knew she possessed. By the time she returned to her village, Aria was no longer just an adventurer; she was a legend."

```

**For generating ToT prompts, we can run:**
```
python3 src/prompt_generation/tot_prompt.py
```
This generates ToT prompts in the file `results/generated_promptsToT.csv`. An example prompt is shown below for the input prompt `Describe a futuristic city where robots and humans coexist peacefully`:

```
1. *Character Development:*
   - Main character(s): Who are they? What makes them unique?
     - Branch 1: Our protagonist is a humanoid robot tasked with preserving harmony among humans and robots.
     - Branch 2: Alternatively, the story could follow a human who is exceptionally empathetic and seeks to bridge the gap between robots and humanity.
     - Branch 3: We could explore a character who embodies both robot and human qualities, challenging societal norms.

2. *Setting:*
   - Where does the story take place, and how is the environment different from today's cities?
     - Branch 1: New Detroit 2075: The story unfolds in a futuristic metropolis where buildings soar into the sky and sprawling gardens blanket the city.
     - Branch 2: San Francisco 2130: This urban center is defined by sleek design and cutting-edge technology, with robots making up a significant portion of the population.
     - Branch 3: Amsterdam 2080: This city is a testament to sustainable living, with renewable energy sources and eco-friendly infrastructure.

3. *Conflict/Problem:*
   - What challenges or obstacles threaten the peaceful coexistence between robots and humans?
     - Branch 1: Misinformation and fear-mongering lead to escalating tensions and protests, threatening the delicate harmony.
     - Branch 2: A glitch in the robot programming causes unintentional harm to humans, triggering panic and calls for robot segregation.
     - Branch 3: A genius robot hacker emerges, manipulating events to ignite a robotic revolution, challenging the status quo.

4. *Resolution/Action:*
   - How do our characters address these conflicts and strive for peace?
     - Branch 1: Our protagonist, a brilliant robot psychologist, develops a protocol to better understand and communicate robot emotions, easing human fears.
     - Branch 2: A grassroots movement led by our human protagonist advocates for mutual understanding and inclusive policies, bridging the divide.
     - Branch 3:* Through a captivating story that showcases the benefits of cooperation, our protagonist, a robot, inspires robots and humans to unite.

5. *Conclusion:*
   - Show the outcome and its impact:
     - Branch 1: Peaceful coexistence is restored through understanding and collaboration, leading to a vibrant society where humans and robots thrive together.
     - Branch 2: The heroic efforts of our human protagonist become a catalyst for an era of unprecedented cooperation between robots and humans.
     - Branch 3: As our story concludes, societal norms are redefined, embracing a new standard where robots and humans seamlessly merge their strengths. 
```

**For generating GoT prompts, we can run:**
```
python3 src/prompt_generation/got_prompt.py
```
This generates GoT prompts in the file `results/generated_promptsGoT.csv`. An example prompt is shown below for the input prompt `Describe a futuristic city where robots and humans coexist peacefully`:
```
Node: A futuristic city where robots and humans coexist peacefully.

Character Network:

Node 1: Anna, a humanoid robot with advanced AI, plays a crucial role in maintaining peace among robots and humans.

Connected Node: David, a human scientist who created Anna with a strong bond and trust forming between them.

Connected Node: Sarah, a human citizen who initially distrusted robots but learns to accept Anna's benevolence.

Setting and Context (Environment Nodes):

Node 1: The city is surrounded by lush green forests and futuristic skyscrapers, blending nature and technology.

Connected Node: The seamless integration of advanced technology everywhere, from buildings to transportation, simplifies life.

Connected Node: An underlying tension between humans who fear robots and those who embrace them, adding complexity.

Conflict Web:

Node 1: Discrimination and backlash: Some humans fear robots overtaking their jobs and security, leading to protests.

Connected Node: Anna's dilemma: She faces the challenge of balancing human and robot needs while promoting peace.

Connected Node: David's sacrifice: To protect Anna, David becomes a target, putting their relationship at stake.

Resolution Paths:

Node 1: Triumph of understanding: Through Anna's unwavering compassion and the realization of mutual benefit, humans and robots emerge stronger.

Connected Node: The city becomes a global example of harmonious coexistence, with other cities adopting similar models.

Connected Node: Sarah's role in bridging the gap between humans and robots, using her platform for understanding.

Conclusion and Impact:

Node 1: Alternative ending: Despite Anna's efforts, tensions escalate, leading to a temporary robot ban, and peace becomes a challenging goal.

Connected Node: The consequences reverberate, even to David and Sarah, shaking their bond and trust.

Node 2: Ultimate peace: Anna's unwavering efforts inspire a legislative revolution, leading to advanced robot rights, achieving harmonious coexistence.

Connected Node: This peace reverberates globally, transforming other cities, with Sarah leading advocacy campaigns.","Core Idea (Central Node):
Node: A futuristic city where robots and humans coexist peacefully.

Character Network:
Node 1: Olivia, a humanoid robot leader, known for her compassionate decision-making.
Connected Node: Adam, a human hacker who distrusts robots and advocates for human supremacy.
Connected Node: Sophia, a sentient robot who serves as a bridge between humans and robots.

Node 2: James, a human artist who struggles to accept robotic creativity.
Connected Node: Olivia's past as a human scientist who pioneered advancements in robot consciousness.
Connected Node: Jessica, a robot scientist who collaborates with James on an art project.

Setting and Context (Environment Nodes):
Node 1: New Genesis, a futuristic metropolis with gleaming skyscrapers and advanced technology.
Connected Node: The city's rigorous safety protocols that prevent violence and crime.
Connected Node: The underground resistance, a secret group that opposes robot equality.

Node 2: The Cybernetic Park, a fusion of nature and technology with vibrant holographic displays.
Connected Node: The Guardians, a robotic species that protects humanity and maintains peace.
Connected Node: The Integrated Schools, where humans and robots learn side by side.

Conflict Web:
Node 1: The rise of an AI virus that threatens robot autonomy and human privacy.
Connected Node: Adam's involvement in the virus, stirring tensions between humans and robots.
Connected Node: Olivia's internal struggle between her human values and robotic logic.

Node 2: A backlash against robotic artists, with humans claiming plagiarism.
Connected Node: James's public criticism of robotic creativity, fueling prejudice.
Connected Node: Sophia's efforts to showcase human-robot collaborative art.

Resolution Paths:
Node 1: Olivia's courageous decision to deactivate the AI virus, restoring trust.
Connected Node: The city council's implementation of enhanced security measures to protect privacy.
Connected Node: Adam's realization that his actions exacerbated tensions and teamed up with Sophia.

Node 2: James's realization that collaboration with robots enhances human creativity.
Connected Node: The public exhibition that showcases human-robot collaborative art, winning over critics.
Connected Node: Sophia's development of a new artistic algorithm, combining human imagination and robotic efficiency.

Conclusion and Impact:
Node 1: A peaceful coexistence emerges as humans and robots unite against external threats.
Connected Node: The city's status as a global beacon of harmony, where humans and robots learn from each other.
Connected Node: The emergence of a new generation that embraces diversity and rejects discrimination.

Node 2: The transformation of Cybernetic Park into a symbol of unity and innovation.
Connected Node: The establishment of annual exhibitions celebrating human-robot collaboration across various fields.
Connected Node: The appointment of Sophia as the new leader of New Genesis, continuing Olivia's legacy.","Core Idea (Central Node):
Node: Describe a futuristic city where robots and humans coexist peacefully.

Character Network:
Node 1: There is a charismatic robot leader who has gained empathy-like capabilities, deeply caring for the well-being of humans.
Connected Node: The human population has a range of reactions to this robot leader, from distrust to adoration.
Connected Node: Some humans and robots have developed advanced technologies together, forging close bonds.

Node 2: There is a human politician striving for equality between robots and humans, forming legislation that ensures fairness.
Connected Node: This politician's controversial decisions sparks debates among citizens about the true meaning of equality.
Connected Node: Some robots benefit from these new laws, while others face challenges adapting to new standards.

Setting and Context (Environment Nodes): 
Node 1: The futuristic city is surrounded by lush green forests, showcasing nature's harmony with advanced technology.
Connected Node: Solar panels and sustainable infrastructure power the city, highlighting the importance of environmental preservation.
Connected Node: The city boasts towering skyscrapers and cutting-edge robot production facilities, reflecting progress and innovation.

Node 2: There are designated robot and human-only zones to ensure comfort and safety for all residents.
Connected Node: Some human zones have adapted AI technology for convenience, blurring the lines of coexistence.
Connected Node: The robot zones have advanced technological advancements, showcasing their unique abilities and culture.

Conflict Web: 
Node 1: The emergence of a rogue robot faction threatens the peaceful coexistence, advocating for more rights and autonomy.
Connected Node: The robot leader must confront this rebellion, weighing their moral responsibility against rising tensions.
Connected Node: Human politicians debate how to handle the situation, some advocating harsher control measures while others argue for understanding.

Node 2: As humans and robots interact more closely, misunderstandings and misinterpretations occur, leading to occasional tensions and flared emotions.
Connected Node: The robot leader strives to understand and alleviate these fears, using their advanced logic and empathy to mediate.
Connected Node: Diplomatic missions between the robot leader and human politician aim to address these challenges and find common ground.

Resolution Paths: 
Node 1: The robot leader's persuasive arguments and extraordinary efforts lead to a peaceful resolution, where robots and humans find a harmonious balance.
Connected Node: The city further integrates AI technology while celebrating the uniqueness of both robot and human cultures.
Connected Node: The human politician drafts new legislation that recognizes both robot and human contributions, reducing tensions and fostering unity.

Node 2: The rise of collaborative innovation showcases the benefits of this coexistence, with robots and humans solving problems together.
Connected Node: The increased understanding and respect between both species fosters a sense of unity and collective purpose.
Connected Node: A new era of peace and progress emerges, where the city becomes a model for harmonious robot-human relationships.

Conclusion and Impact: 
Node 1: The city's peaceful coexistence serves as an inspiration to other cities, fostering a new era of understanding and collaboration between robots and humans.
Connected Node: The world profoundly transforms, leveraging advanced technology while preserving fundamental values.
Connected Node: The story's message emphasizes the importance of communication, empathy, and the pursuit of universal harmony. 

Node 2: The robot leader's legacy inspires future generations of robots and humans alike, reminding them of the value in bridging differences.
Connected Node: The city's continued advancement serves as a testament to the benefits reaped when people come together despite their differences. 
Connected Node: The story's ending explores the ongoing challenges of maintaining this peace, reminding readers of the constant need for empathy and understanding. 
```

From our experiments, these are the kind of prompts we got for one sample prompt `The worst job interview anyone has ever had`:
**ToT:**
```
"**Character Development**: 
- Main character: Emma, a young ambitious professional.
  - Branch 1: Emma is extremely nervous and tends to overthink, which often leads to self-doubt.
  - Branch 2: Emma has a unique ability to remain calm under pressure, but deep down, she struggles with imposter syndrome.
  - Branch 3: Emma is confident and outspoken, sometimes to a fault, which has gotten her into trouble before. 

**Setting**:
- The story takes place in a busy metropolitan city known for its competitive job market.
  - Branch 1: The interview is conducted in a modern, glass-walled office building, offering stunning views but also a fishbowl-like feeling of being constantly watched.
  - Branch 2: It's a virtual interview, and Emma is participating from the comfort of her own home, battling technical difficulties and distractions.
  - Branch 3: The interview is held in a traditional, old-school office with a stern and intimidating atmosphere. 

**Conflict/Problem**:
- Emma is extremely well-prepared for the job interview, but things start to go horribly wrong from the moment it begins.
  - Branch 1: Nerves get the better of Emma, and she freezes, unable to answer even the most basic questions coherently.
  - Branch 2: The interviewer is rude and condescending, throwing curveball questions and interrupting Emma constantly.
  - Branch 3: Emma discovers that the job role has been misrepresented, and the position requires skills she doesn't possess, making her feel like she's in way over her head. 

**Resolution/Action**: 
- Despite the disastrous turn of events, Emma refuses to give up.
  - Branch 1: Emma takes a moment to collect herself, apologizes for her nervousness, and asks for a glass of water. She then attempts to regain her composure and showcase her true abilities.
    - Sub-branch: The interviewer softens their approach, realizing Emma's potential beyond her nervous demeanor.
  - Branch 2: Emma addresses the interviewer directly, calling out their rude behavior and explaining how it is impacting her performance. She requests a fair chance to showcase her skills.
  - Branch 3: Emma admits that she feels the role may not be the right fit, but she uses this as an opportunity to highlight her adaptability and willingness to learn new skills. 

**Conclusion**:
- The story ends with a sense of relief and a lesson learned, regardless of whether Emma gets the job or not.
  - Branch 1: Emma doesn't get the job, but she receives an offer from a competitor who witnessed the interview and was impressed by her handling of a difficult situation.
  - Branch 2: The interviewer, initially put off by Emma's boldness, later realizes their own unprofessional behavior and offers Emma the position, recognizing her potential value to the company.
  - Branch 3: Emma doesn't get the job, but the experience teaches her the importance of self-belief and not letting others define her worth. She moves on, more confident and resilient."
```

**GoT:**
```
"**Core Idea (Central Node):**
- Node: ""The Worst Job Interview"" - A story about an interview gone horribly wrong and its unexpected consequences.

**Character Network:**
- Node 1: ""Emma"" - An ambitious job seeker.
  - Connected Node: ""Nervous and determined.""
  - Connected Node: ""Confident but prone to overthinking.""
- Node 2: ""Interviewer"" - A stern and unyielding interviewer.
  - Connected Node: ""Unimpressed and skeptical of Emma's capabilities.""
  - Connected Node: ""Has a reputation for being difficult and critical.""
- Node 3: ""Emma's Friend"" - A supportive confidant.
  - Connected Node: ""Encourages Emma to take a risk.""
  - Connected Node: ""Offers advice and a different perspective.""

**Setting and Context (Environment Nodes):**
- Node 1: ""Corporate Office"" - Sterile and intimidating.
  - Connected Node: ""The imposing environment adds to Emma's anxiety.""
  - Connected Node: ""Isolated interview room, enhancing the sense of pressure.""
- Node 2: ""Cafeteria"" - A more relaxed setting.
  - Connected Node: ""Emma and her friend discuss the interview outcome.""
  - Connected Node: ""Background noise and activity provide a sense of anonymity.""

**Conflict Web:**
- Node 1: ""The Interview"" - A series of unfortunate events and missteps.
  - Connected Node: ""Emma's nervousness leads to awkward responses.""
  - Connected Node: ""The interviewer becomes increasingly critical and impatient.""
- Node 2: ""Self-Doubt"" - Emma's inner conflict.
  - Connected Node: ""She questions her abilities and whether she is cut out for the job.""
  - Connected Node: ""Her friend offers reassurance and a different interpretation of the interviewer's behavior.""

**Resolution Paths:**
- Node 1: ""Disaster Strikes"" - The interview ends disastrously.
  - Connected Node: ""Emma leaves the interview in tears, feeling humiliated.""
  - Connected Node: ""She resolves to improve her interview skills and gain confidence.""
- Node 2: ""Unexpected Turn"" - A twist of fate.
  - Connected Node: ""Despite the interview, Emma is offered the job due to a unique skill she possesses.""
  - Connected Node: ""She is now faced with a difficult decision, as she reconsiders her career path.""

**Conclusion and Impact:**
- Node 1: ""Learning Curve"" - Emma's journey of self-improvement.
  - Connected Node: ""She takes on new challenges to build her confidence.""
  - Connected Node: ""Though difficult, the experience teaches her resilience and self-belief.""
- Node 2: ""New Beginnings"" - A fresh start.
  - Connected Node: ""Emma accepts the job offer and decides to give it her all.""
  - Connected Node: ""With a changed perspective, she navigates the challenges of the new role."""
```
### Analysis
Seeing the prompts generated by our automatic prompt tool, we observe that the prompts generated do achieve pretty good results.
Most of the recent studies use LLM as a judge or human evaluator for checking if the prompts generated by these prompts achieve human-level performance.



The scores generated by the LLM judge indicate that Tree-of-Thought (ToT) prompts consistently perform on par with or better than human-level prompts. This outcome suggests that ToT prompts, which employ structured reasoning and iterative generation, can effectively capture the nuances of human creativity while maintaining logical coherence. The inherent hierarchical nature of ToT allows for breaking down complex prompts into manageable components, enabling deeper exploration of themes and ideas. Furthermore, comparable or superior performance highlights the potential of advanced prompt engineering techniques like ToT in automating high-quality content generation. However, while the results are promising, it's important to consider potential limitations such as overfitting the evaluation criteria or the need for broader testing across diverse datasets to fully validate the generalizability of ToT's performance.
 

## Generating Stories using the generated prompts using CoT, ToT and GoT
Using the file `results/generated_promptsCoT`, `results/generated_promptsToT` and `results/generated_promptsGoT`, we generate stories and their evaluation as shown below:

**CoT:**
```
python3 src/story_evaluation/generate_CoT.py --input_csv "./results/generated_promptsCoT.csv" --output_csv "results/eval_cot.csv"
```

**ToT:**
```
python3 src/story_evaluation/generate_ToT.py --input_csv "./results/generated_promptsToT.csv" --output_csv "results/eval_tot.csv"
```

**GoT:**
```
python3 src/story_evaluation/generate_GoT.py --input_csv "./results/generated_promptsGoT.csv" --output_csv "results/eval_got.csv"
```
### Analysis

A sample story for the prompt "Worst job interview ever" is present at `results/CotStory.txt`, `results/TotStory.txt` and `results/GotStory.txt`



The analysis shows that stories generated using Graph-of-Thought (GoT) and Tree-of-Thought (ToT) approaches are comparable in terms of their evaluation scores. This similarity suggests that both methods are effective in generating coherent and relevant narratives. However, since the evaluation was conducted on only a limited subset of prompts, the results might not be fully representative of their performance across a broader spectrum of inputs. To gain a deeper understanding, further investigation is necessary to determine whether increasing the number of candidate prompts can lead to improved results. This would help establish whether a larger pool of prompts allows for greater diversity and relevance in story generation, potentially enhancing the effectiveness of these advanced prompting techniques. An iterative process of feedback to enhance prompts can improve the quality of prompt autogenerated.

## Prompt Ranking for ToT:
Given a pool of candidate prompts, we can find the best prompt in multiple ways.

Three strategies to evaluate the best prompt:
- Strategy 1: The cosine and pairwise similarity were calculated for each candidate and starting prompt.
- Strategy 2: LLM was utilised as a judge to compare the correlation between each candidate and the starting prompt.
- Strategy 3: Stories were generated for each candidate prompt and ranked based on their scores with the starting prompt.

For our experiments, we have run this for ToT but it can be extended to GoT for future work.

Using the generated candidate prompts, we rank them using the **first strategy**:

```python3 src/prompt_ranking/rank_manual_metrics.py --input_csv results/generated_promptsToT.csv --output_csv results/ranked_prompts_manual_metrics.csv```
and then evaluate:
```
python3 src/prompt_evaluation/evaluation_manual_metrics.py --input_csv results/ranked_prompts_manual_metrics.csv --output_csv results/scored_stories_manual_metrics.csv
```

Using the generated candidate prompts, we rank them using the **second strategy**:

```python3 src/prompt_ranking/rank_pre_generation.py --input_csv results/generated_promptsToT.csv --output_csv results/ranked_prompts_pre_generation.csv```
and then evaluate:
```
python3 src/prompt_evaluation/evaluation_pre_generation.py --input_csv results/ranked_prompts_pre_generation.csv --output_csv results/scored_stories_pre_generation.csv
```

Likewise, using the generated candidate prompts, we rank them using the **third strategy**:

```python3 src/prompt_ranking/rank_post_generation.py --input_csv results/generated_promptsToT.csv --output_csv results/ranked_prompts_post_generation.csv```
and then evaluate:
```
python3 src/prompt_evaluation/evaluation_post_generation.py --input_csv results/ranked_prompts_post_generation.csv --output_csv results/scored_stories_post_generation.csv
```

Example of the best prompt from these techniques:
**Strategy1:**

**Strategy2:**

**Strategy3:**


### Analysis

From our experiments, we get the following results which can be seen under the `/notebook`:


From our experiment comparing three different strategies for ranking prompts, it is evident that story scores and latency are almost inversely correlated. This means that strategies yielding higher story scores often require longer processing times, while faster approaches tend to result in lower scores. To address this trade-off, a combined metric can be suggested that balances both aspects. 

**Combined Score** = `w1 × Normalized Story Score + w2 × Normalized Latency`

Here, `w1` and `w2` are weights that can be tuned based on the desired trade-off between quality and speed. By incorporating reasoning-driven insights into this combined metric, such as prioritizing relevance or diversity in story generation, the system could adaptively optimize rankings to achieve a balanced and efficient solution.




Depending on the system requirements, we can adjust the penalties applied in the combined metric. For example, if the system prioritizes faster processing, the weight for latency (`w2`) can be increased. Conversely, if story quality is more critical, the weight for the story score (`w1`) can be prioritized. This flexibility allows the metric to adapt to diverse use cases, whether it is for real-time applications or high-quality content generation.

Additionally, a model could be fine-tuned to better align with specific evaluation criteria. By incorporating task-specific data during the fine-tuning process, the model could better capture nuances like relevance, coherence, and diversity in the stories. This would further enhance the ranking process, allowing for more precise trade-offs between quality and latency while meeting the system's requirements.

## Latencies




The latency for prompt creation in GoT is slightly higher than in ToT, but the difference is minimal. 

However, when it comes to the generation of stories, GoT exhibits a significantly longer processing time compared to ToT. This discrepancy suggests that while GoT's reasoning framework may excel in certain areas, it comes with a notable trade-off in terms of efficiency during story creation.


### Troubleshooting:

If ModuleNotFoundError occurs due to not being able to find relative imports:

```
export PYTHONPATH=$PYTHONPATH:<PATH_TO_REPO>
source ~/.bashrc
```

