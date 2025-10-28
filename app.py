import streamlit as st
import subprocess
import os

st.set_page_config(page_title="AI-Powered Multimodal MCP Chatbot", page_icon="🤖")

st.title("🤖 AI-Powered Multimodal MCP Chatbot")
st.write("Welcome! This app interfaces with your Jac-based MCP system.")

# Simple input UI
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    if user_input.strip():
        st.write("Thinking...")

        # Example: Run Jac or Python backend logic
        # You can customize this subprocess call to your actual chatbot logic
        result = subprocess.getoutput(f"python3 mcp_client.jac '{user_input}'")
        st.success(result)
    else:
        st.warning("Please type a message before sending.")

st.divider()
st.caption("Built by PollyM-tech | Powered by Jac + Streamlit")
