# main.py
from time import time
import time
from dotenv import load_dotenv
import os
import streamlit as st
from graphs.graph import graph

load_dotenv()

st.set_page_config(page_title="Blog Generator", layout="wide")

st.title("🧠 AI Blog Generator")

topic="The future of AI in healthcare"

if st.button("Generate Blog"):

    with st.spinner("Generating blog..."):
        result = graph.invoke({"topic": topic})

    st.success("Blog Generated!")

    st.subheader("📝 Blog Output")

    st.markdown(result["blog"])

    st.download_button(
        "Download Blog",
        result["blog"],
        file_name="blog.txt"
    )