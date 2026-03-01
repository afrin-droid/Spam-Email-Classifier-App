import streamlit as st
import pickle

# Load saved model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Spam Email Classifier")

user_input = st.text_area("Enter Email Text")

if st.button("Predict"):
    if user_input.strip() != "":
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)

        if prediction[0] == 1:
            st.error("This is SPAM")
        else:
            st.success("This is NOT Spam")
    else:
        st.warning("Please enter some text.")