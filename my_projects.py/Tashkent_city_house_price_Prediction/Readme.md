# 🏠 Tashkent House Price Prediction

This project predicts house prices in Tashkent using Machine Learning models.

---

## 📊 Problem

We aim to predict real estate prices based on:
- size
- rooms
- floor level
- building levels
- engineered features

---

## ⚙️ Approach

- Data cleaning and preprocessing
- Feature engineering (e.g. size_per_room)
- Encoding categorical variables
- Random Forest Regressor model
- Feature importance analysis

---

## 🚫 Important Insight (Location Feature)

We tested location feature using:
- OneHotEncoding
- Target Encoding

However, it was removed because:
- Too many unique values (high cardinality)
- Sparse data per category
- RMSE increased (model performance got worse)

---

## 📈 Results

| Model | RMSE |
|------|------|
| Without Location | ~17,000 |
| With Target Encoding | ~19,000 ❌ |

---

## 🧠 Important Features

- size
- rooms
- size_per_room
- max_levels
- level

---

## 👨‍💻 Author

Husanjon Kamolov