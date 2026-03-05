 🚢 Titanic Survival Predictor

A Streamlit web application that deploys a **Random Forest Classifier** model to predict the survival of passengers on the Titanic based on user input.

---

## 📖 About This Project

This application allows users to input passenger details and receive a prediction on whether the passenger would have survived the Titanic disaster. The model is trained using historical Titanic passenger data and deployed using Streamlit for an interactive user experience.

---

## ✨ Features

- 🤖 **Machine Learning Model**: Random Forest Classifier for accurate predictions
- 🎨 **Interactive UI**: Clean and intuitive Streamlit interface
- 📊 **Prediction Probabilities**: Shows confidence scores for predictions
- 📁 **Batch Predictions**: Upload CSV files for multiple predictions
- 🚀 **Easy Deployment**: Ready for Streamlit Cloud deployment

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Git
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-survival-predictor.git
cd titanic-survival-predictor
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### Local Development

Run the Streamlit app locally:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

### Input Features

Enter the following passenger details in the sidebar:

| Feature | Description |
|---------|-------------|
| **Pclass** | Passenger Class (1, 2, or 3) |
| **Sex** | Gender (0 = Male, 1 = Female) |
| **Age** | Age in years |
| **SibSp** | Number of siblings/spouses aboard |
| **Parch** | Number of parents/children aboard |
| **Fare** | Ticket fare paid |
| **Embarked** | Port of embarkation (0 = C, 1 = Q, 2 = S) |

### Batch Predictions

1. Upload a CSV file with the same features as above
2. Click "Predict on Uploaded Data"
3. View predictions in the results table

---

## 📁 Project Structure

```
titanic-survival-predictor/
├── app.py                    # Streamlit application
├── model.pkl                 # Trained Random Forest model
├── feature_names.pkl         # Feature names for the model
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # This file
└── .streamlit/
    └── config.toml           # Streamlit configuration (optional)
```

---

## 📦 Requirements

```text
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
```

---

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New App**
4. Select your GitHub repository
5. Set the main file to `app.py`
6. Click **Deploy**

### Deployment Checklist

- [ ] `app.py` is in the root directory
- [ ] `requirements.txt` is present
- [ ] `model.pkl` is included in the repository
- [ ] `.gitignore` is configured correctly
- [ ] All dependencies are listed in `requirements.txt`

---

## 🧪 Model Information

| Property | Value |
|----------|-------|
| **Model Type** | RandomForestClassifier |
| **Training Dataset** | Titanic Dataset (Kaggle) |
| **Features** | 7 (Pclass, Sex, Age, SibSp, Parch, Fare, Embarked) |
| **Accuracy** | ~80-85% (on test data) |
| **Framework** | scikit-learn |

---
---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---


## 🙏 Acknowledgments

- [Titanic Dataset](https://www.kaggle.com/c/titanic/data) - Kaggle
- [Streamlit](https://streamlit.io/) - Web app framework
- [scikit-learn](https://scikit-learn.org/) - Machine learning library

---

## 📞 Support

For issues or questions, please open an issue on the [GitHub repository](https://github.com/yourusername/titanic-survival-predictor/issues).

---

<div align="center">

**Made with ❤️ using Streamlit & scikit-learn**

</div>
