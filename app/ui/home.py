import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vision-Crafters", page_icon="🤖")

st.title("🤖 Vision-Crafters")
st.subheader("AI-Powered Candidate Ranking System")

st.write("Welcome to Vision-Crafters!")
st.write("This application helps recruiters rank candidates based on their skills and job requirements.")

job_description = st.text_area(
    "Enter Job Description",
    placeholder="Example: Looking for a Python developer with Machine Learning and SQL skills"
)

if st.button("Show Ranked Candidates"):

    df = pd.read_csv("app/data/candidates.csv")

    if "python" in job_description.lower():
        df["Score"] = df["Skills"].apply(
            lambda x: 100 if "Python" in x else 70
        )

    elif "java" in job_description.lower():
        df["Score"] = df["Skills"].apply(
            lambda x: 100 if "Java" in x else 70
        )

    else:
        df["Score"] = 80

    df = df.sort_values(by="Score", ascending=False)

    st.dataframe(df)

    st.success(f"Top Candidate: {df.iloc[0]['Name']}")

    st.metric("Total Candidates", len(df))
    st.metric("Highest Score", df["Score"].max())

    st.bar_chart(df.set_index("Name")["Score"])