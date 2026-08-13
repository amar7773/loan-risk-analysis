import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Loan Risk Assistant",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Loan Risk Assistant")
st.write("Machine Learning + NLP + FastAPI")
st.divider()
st.header("💰 Loan Risk Prediction")
col1, col2 = st.columns(2)
with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    salary = st.number_input(
        "Salary",
        min_value=0,
        value=300000,
        step=10000
    )

    loan = st.number_input(
        "Loan Amount",
        min_value=0,
        value=500000,
        step=10000
    )


with col2:

    credit = st.number_input(
        "Credit Score",
        min_value=0,
        max_value=900,
        value=750
    )

    exp = st.number_input(
        "Experience",
        min_value=0,
        max_value=50,
        value=2
    )


if st.button("🔮 Predict Loan Risk"):

    data = {
        "age": age,
        "salary": salary,
        "loan": loan,
        "credit": credit,
        "exp": exp
    }

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction Completed")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Prediction",
                    result["prediction"]
                )

            with col2:
                st.metric(
                    "Probability",
                    f'{result["probability"]}%'
                )

            with col3:
                st.metric(
                    "Status",
                    result["status"]
                )

        else:

            st.error("Prediction API Error")

    except Exception as e:

        st.error(
            f"FastAPI server connect nahi ho raha: {e}"
        )


st.divider()


# ==========================================
# AI LOAN ASSISTANT
# ==========================================

st.header("💬 AI Loan Assistant")

question = st.text_input(
    "Ask your question",
    placeholder="Example: Can I check my loan risk?"
)


if st.button("🤖 Ask Assistant"):

    if question.strip() == "":

        st.warning("Please enter your question.")

    else:

        data = {
            "text": question
        }

        try:

            response = requests.post(
                f"{API_URL}/assitant",
                json=data
            )

            if response.status_code == 200:

                result = response.json()

                st.info(
                    f"Intent: {result['intent']}"
                )

                if "response" in result:

                    st.success(
                        result["response"]
                    )

                if "prediction" in result:

                    st.success(
                        f"Prediction: {result['prediction']}"
                    )

                    st.metric(
                        "Probability",
                        f'{result["probability"]}%'
                    )

                    st.metric(
                        "Status",
                        result["status"]
                    )

            else:

                st.error("Assistant API Error")

        except Exception as e:

            st.error(
                f"FastAPI server connect nahi ho raha: {e}"
            )