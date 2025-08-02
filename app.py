from flask import Flask, render_template, request
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Load trained model
with open("data/heart_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    input_vals = []
    show_chart = False
    advice_list = None  # default

    if request.method == "POST":
        try:
            age = float(request.form['age'])
            chol = float(request.form['cholesterol'])
            hr = float(request.form['heart_rate'])
            bmi = float(request.form['bmi'])
            sbp = float(request.form['systolic_bp'])

            input_vals = [age, chol, hr, bmi, sbp]

            # Check for dangerously low vitals
            if hr < 45 or sbp < 70:
                prediction = "⚠️ Dangerously low readings — Immediate medical attention recommended."
                advice_list = []
                if hr < 45:
                    advice_list.append("• Heart rate is dangerously low. Seek emergency medical help.")
                if sbp < 70:
                    advice_list.append("• Systolic blood pressure is too low. Risk of collapse. Visit ER immediately.")
                return render_template("index.html",
                                       input_vals=input_vals,
                                       prediction=prediction,
                                       probability=None,
                                       show_chart=False,
                                       advice=advice_list)

            # Normal prediction
            data = np.array(input_vals).reshape(1, -1)
            pred = model.predict(data)[0]
            prob = model.predict_proba(data)[0][1]

            prediction = "🔴 High Risk (Heart Attack Likely)" if pred == 1 else "🟢 Low Risk"
            probability = round(prob * 100, 2)
            show_chart = True

            # Feature importances chart
            feat_names = ['Age', 'Cholesterol', 'Heart Rate', 'BMI', 'SystolicBP']
            importances = model.feature_importances_
            plt.figure(figsize=(6, 3))
            sns.barplot(x=importances, y=feat_names, palette="Reds_r")
            plt.title("Feature Impact")
            plt.tight_layout()
            plt.savefig("static/feature_impact.png")
            plt.close()

            # If user clicked "Get Health Tips"
            if request.form.get("get_advice") == "true":
                advice_list = []

                if age > 50:
                    advice_list.append("Regular cardiac checkups recommended after age 50.")
                if chol > 200:
                    advice_list.append("High cholesterol detected. Consider dietary changes and consulting a doctor.")
                if hr > 100:
                    advice_list.append("Elevated heart rate. Try to reduce stress or get a clinical evaluation.")
                if bmi > 25:
                    advice_list.append("Your BMI indicates overweight. Regular exercise and diet control advised.")
                if sbp > 140:
                    advice_list.append("High blood pressure detected. Reduce salt intake and consult your doctor.")

                # If all values are normal
                if not advice_list:
                    advice_list.append("All your entered health parameters appear to be in a safe range. Keep it up!")

                return render_template("index.html",
                                       input_vals=input_vals,
                                       prediction=prediction,
                                       probability=probability,
                                       show_chart=show_chart,
                                       advice=advice_list)

        except ValueError:
            prediction = "⚠️ Please enter valid numeric values."

    return render_template("index.html",
                           input_vals=input_vals,
                           prediction=prediction,
                           probability=probability,
                           show_chart=show_chart)

if __name__ == "__main__":
    app.run(debug=True)
