import streamlit

streamlit.title("Text Summary App 🚀")

streamlit.header("Enter your text below:")
text = streamlit.text_area("")
streamlit.header("Summary:")
streamlit.write(text)


# Run the app
if __name__ == "__main__":
    streamlit.run()