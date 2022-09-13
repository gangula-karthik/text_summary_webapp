import streamlit
from transformers import pipeline 

streamlit.title("Text Summary App 📚")

streamlit.header("Enter your text below:")
text = streamlit.text_area("")
streamlit.header("Summary:")
if text != "":
    summarizer = pipeline("summarization")
    hf_summary = summarizer(text, max_length= 500, min_length= 100, do_sample= False, truncation=True)
    streamlit.write(hf_summary[0]['summary_text'])



# import platform
# print(platform.platform())