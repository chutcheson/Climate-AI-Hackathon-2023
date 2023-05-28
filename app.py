import streamlit as st
from streamlit_chat import message

# Title of the app
st.title("Diaita")

# Button click
if st.button("Submit"):
    # Display the user's name and selected color
    st.write(f"Hello, {name}!")
    st.write(f"You selected {color}.")

# Streamlit message display
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
