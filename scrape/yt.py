import streamlit as st
st.title("AI Web Scrapper")
url = st.text_input("Enter a website url")

if st.button("scrapppe site"):
    st.write("scraping the website")
