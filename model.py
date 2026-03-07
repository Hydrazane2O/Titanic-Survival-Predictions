# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Load data
df = pd.read_csv('C:/Users/Hydra/Downloads/group 3/Titanic-Dataset.csv')

# Preprocess
df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
df['Embarked'] = LabelEncoder().fit_transform(df['Embarked'].fillna('S'))

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# Features and target
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y = df['Survived']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save with pickle (protocol 5 for better compatibility)
with open('titanic_model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=5)

# Verify file size
file_size = os.path.getsize('titanic_model.pkl')
print(f"✅ Model saved! File size: {file_size} bytes")

if file_size < 10000:
    print("❌ File is too small! Check your code.")
else:
    print("✅ File size is correct!")