import pandas as pd
import streamlit as st
import sqlite3
import openai
import os
from streamlit_chat import message
from sqlite3 import connect
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor


os.environ['OPENAI_API_KEY'] = "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"

#connected sqlite database
db = SQLDatabase.from_uri("sqlite:///./swbe_data.db")
toolkit = SQLDatabaseToolkit(db=db)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

#page header
st.title("CP-Natural language to query your SQL Database OpenAI GPT-3 BOT 🤖powered by LLMs")
st.write('Welcome to the AI assistant!,How may i help you?')
st.divider()  # 👈 Draws a horizontal rule

def get_text():
    input_text = st.text_input("You: ",key="input")
    return input_text

# # Create Streamlit app
# def main():
#     user_input = st.text_input("Your Input:")
#     if 'past' not in st.session_state:
#         st.session_state.past = []
#     if 'generated' not in st.session_state:
#         st.session_state.generated = []

#     if user_input:
#         if st.button("Generate"):
#             output = agent_executor(user_input)
#             st.session_state.generated.append(output)
#             st.write(output)


def main():
    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    user_input = get_text()

    if user_input:
        output = agent_executor(user_input)
        # store the output 
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.write(output)
            st.write(st.session_state['past'][i], "(user)")

        #message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# results=agent_executor.run('the number of maintainenaceworkWO on 2022-09-08?')

# st.write(results)




# Using object notation
add_selectbox = st.sidebar.header(
    "AI Assistant 🤖 "
)
add_selectbox = st.sidebar.write(
    "About LLM:"
)
add_selectbox = st.sidebar.write(
    """
    Everyone has agreed and submitted to the grandeur and potential of these Large Language Models as the world is occupied with ChatGPT to solve everyday problems and businesses are preparing to harness the power of Large Language Models to their business use cases.
    
    """
)

if __name__ == "__main__":
    main()
