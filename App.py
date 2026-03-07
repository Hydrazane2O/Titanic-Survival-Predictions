import streamlit as st
import pandas as pd
import pickle
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)


st.title("Titanic Survival Predictor 🚢")
st.write("Enter passenger details to see if they would have survived.")


pclass = st.selectbox("Ticket Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare Paid", 0.0, 500.0, 32.0)


sex_val = 0 if sex == "male" else 1

input_data = None

if st.button("Predict Survival"):
    input_data = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare]],
    columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])
    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("Result: This passenger would have SURVIVED! 🎉")
        else:
            st.error("Result: This passenger would NOT have survived. 😔")
    except Exception as e:
        st.error(f"Prediction error: {e}")





