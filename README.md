# Customer Churn Prediction Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

##  Project Overview

A comprehensive end-to-end data science project that predicts customer churn for a telecommunications company using machine learning. This project demonstrates the complete data science workflow from exploratory data analysis to model deployment.

**Project Goal:** Identify customers likely to cancel their service and provide actionable recommendations to reduce churn rate by 20-30%.

---

##  Business Problem

The telecommunications company faces a significant challenge:
- **Current Churn Rate:** 27% of customers leaving annually
- **Business Impact:** Millions in lost revenue
- **Challenge:** Identifying at-risk customers before they leave

**Solution:** Build a predictive model to identify high-risk customers and enable proactive retention strategies.

---

##  Project Structure
```
Churn-Prediction-Project/
│
├── data/
│   ├── raw/
│   │   └── telco_churn.csv              # Original dataset (7,043 customers)
│   └── processed/
│       └── telco_churn_cleaned.csv      # Cleaned and encoded data
│
├── notebooks/
│   ├── 01_EDA.ipynb                     # Exploratory Data Analysis
│   ├── 02_Data_Preprocessing.ipynb      # Data cleaning & preparation
│   └── 03_Model_Building.ipynb          # Machine learning models
│
├── models/
│   ├── logistic_regression_model.pkl    # Baseline model
│   ├── random_forest_model.pkl          # Best performing model
│   └── train_test_data.pkl              # Processed train/test data
│
├── visualizations/
│   ├── Phase 1 (EDA) - 9 charts
│   └── Phase 3 (ML) - 4 charts
│   └── Total: 13 professional visualizations
│
├── reports/
│   ├── EDA_Report.txt                   # Analysis findings
│   ├── Model_Performance_Report.txt     # ML results
│   └── Final_Project_Summary.txt        # Complete summary
│
├── README.md                             # Project documentation (this file)
├── requirements.txt                      # Python dependencies
└── .gitignore                           # Git ignore rules
```

---

##  Dataset Information

**Source:** Kaggle - Telco Customer Churn Dataset

**Dataset Details:**
- **Total Customers:** 7,043
- **Features:** 21 variables
- **Target Variable:** Churn (Yes/No)
- **Churn Rate:** 26.5%

**Key Features:**
- Customer Demographics (gender, age, partner status)
- Services Subscribed (phone, internet, streaming)
- Account Information (contract type, payment method, tenure)
- Billing Details (monthly charges, total charges)

---

## 🔍 Project Phases

### Phase 1: Exploratory Data Analysis 

**Objective:** Understand data patterns and identify key churn drivers

**Activities:**
- Data quality assessment
- Statistical analysis
- Correlation analysis
- Visual exploration
- Pattern identification

**Key Findings:**

1. **Contract Type Impact**
   - Month-to-month: 43% churn rate
   - One year: 11% churn rate
   - Two year: 3% churn rate
   - **Insight:** Month-to-month customers are 14x more likely to churn

2. **Customer Tenure Effect**
   - 0-1 year: 50% churn rate
   - 1-2 years: 35% churn rate
   - 2+ years: 15% churn rate
   - **Insight:** First year is critical retention period

3. **Tech Support Value**
   - Without tech support: 41.6% churn
   - With tech support: 15.2% churn
   - **Insight:** Tech support reduces churn by 2.7x

4. **Pricing Sensitivity**
   - Churned customers: $74.44/month average
   - Retained customers: $61.27/month average
   - **Insight:** Higher-paying customers more likely to leave

5. **Service Quality Issue**
   - Fiber optic: 41.9% churn rate
   - DSL: 18.9% churn rate
   - **Insight:** Fiber optic service quality needs investigation

**Deliverables:**
- 9 professional visualizations
- Comprehensive EDA report
- Business insights document

---

### Phase 2: Data Preprocessing 

**Objective:** Clean and prepare data for machine learning

**Activities:**
- Missing value handling (TotalCharges imputation)
- Categorical encoding (20+ variables converted to numeric)
- Feature/target separation
- Train-test split (80/20 ratio)
- Class balancing using SMOTE technique

**Data Preparation:**
- Original dataset: 7,043 samples
- Training set: 80% (balanced with SMOTE)
- Testing set: 20% (1,409 samples)
- All features converted to numeric format
- No missing values in final dataset

**Deliverables:**
- Cleaned dataset saved
- Train/test data prepared
- Processing pipeline documented

---

### Phase 3: Machine Learning Models 

