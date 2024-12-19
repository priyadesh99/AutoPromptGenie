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

Generation of prompts were one of the 




### Troubleshooting:

If ModuleNotFoundError occurs due to not being able to find relative imports:

```
export PYTHONPATH=$PYTHONPATH:<PATH_TO_REPO>
source ~/.bashrc
```

