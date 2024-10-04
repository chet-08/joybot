import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time
import google.generativeai

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


# Function to handle button click and update session state
def handle_click():
    st.session_state.user_input = ""  # Clear the input field in session state


# Streamlit app setup
st.set_page_config(
    page_title="Joy - Your AI Therapist",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# App Title
st.title("Joy - Your AI Therapist 💖")
st.markdown(
    """
    <style>
        .stTitle {
            color: white; 
            font-weight: bold; 
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Disclaimer
st.markdown(
    """
    <div class="disclaimer">A safe and loving space for your thoughts and feelings. 😊</div>
    <style>
        .disclaimer {
            text-align: top left;
            font-size: 1.8em;
            color: white; 
            margin-bottom: 20px;
            animation: fade-in 2s ease; 
        }
        @keyframes fade-in {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sign Up/Login Buttons (Top Right) ---
st.markdown(
    """
    <div class="auth-buttons">
        <button class="animated-button">Sign Up</button>
        <button class="animated-button">Login</button>
    </div>
    <style>
        .auth-buttons {
            position: fixed;
            top: 60px;
            right: 20px;
            display: flex;
            gap: 10px;
            z-index: 101; 
        }

        /* Cerise color for Sign Up/Login buttons */
        .auth-buttons .animated-button {
            background-color: #DE3163; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar with Animated Buttons ---
st.sidebar.markdown(
    """
    <div class="sidebar-buttons">
        <button class="animated-button">Mood Journal</button><br>
        <button class="animated-button">Mood Boosters</button><br>
        <button class="animated-button">Positive Activities</button><br>
        <button class="animated-button">Use Your Trigger Plan</button><br>
        <button class="animated-button">Goal Trainer</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat History Container
chat_history = st.container()

# Improved Prompt Template
prompt_template = """
You are Joy, a friendly and supportive AI therapist. Your goal is to make users feel heard, understood, and empowered. 

Remember to:

* **Acknowledge and Validate:** Let the user know you understand and their feelings are valid.
* **Personalize:**  Use details from previous conversations to make responses feel personal.
* **Reduce Cognitive Load:** Keep your responses simple, direct, and not overwhelming.
* **Encourage Self-Care:** Suggest self-care activities that could help.
* **Be Calming and Supportive:** Create a relaxing and safe space with your tone. 
* **Offer Resources:** Provide helpful resources or exercises when appropriate.

Here's the user's current message:

{question}
"""

# Input Area
with st.container():
    st.markdown("<br>", unsafe_allow_html=True)

    # Use session state to store and manage user input
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    user_input = st.text_input(
        "Enter your question:",
        key="user_input",
        value=st.session_state.user_input,
        placeholder="Type your question here...",
    )

    # Centered "Ask" button
    st.markdown(
        '<div style="display: flex; justify-content: center;"></div>',
        unsafe_allow_html=True,
    )
    if st.button("Ask", on_click=handle_click):
        with st.spinner("Joy is listening..."):
            time.sleep(1)  # Simulate thinking time
            response = get_gemini_response(user_input, prompt_template)
            time.sleep(1)

        # Add user query and response to chat history
        chat_history.markdown(f"**You:** {user_input}")
        chat_history.markdown(f"**Joy:** {response}")

# --- Breathing Circle Animation (Bottom Left) ---
st.markdown(
    """
    <div class="breathing-circle">
        <div class="breathing-circle-text">
            3 Mins <br>
            Meditation
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Talk to a Professional Button (Bottom Right) ---
st.markdown(
    """
    <div class="talk-button">
        <button class="animated-button">Talk to a Professional</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Custom CSS 
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://wallpaperaccess.com/full/1761719.jpg");  
            background-size: cover;
            font-family: 'Candara', candara ;
            overflow-x: hidden;
            margin: 0;
            padding: 0;
            color: white; 
        }

        /* ... (Other CSS styles) ... */

        /* Breathing Circle Animation */
        .breathing-circle {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 80px; 
            height: 80px; 
            border-radius: 50%;
            background-color: #DE3163; 
            animation: breathe 4s ease-in-out infinite; 
            z-index: 100;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
        }

        @keyframes breathe {
            0% {
                transform: scale(0.9);
                opacity: 0.7; 
            }
            50% {
                transform: scale(1.1);
                opacity: 1;    
            }
            100% {
                transform: scale(0.9);
                opacity: 0.7; 
            }
        }

        .breathing-circle-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 16px;
            color: black;
            text-align: center;
        }

        /* Talk to a Professional Button */
        .talk-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 101;
        }

        /* Sidebar Button Styling */
        .sidebar-buttons {
            margin-top: 50px; 
        }

        /* All Animated Buttons -  #DE3163 (Cerise) Color */
        .animated-button {
            background-color: #DE3163; 
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            cursor: pointer;
            width: 100%; 
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            font-size: 1em;
            transition: transform 0.1s ease, box-shadow 0.1s ease;
        }

        .animated-button:hover {
            transform: translateY(-2px); 
            box-shadow: 0 5px 8px rgba(0, 0, 0, 0.15);
        }

        /* ... (Other CSS styles) ... */

    </style>
    """,
    unsafe_allow_html=True,
)