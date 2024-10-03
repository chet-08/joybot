import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()  # Load environment variables from .env file

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question, prompt_template):
    full_prompt = prompt_template.format(question=question)
    response = chat.send_message(full_prompt, stream=True)
    text_response = ""
    for chunk in response:
        text_response += chunk.text
    return text_response

# Streamlit app setup
st.set_page_config(
    page_title="Joy - Your AI Therapist",
    page_icon="💖", # Change to a heart icon
    layout="wide",
    initial_sidebar_state="collapsed",
)

# App Title
st.title("Joy - Your AI Therapist 💖") # Change to a heart icon

# Disclaimer
st.markdown("A safe and loving space for your thoughts and feelings. 😊")

# Chat History Container
chat_history = st.empty() 

# Prompt Template (You can customize this!)
prompt_template = """
How are you feeling today, friend?  I'm here to listen without judgment.  
{question}
"""

# Function to handle user input and display response
def handle_user_input():
    input_area = st.empty()
    input = input_area.text_input("Enter your question:", key="input", placeholder="Type your question here...")
    submit = st.button("Ask", use_container_width=True)

    if submit and input:
        with st.spinner("Joy is listening..."):
            time.sleep(1)  # Simulate typing time
            response = get_gemini_response(input, prompt_template)
            time.sleep(1)  # Simulate thinking time

        # Add user query and response to chat history
        chat_history.markdown(f"**You:** {input}")
        chat_history.markdown(f"**Joy:** {response}")

        # Clear the input field
        input_area.text_input("Enter your question:", key="input_clear", value="") 

# Call the input handling function
handle_user_input() 

# Custom CSS for a ChatGPT-like interface with a professional dark theme
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom, #333399, #2962FF); /* Darker purple to dark blue gradient */
            color: #eee;       /* Light text */
            font-family: 'Arial', sans-serif; /* Clean, easy-to-read font */
            overflow-x: hidden; /* Hide horizontal scrollbar */
            margin: 0; /* Remove default margins */
            padding: 0; /* Remove default padding */
        }

        .stTitle {
            color: #eee;       /* Light text */
            text-align: center;
            font-size: 2.8em; /* Larger font size for the title */
            margin-bottom: 30px; /* Add more space below the title */
            font-weight: bold; /* Bold title */
            font-family: 'Pacifico', cursive;  /* A more friendly font for the title */
        }

        .chat-history {
            max-height: 400px;  /* Set the maximum height */
            overflow-y: auto;  /* Enable vertical scrolling */
            padding: 15px;
            border: 1px solid #444; /* Darker border */
            border-radius: 10px;
            margin-bottom: 20px;
            background-color: #333; /* Darker background for chat history */
            font-size: 1.3em; /* Slightly larger font size for readability */
            font-weight: 400; /* Slightly bolder font weight */
            line-height: 1.5; /* Adjust line height for better readability */
        }

        .chat-history .you {
            text-align: right;
            color: #fff; /* White for user messages */
            font-weight: bold;
            margin-bottom: 10px;
        }

        .chat-history .bot {
            text-align: left;
            color: #eee;    /* Light text for bot messages */
            margin-bottom: 10px;
        }

        .stTextInput {
            background-color: #333; /* Darker blue input field */
            color: #eee;       /* Light text in input */
            border: 1px solid #444; /* Darker border */
            border-radius: 8px;
            padding: 12px;
            font-size: 1.1em; /* Slightly larger font size for readability */
            margin-bottom: 15px; /* Add spacing below the input field */
        }

        .stButton {
            background-color: #0069d9; /* Darker blue on hover */
            color: #fff;       /* White text on button */
            border: none;
            border-radius: 10px;
            padding: 12px 30px;
            cursor: pointer;
            width: 100%; /* Make the button fill the container width */
            text-align: center;
            border: none;
            box-shadow: none; /* Remove default button shadow */
            outline: none;
            font-weight: bold;
            font-size: 1.2em; /* Slightly larger font size for readability */
            transition: background-color 0.2s ease; /* Add a smooth transition for hover effect */
        }

        .stButton:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
    </style>
    """,
    unsafe_allow_html=True
)
