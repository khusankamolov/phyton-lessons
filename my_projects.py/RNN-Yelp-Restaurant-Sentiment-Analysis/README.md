# 🍽️ Yelp Restaurant Sentiment Analysis using RNN (PyTorch)

A deep learning project for binary sentiment classification of Yelp restaurant reviews using a Recurrent Neural Network (RNN) implemented with PyTorch.

The model predicts whether a restaurant review expresses **positive** or **negative** sentiment.

---

## Project Overview

This project demonstrates the complete NLP pipeline from raw text preprocessing to training a neural network for sentiment classification.

The workflow includes:

- Text preprocessing
- Vocabulary construction
- Tokenization
- Numerical encoding
- Custom PyTorch Dataset
- DataLoader
- RNN-based sentiment classifier
- Model evaluation
- Inference on custom reviews

---

## Dataset

Dataset: **Yelp Restaurant Reviews**

### Preprocessing

- Removed unnecessary columns
- Removed neutral reviews (Rating = 3)
- Converted ratings into binary labels

| Rating | Label |
|---------|-------|
| 1,2 | Negative |
| 4,5 | Positive |

To balance the dataset:

- 750 positive reviews
- 750 negative reviews

Total samples:

```
1500
```

---

## NLP Pipeline

### Text Processing

- Lowercase conversion
- Whitespace tokenization

### Vocabulary

Vocabulary built using

```
collections.Counter
```

Top **5000** most frequent words were kept.

Special tokens

| Token | Index |
|---------|------|
| PAD | 0 |
| UNK | 1 |

---

## Model Architecture

```
Input Text
      │
Embedding Layer
      │
Simple RNN
      │
Last Hidden State
      │
Linear Layer
      │
Sigmoid
      │
Positive / Negative
```

Architecture

- Embedding Layer
- Simple RNN
- Fully Connected Layer
- Sigmoid Activation

Loss Function

```
BCELoss
```

Optimizer

```
Adam
```

---

## Technologies

- Python
- PyTorch
- Pandas
- NumPy

---

## Project Structure

```
RNN-Yelp-Restaurant-Sentiment-Analysis/
│
├── README.md
├── requirements.txt
├── RNN_Project_yelp_restaurant.ipynb
└── Yelp_Restaurant_Reviews.csv
```

---

## Training

Example

```python
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

Training is performed for multiple epochs using PyTorch DataLoader.

---

## Prediction

Example

```python
predict("The food was amazing and the staff were very friendly.")

predict("I will never come back. The service was terrible.")
```

---

## Results

The trained model successfully classifies restaurant reviews into:

- Positive
- Negative

using a simple RNN architecture.

---

## Future Improvements

- LSTM
- GRU
- Bidirectional RNN
- Pretrained Word Embeddings (GloVe / FastText)
- BERT Fine-tuning
- Hyperparameter Optimization
- Attention Mechanism

---

## Author

Husanjon Kamolov

GitHub:
https://github.com/khusankamolov