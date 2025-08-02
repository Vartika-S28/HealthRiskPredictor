import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ✅ Load your uploaded dataset
df = pd.read_csv("data/heart.csv")

# ✅ Extract Systolic and Diastolic BP from 'Blood Pressure' column
df[['SystolicBP', 'DiastolicBP']] = df['Blood Pressure'].str.split('/', expand=True)
df['SystolicBP'] = pd.to_numeric(df['SystolicBP'], errors='coerce')
df['DiastolicBP'] = pd.to_numeric(df['DiastolicBP'], errors='coerce')

# ✅ Select the 5 important features
features = ['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'SystolicBP']
df = df.dropna(subset=features + ['Heart Attack Risk'])

# ✅ Set up input X and output y
X = df[features]
y = df['Heart Attack Risk']

# ✅ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("data/heart_model.pkl", "wb") as f:
    pickle.dump(model, f)


model.score(X_test, y_test)
