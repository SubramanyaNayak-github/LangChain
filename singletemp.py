### Single Prompt Template



import os
import streamlit as st 

from constant import openai_key

os.environ['OPENAI_API_KEY']=openai_key



from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain


## ST framework

st.title('Celebrity Search Result')

input_text = st.text_input('Search the celebrity u want')

## Prompt template

first_prompt = PromptTemplate(
    input_variables=['name'],
    template ='tell me about {name}'
)


llm=OpenAI(temperature=0.9)
chain = LLMChain(llm=llm,prompt=first_prompt,verbose=True)




if input_text:
    st.write(chain.run(input_text))
