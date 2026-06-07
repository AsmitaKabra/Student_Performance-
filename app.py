import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #4CAF50;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #AAAAAA;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown(
    '<p class="main-title">📚 Student Performance Prediction</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Predict a student\'s Math Score using Machine Learning</p>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("📖 About Project")

st.sidebar.info(
    """
    This application predicts a student's **Math Score**
    based on:

    - Gender
    - Race/Ethnicity
    - Parental Education
    - Lunch Type
    - Test Preparation Course
    - Reading Score
    - Writing Score

    Built using:
    - Scikit-Learn
    - CatBoost
    - Streamlit
    """
)

# ---------------- INPUT FORM ---------------- #

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        ["female", "male"]
    )

    race_ethnicity = st.selectbox(
        "🌎 Race/Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ]
    )

    parental_level_of_education = st.selectbox(
        "🎓 Parent Education",
        [
            "associate's degree",
            "bachelor's degree",
            "high school",
            "master's degree",
            "some college",
            "some high school"
        ]
    )

with col2:

    lunch = st.selectbox(
        "🍽️ Lunch Type",
        [
            "standard",
            "free/reduced"
        ]
    )

    test_preparation_course = st.selectbox(
        "📝 Test Preparation",
        [
            "none",
            "completed"
        ]
    )

# ---------------- SCORES ---------------- #

st.markdown("### 📊 Academic Scores")

col3, col4 = st.columns(2)

with col3:
    reading_score = st.slider(
        "Reading Score",
        0,
        100,
        50
    )

with col4:
    writing_score = st.slider(
        "Writing Score",
        0,
        100,
        50
    )

st.write("")

# ---------------- PREDICT BUTTON ---------------- #

if st.button("🚀 Predict Math Score", use_container_width=True):

    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()

    result = predict_pipeline.predict(pred_df)

    prediction = round(result[0], 2)

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="📈 Predicted Math Score",
        value=prediction
    )

    if prediction >= 80:
        st.balloons()
        st.success("Excellent Performance Expected!")
    elif prediction >= 60:
        st.info("Good Performance Expected!")
    else:
        st.warning("Student may need additional academic support.")

