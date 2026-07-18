# 📰 AG News Text Classification using BERT

A deep learning project that fine-tunes **BERT (bert-base-uncased)** for automatic news article classification using the **AG News** dataset from Hugging Face.

The model predicts one of four news categories:

* 🌍 World
* ⚽ Sports
* 💼 Business
* 🔬 Sci/Tech

---

# Project Overview

This project demonstrates an end-to-end Natural Language Processing (NLP) workflow using the Hugging Face ecosystem.

The project includes:

* Loading and preprocessing the AG News dataset
* Tokenizing text using BERT Tokenizer
* Fine-tuning a pretrained BERT model
* Evaluating the model with multiple metrics
* Visualizing performance using a Confusion Matrix
* Deploying the model with Gradio
* Saving the trained model for future inference

The notebook was developed and trained using **Google Colab GPU**.

---

# Dataset

**Dataset:** AG News

The dataset contains news articles collected from more than 2,000 news sources and is divided into four categories.

| Label | Category |
| ----: | -------- |
|     0 | World    |
|     1 | Sports   |
|     2 | Business |
|     3 | Sci/Tech |

For faster experimentation, this project uses:

* **20,000** training samples
* **5,000** testing samples

---

# Model

**Base Model**

* bert-base-uncased

**Task**

* Multi-class Text Classification

**Framework**

* Hugging Face Transformers

---

# Technologies

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Scikit-learn
* Matplotlib
* Gradio
* Google Colab

---

# Training Configuration

| Parameter     |                        Value |
| ------------- | ---------------------------: |
| Epochs        |                            2 |
| Learning Rate |                         2e-5 |
| Weight Decay  |                         0.01 |
| Batch Size    |                           16 |
| Max Length    |                          256 |
| Optimizer     | AdamW (Transformers Trainer) |

---

# Evaluation

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

Example evaluation workflow:

```
Test Dataset
      │
      ▼
Model Prediction
      │
      ▼
Classification Report
      │
      ▼
Confusion Matrix
```

---

# Model Deployment

A simple Gradio interface is included, allowing users to classify custom news articles interactively.

Example:

**Input**

```
Apple unveiled its newest AI-powered processor for smartphones.
```

**Prediction**

```
Sci/Tech
```

---

# Project Structure

```
AG-News-BERT/
│
├── Project_ag_news_deep_learning.ipynb
├── news_model.pth
├── README.md
├── requirements.txt
└── images/
```

---

# Running the Project

Open the notebook in **Google Colab** or Jupyter Notebook.

Run the cells in order:

1. Install dependencies
2. Load dataset
3. Tokenize text
4. Train BERT
5. Evaluate the model
6. Launch the Gradio interface
7. Save the trained model

---

# Future Improvements

* Train using the complete AG News dataset
* Deploy the model using FastAPI
* Dockerize the application
* Display prediction confidence scores
* Compare BERT with DistilBERT and RoBERTa
* Upload the model to Hugging Face Hub

---

# Author

**Husan Kamolov**

Artificial Intelligence & Machine Learning Enthusiast

Focused on Natural Language Processing, Deep Learning, and Computer Vision.