**Objective:** Build and evaluate predictive models

**Models Trained:**

1. **Logistic Regression** (Baseline)
   - Simple, interpretable model
   - Fast training and prediction
   - Good starting benchmark

2. **Random Forest** (Best Model)
   - Ensemble learning approach
   - Handles non-linear relationships
   - Provides feature importance

**Model Performance:**

| Metric | Logistic Regression | Random Forest |
|--------|---------------------|---------------|
| **Accuracy** | 79% | **82%** |
| **Precision** | 74% | **78%** |
| **Recall** | 80% | **83%** |
| **F1-Score** | 77% | **80%** |
| **ROC-AUC** | 0.82 | **0.85** |

**Winner:** Random Forest 

**Model Interpretation:**
- **83% Recall:** Catches 83 out of 100 customers who will churn
- **78% Precision:** 78% of flagged customers actually churn
- **0.85 ROC-AUC:** Excellent discrimination ability

**Top 5 Predictive Features:**
1. Tenure (customer lifetime)
2. Contract type
3. Total charges
4. Monthly charges
5. Internet service type

**Deliverables:**
- 2 trained models saved
- 4 model evaluation visualizations
- Performance report
- Feature importance analysis

---

## Business Recommendations

Based on data analysis and model predictions:

### 1. Contract Incentive Program
**Action:** Offer 15-20% discount for customers upgrading to annual contracts  
**Target:** Month-to-month customers  
**Expected Impact:** 15-20% churn reduction  
**ROI:** High

### 2. New Customer Welcome Program
**Action:** Implement 6-month enhanced support program  
**Target:** Customers in first year  
**Expected Impact:** 25% reduction in first-year churn  
**Components:**
- Dedicated customer success manager
- Free premium support for 3 months
- Regular check-in calls at 1, 3, 6 months
- Usage optimization guidance

### 3. Premium Service Bundling
**Action:** Create "Protection Plus" bundle (Tech Support + Online Security)  
**Target:** Customers without premium services  
**Expected Impact:** 30% churn reduction among adopters  
**Pricing:** 20% discount vs individual services

### 4. Pricing Strategy Review
**Action:** Implement loyalty pricing for long-term customers  
**Target:** High-value customers (>$70/month)  
**Expected Impact:** Improved satisfaction and retention  
**Options:**
- Loyalty discounts after 2 years
- Value-added services at no extra cost
- Flexible pricing tiers

### 5. Fiber Optic Service Quality Initiative
**Action:** Urgent investigation and improvement of fiber service  
**Target:** All fiber optic customers  
**Expected Impact:** Save 400+ high-value customers annually  
**Steps:**
- Comprehensive service quality audit
- Network performance improvements
- Proactive customer communication

---

## Expected Business Impact

**If All Recommendations Implemented:**

**Current State:**
- Customers lost annually: ~1,900
- Churn rate: 27%

**Projected State (12 months):**
- Churn reduction: 20-30%
- Customers saved: 400-600 annually
- Improved churn rate: 19-21%

**Revenue Impact:**
- Average revenue per customer: ~$900/year
- Annual revenue protected: $360,000 - $540,000

**Additional Benefits:**
- Improved customer lifetime value
- Enhanced brand reputation
- Competitive advantage
- Data-driven decision making

---

## Technologies Used

**Programming Language:**
- Python 3.8+

**Data Analysis & Manipulation:**
- Pandas - Data manipulation and analysis
- NumPy - Numerical computing

**Data Visualization:**
- Matplotlib - Creating static plots
- Seaborn - Statistical data visualization

**Machine Learning:**
- Scikit-learn - ML models and evaluation
- Imbalanced-learn - SMOTE for class balancing

**Development Environment:**
- Jupyter Notebook - Interactive development
- Git/GitHub - Version control

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/teekshansalgotra-a11y/Churn-Prediction-Project.git
cd Churn-Prediction-Project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch Jupyter Notebook
```bash
jupyter notebook
```

### Step 4: Explore the Project
Start with the notebooks in order:
1. `01_EDA.ipynb` - Understand the data
2. `02_Data_Preprocessing.ipynb` - See data cleaning process
3. `03_Model_Building.ipynb` - Review ML models

---

## How to Use This Project

### For Recruiters & Hiring Managers:
1. Review the README for project overview
2. Check visualizations folder for data insights
3. Read reports folder for detailed findings
4. Examine notebooks for code quality

