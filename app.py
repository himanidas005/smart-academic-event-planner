import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Smart Academic Event Planner",
    layout="wide"
)

st.title("Smart Academic Event Planning Using Student Feedback Analytics")

st.write(
    "This AI-based system analyzes student learning interests "
    "and recommends the most suitable workshop topic."
)

# --------------------------
# Session State
# --------------------------
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

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

comment = st.text_area(
    "Describe what you want to learn or improve"
)

preferred_mode = st.selectbox(
    "Preferred Event Type",
    ["Workshop", "Seminar", "Training", "Bootcamp"]
)

# --------------------------
# Submit Feedback
# --------------------------
if st.button("Submit Feedback"):
    if comment.strip():
        st.session_state.feedback_list.append(comment.strip())
        st.success("Feedback submitted successfully!")

# --------------------------
# AI Recommendation Logic
# --------------------------
st.subheader("Analytics Dashboard")

if st.session_state.feedback_list:

    feedback_df = pd.DataFrame(
        st.session_state.feedback_list,
        columns=["feedback"]
    )

    # TF-IDF keyword extraction
   custom_stop_words = [
    "want", "need", "improve", "learn",
    "interested", "skills", "skill",
    "workshop", "training", "seminar",
    "improvement", "improving",
    "basic", "advanced", "help"
]

vectorizer = TfidfVectorizer(
    stop_words=custom_stop_words,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(feedback_df["feedback"])
    X = vectorizer.fit_transform(feedback_df["feedback"])

    word_scores = X.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()

    keyword_df = pd.DataFrame({
        "topic": words,
        "count": word_scores
    })

    keyword_df = keyword_df.sort_values(
        by="count",
        ascending=False
    ).head(10)

    # Recommended workshop
    recommended_topic = keyword_df.iloc[0]["topic"].title()

    st.metric(
        "Recommended Workshop",
        f"{recommended_topic} Workshop"
    )

    # Dynamic chart
    chart_data = keyword_df.set_index("topic")["count"]

    st.bar_chart(chart_data)

else:
    st.info("No feedback submitted yet.")
