# Import necessary modules
import streamlit as st

def app():
    """This function creates the home page"""
    
    # Add title to the home page with customized style
    st.markdown(
    """
    <style>
        .typewriter {
            font-family: 'Times New Roman', serif;
            color: lightblue;
            overflow: hidden; /* Ensures text disappears as it types */
            white-space: nowrap; /* Keeps the text on a single line */
            border-right: 0.15em solid transparent; /* Invisible caret */
            animation: typing 2.5s steps(40, end) forwards;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
    </style>

    <h1 class="typewriter" style="text-align: center; font-size: 36px;">
        Welcome to the Diabetes Predictor Web App!
    </h1>
    """, unsafe_allow_html=True)




    # Add image to the home page
    st.image("./images/home.png")

    # Add brief description of your web app
    st.markdown(
    """<p style="font-size:20px; font-family: 'Times New Roman', serif;">
            I developed this web app to assess diabetes risk and provide valuable health insights. Diabetes disrupts how your body processes energy, and while there's no cure, a healthier lifestyle can help mitigate its effects. The app uses a Random Forest Classifier to analyze health indicators and offer predictions, helping you make informed decisions and manage your well-being effectively.
        </p>
    """, unsafe_allow_html=True)

    
    # Add contact information with colorful icons side by side and increase their size
    st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size:24px; font-weight:bold; margin-bottom: 20px;">
            ✨ Stay Connected
        </p>
        <a href="https://www.linkedin.com/in/pareshpatil11/" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" style="margin: 0 15px;"/>
        </a>
        <a href="https://github.com/Paresh-Patil-11" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/github.png" alt="GitHub" style="margin: 0 15px;"/>
        </a>
        <a href="https://paresh-patil-11.github.io/Paresh-Portfolio/" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/domain.png" alt="Portfolio" style="margin: 0 15px;"/>
        </a>
    </div>
    """, unsafe_allow_html=True)
