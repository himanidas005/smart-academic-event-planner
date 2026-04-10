import streamlit as st
import pandas as pd
import random

# Page settings
st.set_page_config(
    page_title="Smart Academic Event Planner",
    layout="wide"
)

# Title
st.title("Smart Academic Event Planning Using Student Feedback Analytics")

# Description
st.write(
    "This AI-based system collects student learning preferences "
    "and recommends workshops based on majority interest."
)

# Input section
st.subheader("Student Feedback Form")

student_name = st.text_input("Enter Student Name")

department = st.selectbox(
    "Select Department",
    ["CSE", "DS", "IT", "ECE", "EEE"]
)

skill_level = st.selectbox(
    "Current Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

comment = st.text_area(
    "Describe what you want to learn or improve"
)

preferred_mode = st.selectbox(
    "Preferred Event Type",
    ["Workshop", "Seminar", "Training", "Bootcamp"]
)

# Submit button
if st.button("Submit Feedback"):
    st.success("Feedback submitted successfully!")

# Simulated analytics section
st.subheader("Analytics Dashboard")

topics = [
    "Machine Learning Workshop",
    "Cloud and AWS Bootcamp",
    "SQL and Data Engineering Seminar",
    "DSA Interview Preparation Training",
    "Web Development Bootcamp"
]

recommended_topic = random.choice(topics)

st.metric("Recommended Workshop", recommended_topic)

# Sample analytics graph
sample_counts = pd.Series(
    [320, 250, 180, 210, 140],
    index=["ML", "Cloud", "SQL", "DSA", "Web"]
)

st.bar_chart(sample_counts)
