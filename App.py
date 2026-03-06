import gradio as gr
import joblib
import pandas as pd

# Load model
model = joblib.load('titanic_model.pkl')

def predict_survival(pclass, sex, age, sibsp, parch, fare):
    """Predict Titanic survival based on passenger details"""
    try:
        # Convert sex to numeric (0 = male, 1 = female)
        sex_val = 0 if sex == "male" else 1
        
        # Create input DataFrame
        input_data = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare]], 
                                  columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        # Format result
        if prediction == 1:
            result = f"🎉 **SURVIVED!**\n\nConfidence: {max(probability):.2%}"
        else:
            result = f"😔 **NOT SURVIVED**\n\nConfidence: {max(probability):.2%}"
        
        return result
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=predict_survival,
    inputs=[
        gr.Number(label="Ticket Class (1, 2, or 3)", value=1, step=1),
        gr.Radio(choices=["male", "female"], label="Sex", value="male"),
        gr.Slider(minimum=0, maximum=100, value=25, label="Age"),
        gr.Number(label="Siblings/Spouses Aboard", value=0, step=1),
        gr.Number(label="Parents/Children Aboard", value=0, step=1),
        gr.Number(label="Fare Paid ($)", value=32.0, step=0.1)
    ],
    outputs="text",
    title="🚢 Titanic Survival Predictor",
    description="Enter passenger details to predict if they would have survived the Titanic disaster.",
    examples=[
        [1, "female", 29, 0, 0, 211.5],
        [3, "male", 22, 1, 0, 7.25],
        [1, "male", 38, 1, 0, 71.2833],
        [3, "female", 35, 0, 0, 16.0],
    ],
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()