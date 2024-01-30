# Quick Overview

- ![img](https://microsoft.github.io/generative-ai-for-beginners/01-introduction-to-genai/images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)


## How do large language model work?

- Tokenizer, text to numbers: Large Language Models receive a text as input and generate a text as output. However, being statistical models, they work much better with numbers than text sequences. That’s why every input to the model is processed by a tokenizer, before being used by the core model. A token is a chunk of text – consisting of a variable number of characters, so the tokenizer's main task is splitting the input into an array of tokens. Then, each token is mapped with a token index, which is the integer encoding of the original text chunk.
- Predicting output tokens
- Selection process, probability distribution

![img](https://microsoft.github.io/generative-ai-for-beginners/01-introduction-to-genai/images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)