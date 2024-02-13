## LangChain Cookbook 
This cookbook is based off the LangChain Conceptual Documentation

**Goal:** 

1. Provide an introductory understanding of the components and use cases of LangChain via ELI5 examples and code snippets. For use cases check out part 
2. See video tutorial of this notebook.


### `What is LangChain?`

`LangChain is a framework for developing applications powered by language models.`

`LangChain makes the complicated parts of working & building with AI models easier.`

**It helps do this in two ways:**

1. Integration - Bring external data, such as your files, other applications, and api data, to your LLMs
2. Agency - Allow your LLMs to interact with it's environment via decision making. Use LLMs to help decide which action to take next



### `Why LangChain?`


1. Components - LangChain makes it easy to swap out abstractions and components necessary to work with language models.

2. Customized Chains - LangChain provides out of the box support for using and customizing 'chains' - a series of actions strung together.

3. Speed 🚢 - This team ships insanely fast. You'll be up to date with the latest LLM features.

4. Community 👥 - Wonderful discord and community support, meet ups, hackathons, etc.

Though LLMs can be straightforward (text-in, text-out) you'll quickly run into friction points that LangChain helps with once you develop more complicated applications.

**Note:** 
This cookbook will not cover all aspects of LangChain. It's contents have been curated to get you to building & impact as quick as possible. For more, please check out [LangChain Conceptual Documentation](https://python.langchain.com/docs/get_started/introduction).


You'll need an OpenAI api key to follow this tutorial. You can have it as an environement variable, in an .env file where this jupyter notebook lives, or insert it below where 'YourAPIKey' is. Have if you have questions on this, put these instructions into [ChatGPT](https://chat.openai.com/).