### For Data Science Students:
1. Clone the repository
2. Follow notebooks sequentially
3. Experiment with different models
4. Try improving the results

### For Business Stakeholders:
1. Read the Executive Summary above
2. Review Business Recommendations section
3. Check Expected Business Impact
4. View visualizations for key insights

---

## Skills Demonstrated

### Technical Skills:
✓ Python programming  
✓ Data cleaning and preprocessing  
✓ Exploratory data analysis  
✓ Statistical analysis  
✓ Feature engineering  
✓ Machine learning (classification)  
✓ Model evaluation and selection  
✓ Data visualization  
✓ Version control (Git)  

### Data Science Skills:
✓ End-to-end project execution  
✓ Handling imbalanced datasets  
✓ Model comparison and selection  
✓ Feature importance analysis  
✓ Business insight generation  
✓ Technical documentation  

### Business Skills:
✓ Problem definition  
✓ Stakeholder communication  
✓ Business recommendation development  
✓ ROI analysis  
✓ Strategic thinking  

---

## Project Highlights

**Data Quality:**
- Comprehensive data cleaning pipeline
- Handled missing values systematically
- Proper encoding of 20+ categorical variables

**Analysis Depth:**
- 13 professional visualizations
- Multiple correlation analyses
- Statistical significance testing

**Model Performance:**
- Achieved 82% accuracy
- 83% recall (catches most churners)
- 0.85 ROC-AUC (excellent discrimination)

**Business Value:**
- 5 actionable recommendations
- Quantified revenue impact
- Clear implementation roadmap

---

## Future Enhancements

### Short Term (Optional):
- [ ] Add more advanced models (XGBoost, LightGBM)
- [ ] Implement hyperparameter tuning
- [ ] Create customer risk scoring system
- [ ] Add model explainability (SHAP values)

### Long Term (Advanced):
- [ ] Deploy model as web application (Streamlit)
- [ ] Create REST API for predictions
- [ ] Build interactive dashboard
- [ ] Implement real-time scoring pipeline
- [ ] Add A/B testing framework
- [ ] Create automated retraining system

---

## Sample Visualizations

### Churn by Contract Type
Month-to-month contracts show 43% churn rate compared to just 3% for two-year contracts.

### Feature Importance
Top predictors identified: Tenure, Contract Type, and Monthly Charges.

### ROC Curve
Random Forest model achieves 0.85 AUC, indicating excellent predictive power.

### Confusion Matrix
Model correctly identifies 83% of customers who will churn.

*(Actual images available in the visualizations folder)*

---

## Contributing

While this is primarily a portfolio project, suggestions and feedback are welcome!

**How to Contribute:**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Areas for Contribution:**
- Code optimization
- Additional visualizations
- Alternative modeling approaches
- Documentation improvements

---

## License

This project is licensed under the MIT License - free to use for learning and portfolio purposes.

---

##  Contact

**[Teekshan Salgotra]**

- **Email:** teekshansalgotra@gmail.com
- **LinkedIn:** [linkedin.com/in/teekshan-salgotra](https://www.linkedin.com/in/teekshan-salgotra-82a182326)
- **GitHub:** [github.com/teekshansalgotra-a11y](https://github.com/teekshansalgotra-a11y)

---

## Acknowledgments

**Dataset:**  
Telco Customer Churn Dataset from Kaggle  
[https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**Inspiration:**  
This project was inspired by real-world customer retention challenges faced by telecommunications companies.

**Learning Resources:**
- Scikit-learn documentation
- Kaggle community notebooks
- Data science best practices

---

## Project Status

**Current Status:** Complete and Production-Ready

**Last Updated:** Feburary 2026

**Version:** 1.0

---

## 📊 Project Statistics

- **Lines of Code:** ~1,200+
- **Notebooks:** 3
- **Visualizations:** 13
- **Models Trained:** 2
- **Reports Generated:** 3
- **Development Time:** 15-20 hours
---

## Why This Project Stands Out

**Completeness:** Full end-to-end workflow from raw data to deployment-ready model

**Business Focus:** Strong emphasis on actionable insights and ROI

**Technical Depth:** Proper handling of imbalanced data, multiple models, thorough evaluation

**Documentation:** Comprehensive reports and professional visualization

**Real-World Relevance:** Addresses actual business challenge with measurable impact

---

**# If you find this project helpful, please consider giving it a star! #**

---

**Ready to reduce churn? Let's connect!** 
```


