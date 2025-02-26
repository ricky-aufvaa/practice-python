import requests
import streamlit as st 


st.title("My app")
name = st.text_input("Enter the name")
role = st.text_input("Enter the role")

submit = st.button("Submit")
show_all = st.button("show all the employees")
if submit:
    if name and role:
        data = {
            "name":name,
            "role":role
        }
        response = requests.post("http://127.0.0.1:5000/api/friend",json=data)
        if response.status_code==200:
            result = response.json()
            st.success(result["name"])

if show_all:
    response = requests.get("http://127.0.0.1:5000/api/friend")
    if response.status_code ==200:
        results = response.json()
        st.success("The following are teh name and roles of all the employees working here: -")
        for result in results:
            st.success(f"{result["name"]}: {result["role"]}")
