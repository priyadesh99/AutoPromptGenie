# Template with a placeholder
TEMPLATE_TOT = """ Imagine you are a prompt creator for a Large Language Model. Your task is to create a "tree of thought" prompt for generating a story. The goal is to break down the story creation process into multiple layers or steps, with each layer containing several branching ideas that explore different possibilities.

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
"""


# Template with a placeholder
GOT_TEMPLATE = """
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
"""