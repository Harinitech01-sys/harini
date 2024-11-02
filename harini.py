import streamlit as st


st.set_page_config(page_title="My Portfolio", layout="wide")


st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color:black;
        }
        h2 {
            text-align: center;
            color: #fff;
        }
        .skill {
            padding: 10px;
            border-radius: 10px;
            background: aqua;
            margin: 5px 0;
            transition: transform 0.3s;
            color:black;
        }
        .skill:hover {
            transform: scale(1.05);
        }
        .project {
            padding: 20px;
            border: 2px solid #fff;
            border-radius: 10px;
            margin: 10px 0;
            background: rgba(0, 0, 0, 0.5);
            color: #fff;
            transition: background 0.3s;
        }
        .project:hover {
            background: rgba(0, 0, 0, 0.7);
        }
    </style>
""", unsafe_allow_html=True)

# Portfolio title
st.title("My Portfolio")
st.markdown("<h2 style='background: rgb(2,0,36);background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 9%, rgba(0,212,255,1) 50%, rgba(0,212,255,1) 97%);; color: black;'>HARINI</h2>", unsafe_allow_html=True)
st.markdown(" ")
# Introduction
st.write("Welcome to my portfolio! I'm excited to share my projects and passions with you. Dive in to see what I've been working on! Creativity meets dedication, and each project is a step forward in my journey. Explore and join me on this path of growth and innovation. Thanks for stopping by!")
st.markdown(" ")
# Columns for designation and program
col1, col2 = st.columns(2)

with col1:
    st.header("Designation")
    st.markdown(
        '<div style="background-color:aqua; padding:20px; border-radius:10px;color:black">Student</div>',
        unsafe_allow_html=True
    )

with col2:
    st.header("Programme")
    st.markdown(
        '<div style="background-color:aqua; padding:20px;border-radius:10px;color:black">B.Tech in AI and DS</div>',
        unsafe_allow_html=True
    )
    st.markdown(" ")
st.image("https://nasscom.in/ai/democratizing-ai-making-advanced-technology-accessible-to-all/images/banner-bottom.jpg", width=1370)  # Adjust 700 to your desired pixel width



st.markdown("<h2 style='text-align:center;color:black;'>Skills</h2>", unsafe_allow_html=True)
skills = {
    "Python Programming": 90,
    "HTML": 80,
    "CSS": 75,
    "JavaScript": 70,
    "Bootstrap": 65,
    "Web Page Development": 70
}

for skill, level in skills.items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"<div class='skill'>{skill}</div>", unsafe_allow_html=True)
    with col2:
        st.progress(level)

st.markdown("<h2 style='text-align:center;color:white;'>Projects</h2>", unsafe_allow_html=True)
projects = [
    {
        "title": "Web Page Design",
        "description": "Designed a webpage using basic HTML, CSS, Bootstrap, and JavaScript for a chocolate shop.",
        "technologies": "HTML, CSS, Bootstrap",
    },
    {
        "title": "Social Media Login Page",
        "description": "Created a login page using JavaScript.",
        "technologies": "HTML, CSS, JavaScript",
    }
]

for project in projects:
    st.markdown(f"<div class='project'><h3>{project['title']}</h3><p>{project['description']}</p><p><strong>Technologies used:</strong> {project['technologies']}</p></div>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align:center;color:white;'>Contact</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="background-color:aqua;color:black;padding:20px;border-radius:35px;">Phone: 999776533</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="background-color:aqua;color:black;padding:20px;border-radius:35px;">Email: your.email@example.com</div>', unsafe_allow_html=True)



st.markdown(" ")
st.markdown(" ")


st.markdown("<h2 style='text-align:center;color:white;background: rgb(2,0,36);background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 9%, rgba(0,212,255,1) 50%, rgba(0,212,255,1) 97%);'>Thank You for Visiting!</h2>", unsafe_allow_html=True)

#day2
import random
st.markdown(
    """
    <style>
    
    .stAlert {
        background-color: #00FFFF; 
        color: black; 
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def display_rules(mode):
    if mode == "User Guess":
        st.write("""
        **Rules for User Guess Mode:**
        1. The computer will choose a random number between 1 and 10.
        2. You have to guess the number.
        3. After each guess, the computer will tell you if your guess is too high, too low, or correct.
        4. Keep guessing until you find the correct number!
        """)
    elif mode == "Machine Guess":
        st.write("""
        **Rules for Machine Guess Mode:**
        1. You will choose a number between 1 and 10.
        2. The computer will try to guess your number.
        3. After each guess, tell the computer if its guess is too high, too low, or correct.
        4. The game continues until the computer guesses your number!
        """)


def user_guess_mode():
    number_to_guess = random.randint(1, 10)  
    attempts = st.session_state.get("attempts", 0)

    st.write("I have selected a random number between 1 and 10. Can you guess it?")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)  
    if guess:
        attempts += 1
        st.session_state["attempts"] = attempts  
        if guess < number_to_guess:
            st.write("Too low! Try again.")
        elif guess > number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.success(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!", icon="🎉")
            st.session_state["attempts"] = 0  


def machine_guess_mode():
    st.write("Think of a number between 1 and 10, and I'll try to guess it!")
    
    low, high = st.session_state.get("low", 1), st.session_state.get("high", 10) 
    attempts = st.session_state.get("attempts", 0)
    
    if low <= high:
        guess = (low + high) // 2
        st.write(f"My guess is {guess}. Is it too high, too low, or correct?")
        
        user_feedback = st.radio("Choose:", ("Too High", "Too Low", "Correct"))
        if user_feedback == "Too High":
            high = guess - 1
            attempts += 1
        elif user_feedback == "Too Low":
            low = guess + 1
            attempts += 1
        elif user_feedback == "Correct":
            attempts += 1
            st.success(f"I guessed your number in {attempts} attempts!", icon="🤖")
            low, high, attempts = 1, 10, 0 
        
        st.session_state["low"], st.session_state["high"], st.session_state["attempts"] = low, high, attempts
    else:
        st.write("Something went wrong, please restart the game.")


st.title("Guessing Game")
mode = st.selectbox("Choose a mode:", ("User Guess", "Machine Guess"))

display_rules(mode)

if mode == "User Guess":
    user_guess_mode()
elif mode == "Machine Guess":
    machine_guess_mode()

 