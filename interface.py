import streamlit as st

# Welcome Message to User
st.write("# Welcome to The Climate Change Chat Assistant!")
st.write("Do you have a question for me, today?")


def initialize_session_state():
    st.session_state.user_input = ""
    st.session_state.chat_history = []
    # Add any other session-specific variables you need

initialize_session_state()

# Access the user input from session state
user_input = st.text_input("Question", key="user_input")

# Handle user input and chatbot logic
if st.button("Submit"):
    # Process user input with your chatbot and get a response - TO BE UPDATED
    bot_response = your_chatbot_function(user_input)

    # Append the user input and bot response to the chat history
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

    # Clear the user input field
    st.session_state.user_input = ""

# Display the chat history
st.write("Chat History:")
for entry in st.session_state.chat_history:
    st.write(f"User: {entry['user']}")
    st.write(f"Bot: {entry['bot']}")
