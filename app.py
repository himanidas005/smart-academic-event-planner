import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Smart Academic Event Planner",
    layout="wide"
)

# Title
st.title("Smart Academic Event Planning Using Student Feedback Analytics")

st.write(
    "This AI-based system collects student learning preferences "
    "and recommends workshops based on majority interest."
)

# Initialize session state
if "feedback_counts" not in st.session_state:
    st.session_state.feedback_counts = {}

# Student input form
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

topic = st.text_input("Enter Learning Topic (Example: DSA, ML, SQL)")

comment = st.text_area(
    "Describe what you want to learn or improve"
)

preferred_mode = st.selectbox(
    "Preferred Event Type",
    ["Workshop", "Seminar", "Training", "Bootcamp"]
)

# Submit button
if st.button("Submit Feedback"):
    if topic.strip():
        topic_name = topic.strip().title()

        if topic_name in st.session_state.feedback_counts:
            st.session_state.feedback_counts[topic_name] += 1
        else:
            st.session_state.feedback_counts[topic_name] = 1

        st.success("Feedback submitted successfully!")

# Analytics dashboard
st.subheader("Analytics Dashboard")

if st.session_state.feedback_counts:
    feedback_series = pd.Series(st.session_state.feedback_counts)

    st.bar_chart(feedback_series)

    recommended_topic = feedback_series.idxmax()

    st.metric("Recommended Workshop", recommended_topic)
else:
    st.info("No feedback submitted yet.")
