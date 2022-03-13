import streamlit as st
import pandas as pd
import numpy as np
import requests

URL = "https://backend-cyberbullying-apps.herokuapp.com/predict"

st.set_page_config(
    page_title = "BULLETIN (CYBERBULLYING CLASSIFICATION)",
    page_icon="👌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Resti000',
        'About': "# Cyberbullying Classification"
    }
)

st.title("BULLETIN - Cyberbullying Detector")
st.markdown("Determine if your tweet is considered as cyberbullying or not:")

if 'out' not in st.session_state:
    st.session_state.out = "Hi, hope you have a nice day!"

out = st.text_area("Your tweet:")
#res = ""
def add_text(out):
    st.session_state.out = out

submit = st.button('Submit!', on_click=add_text, args=(out, ))
#print(f'res : {res}')
if submit:
    data = {
        'Out':st.session_state.out,
    }
    r = requests.post(URL, json=data)
    #st.write(data)
    global res 
    res = r.json()
    #st.write(res)
    st.write(f"Result of tweet analysis: {res['result_model']}")

st.title("Stop Cyberbullying, right now!")
#st.header("Cyberbullying is NO NO NO")
st.image("cyberbullying.jpg")
st.header("Effects of Cyberbullying:")
st.image("cyberbullying_2.jpg")
st.subheader("\"A BETTER WORLD WITHOUT CYBERBULLYING\"")
st.subheader("BULLETIN - 2022")
col1, col2, col3 = st.columns([2, 5, 2])
col2.image("bulletin.png", use_column_width=True)
#st.image(, use_column_width=True)