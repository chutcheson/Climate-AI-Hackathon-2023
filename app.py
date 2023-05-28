import streamlit as st
from diaita.load import load_collection
from diaita.query import assistant
from streamlit_chat import message

# load the collection of documents
collection = load_collection()

# initialize the Streamlit session state if it doesn't exist yet
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    st.session_state['past'] = []

# make a text input for the user's query
user_query = st.text_input("Enter your query:")

# when the user presses the 'Submit' button
if st.button('Submit'):
    # store the user's query
    st.session_state['past'].append(user_query)

    # use the assistant function to generate a response
    assistant_response = assistant(user_query, collection)
    
    # store the assistant's response
    st.session_state['generated'].append(assistant_response)

# create a container for the chat messages
response_container = st.container()

# display the messages
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

