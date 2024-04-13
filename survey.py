import streamlit as st

def main():
    st.title("Survey")

    # Age group
    age_group = st.selectbox("Your age group", ["10-20", "20-30", "30+"])

    # Working/Student
    work_status = st.radio("Are you currently working or a student?", ["Working", "Student"])

    # Type of work
    work_type = st.selectbox("What kind of work are you doing right now?", ["Non IT", "Software Development", "Analytics", "Others"])

    # Interest in ML
    interest_ml = st.radio("Are you interested in Machine Learning?", ["Yes", "No"])

    # Machine Learning knowledge level
    ml_knowledge = st.selectbox("How much do you know about Machine Learning?", ["Basic", "Intermediate", "Advanced", "Nothing"])

    # Frequency of using ML topics
    ml_frequency = st.selectbox("How frequently do you use ML topics?", ["Rarely", "Occasionally", "Regularly", "Frequently"])

    # Knowledge about Hugging Face or Other API
    api_knowledge = st.radio("Are you familiar with Hugging Face or other APIs?", ["Yes", "No"])

    # Ever built a model
    built_model = st.radio("Have you ever built any ML model?", ["Yes", "No"])

    # Model name
    model_name = st.text_input("If yes, please specify the model name")

    # Ease of use rating
    ease_of_use_rating = st.slider("How would you rate the ease of use of current APIs and models?", min_value=1, max_value=5, value=3)
    
    # Do you need any easy way to build ML models to deploy
    easy_to_use_model = st.radio("Automated Pretrained ML Models?", ["Yes", "No"])

    st.write("\n---\n")
    st.write("### Survey Results:")
    st.write(f"- Age Group: {age_group}")
    st.write(f"- Working/Student: {work_status}")
    st.write(f"- Type of Work: {work_type}")
    st.write(f"- Interest in ML: {interest_ml}")
    st.write(f"- ML Knowledge Level: {ml_knowledge}")
    st.write(f"- Frequency of Using ML Topics: {ml_frequency}")
    st.write(f"- Knowledge about Hugging Face or Other API: {api_knowledge}")
    st.write(f"- Ever Built a Model: {built_model}")
    if built_model == "Yes":
        st.write(f"- Model Name: {model_name}")
    st.write(f"- Ease of Use Rating: {ease_of_use_rating}")
    st.write(f"- Question: {easy_to_use_model}")

if __name__ == "__main__":
    main()
