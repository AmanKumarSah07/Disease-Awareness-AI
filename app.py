import streamlit as st
import os
from dotenv import load_dotenv
from agent import get_agent_chain

# Load environment variables (if .env exists)
load_dotenv()

# Page config
st.set_page_config(page_title="AI Health Assistant", page_icon="🩺", layout="centered")

# Sidebar
with st.sidebar:
    st.title("🩺 AI Health Assistant")
    st.markdown("""
    This agent acts as a preliminary health awareness assistant. It can help you:
    - Understand possible causes of your symptoms
    - Assess disease risks
    - Learn prevention strategies
    """)
    st.warning("⚠️ **Disclaimer:** This tool is for educational and awareness purposes only. It does not replace a doctor and cannot provide professional medical diagnoses. Always consult a healthcare professional for medical advice.")
    
    # Check for Hugging FaceToken
    api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    if not api_token:
        st.markdown("---")
        st.markdown("### Setup Required")
        token_input = st.text_input("Enter your HuggingFace Token:", type="password")
        if token_input:
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = token_input
            st.success("Token saved for this session!")
            st.rerun()
        st.markdown("[Get a free HuggingFace Token here](https://huggingface.co/settings/tokens)")

st.title("How can I help you today?")

# Initialize chat history and agent in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "agent_chain" not in st.session_state:
    if os.environ.get("HUGGINGFACEHUB_API_TOKEN"):
        try:
            st.session_state.agent_chain = get_agent_chain()
        except Exception as e:
            st.error(f"Error initializing AI agent: {e}")
            st.session_state.agent_chain = None
    else:
        st.info("👈 Please enter your Hugging Face token in the sidebar to start chat functionalities.")
        st.session_state.agent_chain = None

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Describe your symptoms or ask about a disease..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if st.session_state.agent_chain:
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Format history string manually from session_state.messages
                    # to match the ChatPromptTemplate variables
                    messages = []
                    for msg in st.session_state.messages: 
                        if msg["role"] == "user":
                            messages.append(("human", msg["content"]))
                        else:
                            messages.append(("ai", msg["content"]))
                    
                    # Run the chain using invoke
                    response = st.session_state.agent_chain.invoke({"messages": messages})
                    response_text = response.content
                    
                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                except Exception as e:
                    st.error(f"An error occurred: {e}. If this is a token issue, please verify your token.")
    else:
        st.error("AI Agent is not initialized. Please provide a valid Hugging Face API token in the sidebar.")
