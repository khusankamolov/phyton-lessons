# 🏦 Customer Churn Prediction

A complete Machine Learning project for predicting customer churn using multiple classification algorithms.

## 📌 Project Overview

Customer churn prediction helps banks identify customers who are likely to leave the company. This project applies several machine learning classification models and compares their performance.

---
## 📂 Project Structure

```
Customer_Churn_Bank/
│
├── Customer_Churn_Bank.ipynb
├── README.md
├── requirements.txt
│
└── images/
    │
    ├── countplots.png
    ├── histplots.png
    ├── heatmap_corr.png
    ├── Exites_countplot.png
    │
    ├── Decision_tree/
    │   ├── tree_plot.png
    │   ├── tree_conf_mtrx.png
    │   └── tree_roc_curve.png
    │
    ├── Random_forest/
    │   ├── random_conf_mtrx.png
    │   └── random_roc_curve.png
    │
    ├── Logistic_regression/
    │   ├── Logistic_conf_mtrx.png
    │   └── log_roc_curve.png
    │
    ├── KNN/
    │   ├── knn_conf_mtrx.png
    │   └── knn_roc_curve.png
    │
    ├── SVM/
    │   ├── svm_conf_mtrx.png
    │   └── svm_roc_curve.png
    │
    └── XGBoost/
        ├── xgb_conf_mtrx.png
        └── xgb_roc_curve.png
```

---

## 📊 Exploratory Data Analysis

The project includes:

- Missing value checking
- Data type inspection
- Countplots
- Histograms
- Correlation Heatmap
- Target distribution analysis

---

## ⚙️ Data Preprocessing

- Label Encoding
- SMOTE
- Feature Scaling (StandardScaler)
- Train/Test Split

---

## 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

- Decision Tree
- Random Forest
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- XGBoost

---

## 📈 Evaluation Metrics

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

---

## 📊 Model Comparison

| Model | Evaluated |
|--------|-----------|
| Decision Tree | ✅ |
| Random Forest | ✅ |
| Logistic Regression | ✅ |
| K-Nearest Neighbors | ✅ |
| Support Vector Machine | ✅ |
| XGBoost | ⭐ Best Model |

---

## 💡 Business Insights

- Active members are less likely to leave the bank.
- Customers with credit cards generally show better retention.
- Middle-aged customers contribute significantly to churn prediction.
- Customer engagement strategies can reduce churn.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

## 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/khusankamolov/phyton-lessons.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the notebook

```
Customer_Churn_Bank.ipynb
```

---

## 📷 Sample Visualizations

The `images/` folder contains:

- EDA plots
- Correlation heatmap
- Confusion matrices
- ROC curves for each model

---

## 📄 Dataset

Customer Churn Dataset

Target variable:

- **Exited**
    - 0 → Customer stayed
    - 1 → Customer left

---

## 👤 Author

Husanjon Kamolov
