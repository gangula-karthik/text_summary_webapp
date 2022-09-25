import streamlit as st
from transformers import pipeline 
import requests
from bs4 import BeautifulSoup
import gc

tab1, tab2 = st.tabs(["Link", "Text"])

gc.enable()

with tab1:
    st.title("Text Summary App 📚")
    st.header("Enter your link below")
    textLink = st.text_input("Enter your link below:")
    if textLink  != "":
        r = requests.get(textLink)
        soup = BeautifulSoup(r.text, features="html.parser")
        results = soup.find_all("p")

        text = ""
        for sent in results: 
            text += sent.get_text()

        st.header("Summary")
        if text != "":
            summarizer = pipeline("summarization")
            hf_summary_text = None
            hf_summary_link = summarizer(text, max_length= 500, min_length= 300, do_sample= False, truncation=True)
            st.write(hf_summary_link[0]['summary_text'])
        gc.collect()


with tab2:
    st.title("Text Summary App 📚")
    st.header("Enter your text below:")
    text = st.text_area("Enter your text below:")
    if text != "":
        st.header("Summary:")
        summarizer = pipeline("summarization")
        hf_summary_link = None
        hf_summary_text = summarizer(text, max_length= 30, min_length= 10, do_sample= False, truncation=True)
        st.write(hf_summary_text[0]['summary_text'])
    gc.collect()
