### Multiple Prompt Template



import os
import streamlit as st 

from constant import openai_key

os.environ['OPENAI_API_KEY']=openai_key



from langchain.llms import OpenAI
from langchain import PromptTemplate ## for writing template
from langchain.chains import (
    LLMChain,
    SimpleSequentialChain,
    SequentialChain) ## construct and manage chains of components for processing and generating responses

### the main problem of `SimpleSequentialChain` is it will only give us last output
## To get all the responses of the modele we use `SequentialChain`


from langchain.memory import ConversationBufferMemory  ## To store the conversation 




## ST framework

st.title('Celebrity Search Result')

input_text = st.text_input('Search the celebrity u want')


# Memory

person_memory = ConversationBufferMemory(input_key='name', memory_key='person_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='dob_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='events_history')


## Prompt template

first_prompt = PromptTemplate(
    input_variables=['name'],
    template ='tell me about {name}'
)


llm=OpenAI(temperature=0.9)
chain = LLMChain(llm=llm,prompt=first_prompt,verbose=True,output_key='person',memory=person_memory)

second_prompt = PromptTemplate(
    input_variables=['person'],
    template ='when was {person} born'
)

chain2 = LLMChain(llm=llm,prompt=second_prompt,verbose=True,output_key='dob',memory=dob_memory)

third_prompt = PromptTemplate(
    input_variables=['dob'],
    template ='Mention 5 major events that happened on {dob} in the world'
)

chain3 = LLMChain(llm=llm,prompt=third_prompt,verbose=True,output_key='events',memory=descr_memory)


main_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variable=['person','dob','events'],verbose=True)


if input_text:
    st.write(main_chain({'name':input_text}))


    with st.expander('Person'): 
        st.info(person_memory.buffer)

    with st.expander('Date of Birth'): 
        st.info(dob_memory.buffer)

    with st.expander('Major Events'): 
        st.info(descr_memory.buffer)
