import streamlit as st
from web_functions import load_data
from Tabs import home, data, predict

st.set_page_config(
    page_title = 'Diabetes Prediction',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict
}

st.sidebar.title("𝙽𝚊𝚟𝚒𝚐𝚊𝚝𝚒𝚘𝚗")
page = st.sidebar.radio("Pages", list(Tabs.keys()))
df, X, y = load_data()

if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
