# Dynamic analytics section
st.subheader("Analytics Dashboard")

# Store feedback in session state
if "feedback_counts" not in st.session_state:
    st.session_state.feedback_counts = {}

# Update count after submission
if st.button("Submit Feedback"):
    topic = comment.strip().title()

    if topic:
        if topic in st.session_state.feedback_counts:
            st.session_state.feedback_counts[topic] += 1
        else:
            st.session_state.feedback_counts[topic] = 1

        st.success("Feedback submitted successfully!")

# Show graph
if st.session_state.feedback_counts:
    feedback_series = pd.Series(st.session_state.feedback_counts)

    st.bar_chart(feedback_series)

    recommended_topic = feedback_series.idxmax()

    st.metric("Recommended Workshop", recommended_topic)
