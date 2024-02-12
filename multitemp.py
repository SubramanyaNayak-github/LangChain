### Multiple Prompt Template



import os
import streamlit as st 

from constant import openai_key

os.environ['OPENAI_API_KEY']=openai_key



from langchain.llms import OpenAI
from langchain import PromptTemplate ## for writing template
from langchain.chains import LLMChain,SimpleSequentialChain  ## construct and manage chains of components for processing and generating responses

### the main problem of `SimpleSequentialChain` is it will only give us last output








## ST framework

st.title('Celebrity Search Result')

input_text = st.text_input('Search the celebrity u want')

## Prompt template

first_prompt = PromptTemplate(
    input_variables=['name'],
    template ='tell me about {name}'
)


llm=OpenAI(temperature=0.9)
chain = LLMChain(llm=llm,prompt=first_prompt,verbose=True,output_key='person')

second_prompt = PromptTemplate(
    input_variables=['person'],
    template ='when was {person} born'
)

chain2 = LLMChain(llm=llm,prompt=second_prompt,verbose=True,output_key='dob')


main_chain=SimpleSequentialChain(chains=[chain,chain2],verbose=True)

if input_text:
    st.write(main_chain.run(input_text))
