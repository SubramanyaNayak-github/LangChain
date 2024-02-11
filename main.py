## To integrate with openai api

import os
import streamlit as st 

from constant import openai_key

os.environ['OPENAI_API_KEY']=openai_key



from langchain.llms import OpenAI


## ST framework

st.title('LangChain & OpenAI Api Demo application')

input_text = st.text_input('Search the topic u want')


llm=OpenAI(tempurature=0.9)



if input_text:
    st.write(llm(input_text))