# 🏥 Obesity Level Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict an individual's **obesity level** based on their **physical attributes and lifestyle habits** using Machine Learning techniques.

The model analyzes factors such as **age, height, weight, physical activity, eating habits, and family history** to classify individuals into different obesity categories.

---

## 🎯 Problem Statement

The goal of this project is to build a **multi-class classification model** that predicts a person's **obesity level (`NObeyesdad`)** using lifestyle and health-related features.

---

## 📊 Dataset Information

* Total Records: **2111**
* Features: **17**
* After preprocessing: **2087 records**

### Target Variable:

* `NObeyesdad`

### Classes:

* Insufficient_Weight
* Normal_Weight
* Overweight_Level_I
* Overweight_Level_II
* Obesity_Type_I
* Obesity_Type_II
* Obesity_Type_III

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Streamlit (for deployment)
* Joblib

---

## 🔍 Exploratory Data Analysis (EDA)

Performed various visualizations to understand data patterns:

* Distribution of obesity levels
* Age, Height, Weight distributions
* Correlation heatmap
* Lifestyle factors vs obesity
* Feature importance analysis

---

## 🧹 Data Preprocessing

* Removed duplicate values
* Handled outliers using IQR method
* Converted categorical columns
* Encoded categorical variables
* Feature selection (reduced from 16 → 6 features)

---

## 🧠 Feature Selection

Final features used in the model:

* Age
* Height
* Weight
* Family History with Overweight
* Physical Activity Frequency (FAF)
* Frequent High-Calorie Food Consumption (FAVC)

---

## 🤖 Models Used

* Logistic Regression
* Decision Tree
* Random Forest ⭐

---

## 📈 Model Performance

| Model               | Accuracy  | Precision | Recall    | F1 Score  |
| ------------------- | --------- | --------- | --------- | --------- |
| Logistic Regression | 76%       | 76%       | 76%       | 75%       |
| Decision Tree       | 94%       | 94%       | 94%       | 94%       |
| Random Forest       | **94.5%** | **94.6%** | **94.5%** | **94.5%** |

✅ **Best Model: Random Forest**

---

## ⚡ Hyperparameter Tuning

Performed tuning using **GridSearchCV**.

**Best Parameters:**

* n_estimators = 300
* max_depth = None
* min_samples_split = 2

---

## 💡 Key Insights

* Weight is the most important factor influencing obesity
* Physical activity significantly reduces obesity risk
* High-calorie food consumption increases obesity levels
* Family history plays a crucial role

---

## 🚀 Streamlit Application

A user-friendly web application was developed using Streamlit.

### Features:

* Input only **6 fields**
* Real-time prediction
* BMI calculation
* Clean and interactive UI

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/obesity-prediction.git
cd obesity-prediction
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Streamlit app

```
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py
├── obesity_rf_model.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
```

---

## 📦 Model Deployment

* Model saved using **Joblib**
* Integrated into Streamlit app for real-time predictions

---

## 📌 Future Improvements

* Add more features like diet details
* Use advanced models like XGBoost
* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Add user authentication

---


## ⭐ Acknowledgements

This project was built as part of **Machine Learning practice and portfolio development**.

---

## 📢 Conclusion

This project demonstrates a complete **end-to-end machine learning workflow**, including:

* Data preprocessing
* Feature engineering
* Model training & evaluation
* Hyperparameter tuning
* Deployment using Streamlit

The final model achieves **~94.5% accuracy** with reduced input features, making it efficient and suitable for real-world applications.

---
