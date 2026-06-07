# 📚 Student Performance Prediction

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic and academic factors.

The project demonstrates the complete ML lifecycle including data ingestion, data transformation, model training, model selection, prediction pipeline creation, and deployment using Streamlit.

---

## 🚀 Live Demo

🔗 https://student-math-score-predictor.streamlit.app

---

## 📌 Problem Statement

Student performance is influenced by multiple factors such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

This project aims to predict a student's **Math Score** using these features.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Machine Learning
- Scikit-Learn
- CatBoost

### Model Selection
- GridSearchCV

### Deployment
- Streamlit

### Version Control
- Git
- GitHub

---

## 📊 Project Workflow

```text
Data Collection
      ↓
Data Ingestion
      ↓
Data Transformation
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Serialization
      ↓
Prediction Pipeline
      ↓
Streamlit Deployment
```

---

## 📂 Project Structure

```text
STUDENT_PERFORMANCE/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
│
├── notebook/
│   ├── 1. EDA.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🤖 Models Evaluated

The following regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- CatBoost Regressor

The best-performing model was selected using GridSearchCV.

---

## ✨ Features

- End-to-End ML Pipeline
- Data Ingestion Pipeline
- Data Transformation Pipeline
- Hyperparameter Tuning
- Model Serialization
- Custom Exception Handling
- Logging Support
- Prediction Pipeline
- Interactive Streamlit Web App
- Cloud Deployment

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/AsmitaKabra/Student_Performance-.git
```

### Move to Project Directory

```bash
cd Student_Performance-
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Sample Prediction

### Input

| Feature | Value |
|----------|--------|
| Gender | Female |
| Race/Ethnicity | Group C |
| Parent Education | Master's Degree |
| Lunch | Standard |
| Test Preparation | Completed |
| Reading Score | 95 |
| Writing Score | 96 |

### Output

```text
Predicted Math Score: 95.21
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building production-style ML pipelines
- Data preprocessing and feature engineering
- Model selection and evaluation
- Hyperparameter tuning
- Model deployment using Streamlit
- Version control using Git and GitHub

---

## 👩‍💻 Author

### Asmita Kabra

Data Science & Machine Learning Enthusiast

🔗 GitHub: https://github.com/AsmitaKabra

🔗 LinkedIn: https://www.linkedin.com/in/asmita-kabra-1a6298342/

---

## ⭐ If you found this project useful, consider giving it a star!
