# 🎬 SST-2 Sentiment Analysis using DistilBERT

A deep learning project that fine-tunes **DistilBERT (distilbert-base-uncased)** for binary sentiment analysis using the **Stanford Sentiment Treebank v2 (SST-2)** dataset from the GLUE benchmark.

The model predicts whether a movie review expresses:

* 😊 Positive sentiment
* ☹️ Negative sentiment

---

# Project Overview

This project demonstrates an end-to-end Natural Language Processing (NLP) pipeline using Hugging Face Transformers.

The workflow includes:

* Loading the SST-2 dataset
* Text preprocessing and tokenization
* Fine-tuning a pretrained DistilBERT model
* Model evaluation
* Classification Report
* Confusion Matrix visualization
* Interactive inference using Gradio
* Saving the trained model

The project was developed and trained using **Google Colab GPU**.

---

# Dataset

**Dataset:** GLUE - SST-2

The Stanford Sentiment Treebank v2 (SST-2) is one of the most widely used benchmark datasets for binary sentiment classification.

Labels:

| Label | Sentiment |
| ----: | --------- |
|     0 | Negative  |
|     1 | Positive  |

This project uses a subset of the dataset for faster experimentation.

---

# Model

**Base Model**

* distilbert-base-uncased

**Task**

* Binary Sentiment Classification

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

| Parameter     | Value |
| ------------- | ----: |
| Epochs        |     2 |
| Learning Rate |  2e-5 |
| Batch Size    |    16 |
| Weight Decay  |  0.01 |
| Max Length    |   256 |

---

# Evaluation

The trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

---

# Model Deployment

A simple Gradio interface allows users to classify custom movie reviews.

Example:

**Input**

```
This movie was absolutely amazing.
```

Prediction

```
Positive
```

---

# Project Structure

```
SST2-Sentiment-Analysis/

├── sst2_deep_learning_model_project.ipynb
├── README.md
├── requirements.txt
└── images/
```

---

# Running the Project

Run the notebook in Google Colab or Jupyter Notebook.

Steps:

1. Install dependencies
2. Load the SST-2 dataset
3. Tokenize the text
4. Fine-tune DistilBERT
5. Evaluate the model
6. Launch the Gradio interface
7. Save the trained model

---

# Future Improvements

* Train on the complete SST-2 dataset
* Deploy using FastAPI
* Dockerize the application
* Add prediction confidence scores
* Compare DistilBERT with BERT and RoBERTa
* Publish the model on Hugging Face Hub

---

# Author

**Husanjon Kamolov**

Artificial Intelligence & Machine Learning Enthusiast

Interested in NLP, Deep Learning, and Computer Vision.
