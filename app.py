import streamlit as st
import pandas as pd

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Smart Academic Event Planner",
    layout="wide"
)

st.title("Smart Academic Event Planning Using Student Feedback Analytics")

st.write(
    "This AI-based system collects student preferred learning topics "
    "and recommends workshops based on majority demand."
)

# --------------------------
# Session State
# --------------------------
if "topic_counts" not in st.session_state:
    st.session_state.topic_counts = {}

# --------------------------
# Student Form
# --------------------------
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

# NEW MAIN INPUT
topic_name = st.text_input(
    "Enter Topic Name (Example: DSA, UI/UX, Machine Learning)"
)

# Optional detailed comment
comment = st.text_area(
    "Optional: Describe what you want to learn"
)

preferred_mode = st.selectbox(
    "Preferred Event Type",
    ["Workshop", "Seminar", "Training", "Bootcamp"]
)

# --------------------------
# Submit Feedback
# --------------------------
if st.button("Submit Feedback"):
    if topic_name.strip():
        topic = topic_name.strip().title()

        if topic in st.session_state.topic_counts:
            st.session_state.topic_counts[topic] += 1
        else:
            st.session_state.topic_counts[topic] = 1

        st.success("Feedback submitted successfully!")

# --------------------------
# Analytics Dashboard
# --------------------------
st.subheader("Analytics Dashboard")

if st.session_state.topic_counts:

    topic_df = pd.DataFrame(
        list(st.session_state.topic_counts.items()),
        columns=["Topic", "Count"]
    )

    topic_df = topic_df.sort_values(
        by="Count",
        ascending=False
    )

    recommended_topic = topic_df.iloc[0]["Topic"]

    st.metric(
        "Recommended Workshop",
        f"{recommended_topic} Workshop"
    )

    chart_data = topic_df.set_index("Topic")["Count"]

    st.bar_chart(chart_data)

else:
    st.info("No feedback submitted yet.")
