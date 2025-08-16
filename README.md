# ❤️ Heart Attack Risk Predictor

A machine learning web application that predicts heart attack risk based on key health parameters using a Random Forest classifier.

## 🚀 Features

- **Real-time Risk Assessment**: Input your health parameters and get instant heart attack risk predictions
- **Personalized Health Tips**: Receive tailored health advice based on your input values
- **Feature Impact Visualization**: See which health factors most influence the prediction
- **Emergency Alerts**: Automatic detection of dangerously low vital signs with immediate medical recommendations
- **User-friendly Interface**: Clean, responsive web interface with intuitive design

## 📊 Health Parameters Analyzed

The application analyzes the following 5 key health indicators:

1. **Age** - Age in years
2. **Cholesterol** - Total cholesterol level (mg/dl)
3. **Heart Rate** - Resting heart rate (beats per minute)
4. **BMI** - Body Mass Index
5. **Systolic Blood Pressure** - Systolic blood pressure reading (mmHg)

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Visualization**: Matplotlib & Seaborn
- **Frontend**: HTML, CSS
- **Data Processing**: Pandas, NumPy

## 📁 Project Structure

```
health_risk/
├── app.py                 # Main Flask application
├── train_model.py         # Model training script
├── data/
│   ├── heart.csv         # Training dataset
│   ├── heart_model.pkl   # Trained model file
│   └── diabetes.csv      # Additional dataset
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── style.css         # Styling
│   ├── feature_impact.png # Generated charts
│   └── feature_importance.png
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd health_risk
   ```

2. **Install required dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn matplotlib seaborn
   ```

3. **Train the model** (if not already trained)
   ```bash
   python train_model.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 How to Use

1. **Enter Health Data**: Fill in the form with your current health parameters
2. **Get Prediction**: Click "Predict Risk" to receive your risk assessment
3. **View Results**: See your risk level (Low/High) with confidence percentage
4. **Get Health Tips**: Click "Get Health Tips" for personalized advice
5. **Analyze Features**: View the feature impact chart to understand which factors most influence your risk

## ⚠️ Important Notes

- **Medical Disclaimer**: This tool is for educational purposes only and should not replace professional medical advice
- **Emergency Situations**: The app automatically detects dangerously low vital signs and recommends immediate medical attention
- **Data Privacy**: No personal health data is stored or transmitted

## 🔧 Model Details

- **Algorithm**: Random Forest Classifier
- **Training Data**: Heart disease dataset with 5 key features
- **Model Performance**: Trained on 80% of data, tested on 20%
- **Features Used**: Age, Cholesterol, Heart Rate, BMI, Systolic Blood Pressure

## 🎯 Risk Categories

- **🟢 Low Risk**: Heart attack unlikely based on current parameters
- **🔴 High Risk**: Elevated risk of heart attack - consult healthcare provider
- **⚠️ Emergency**: Dangerously low vital signs detected - seek immediate medical attention

## 📈 Future Enhancements

- [ ] Add more health parameters (diabetes, smoking status, etc.)
- [ ] Implement user accounts and health history tracking
- [ ] Add more detailed health recommendations
- [ ] Mobile app version
- [ ] API endpoints for integration with other health apps

## 📞 Support

If you have any questions or need support, please open an issue in the repository.

---

**Remember**: This application is designed for educational and awareness purposes. Always consult with healthcare professionals for medical decisions and emergency situations. 
