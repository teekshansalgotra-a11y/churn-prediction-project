# Customer Churn Prediction — Telecom

🔗 **[Live Demo — Try it here](https://churn-prediction-project-6b6zbmikstbhmfkptdmexn.streamlit.app/)**

A complete end-to-end machine learning pipeline that predicts customer churn for a telecom company — from raw data to an interactive Streamlit web app. Built with Python, Scikit-learn, and deployed on Streamlit Cloud.

---

## 🎯 Results

| Metric | Baseline Model | Optimized Model |
|---|---|---|
| Accuracy | 78% | 86% |
| Precision | — | High |
| Recall | — | High |
| Model | Logistic Regression | Random Forest + Tuning |

> Improved model accuracy by **8 percentage points** through feature engineering and hyperparameter tuning.

---

## 🚀 Live Demo

👉 **[churn-prediction-project.streamlit.app](https://churn-prediction-project-6b6zbmikstbhmfkptdmexn.streamlit.app/)**

Input customer details and get an instant churn prediction with probability score. No setup required — runs in the browser.

---

## 📌 Project Overview

Customer churn is one of the most expensive problems in telecom — acquiring a new customer costs 5–10x more than retaining one. This project builds a production-ready ML pipeline to:

- Identify customers at high risk of churning
- Understand which factors drive churn most
- Deliver predictions through an interactive web interface

---

## 🔄 Pipeline

```
Raw Data → EDA → Feature Engineering → Model Training → Evaluation → Streamlit App
```

### Phase 1 — Exploratory Data Analysis
- Distribution analysis of all features
- Churn rate breakdown by contract type, tenure, charges
- Correlation heatmap and feature relationships
- Class imbalance analysis

### Phase 2 — Feature Engineering
- Encoding categorical variables
- Handling missing values
- Feature scaling and normalization
- Dropping low-importance features

### Phase 3 — Model Training & Comparison
- Logistic Regression (baseline)
- Random Forest Classifier
- Hyperparameter tuning via GridSearchCV
- Cross-validation for robust evaluation

### Phase 4 — Evaluation
- Confusion matrix analysis
- Precision, Recall, F1-Score
- ROC-AUC curve
- Feature importance visualization

### Phase 5 — Deployment
- Interactive Streamlit web app
- Real-time prediction with probability score
- Clean UI for business users

---

## 💡 Business Recommendations

Based on model insights:

- **Contract type** is the strongest churn predictor — month-to-month customers churn at 3x the rate of annual contract customers
- **Tenure** is highly inversely correlated with churn — target retention efforts at customers under 12 months
- **High monthly charges** with no added services strongly predict churn — bundle offers could reduce risk
- **Tech support and online security** add-ons significantly reduce churn — proactively offer these to at-risk segments

---

## 🛠️ Technologies Used

- **Python 3.x** — Core language
- **Pandas & NumPy** — Data manipulation
- **Scikit-learn** — ML models and evaluation
- **Matplotlib & Seaborn** — Visualizations
- **Streamlit** — Web app deployment
- **Jupyter Notebook** — Experimentation and EDA

---

## 📁 Project Structure

```
churn-prediction-project/
├── data/
│   └── telecom_churn.csv          # Dataset
├── notebooks/
│   └── churn_analysis.ipynb       # Full EDA + modeling notebook
├── visualizations/                # Generated charts and plots
├── models/
│   └── churn_model.pkl            # Saved trained model
├── app.py                         # Streamlit application
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/teekshansalgotra-a11y/churn-prediction-project
cd churn-prediction-project

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 📬 Contact

**Teekshan Salgotra**
- 📧 Email: [teekshansalgotra@gmail.com](mailto:teekshansalgotra@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/teekshan-salgotra-82a182326](https://www.linkedin.com/in/teekshan-salgotra-82a182326/)
- 🐙 GitHub: [teekshansalgotra-a11y](https://github.com/teekshansalgotra-a11y)

---

*B.Tech CSE | VIT Chennai | Open to remote DS/ML internships*
