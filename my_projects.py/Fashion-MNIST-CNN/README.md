# 👕 Fashion-MNIST Image Classification using CNN (PyTorch)

A deep learning project that classifies grayscale clothing images from the Fashion-MNIST dataset using a Convolutional Neural Network (CNN) implemented with PyTorch.

## 📌 Project Overview

This project demonstrates how to build, train, and evaluate a CNN for image classification. The model learns to recognize 10 categories of clothing items from the Fashion-MNIST dataset.

The project covers:

- Image preprocessing
- CNN architecture design
- Model training
- Performance evaluation
- GPU support (CUDA)

---

## 📂 Dataset

**Fashion-MNIST**

- 70,000 grayscale images
- Image size: **28×28**
- 10 clothing categories

Classes:

| Label | Category |
|--------|----------|
|0|T-shirt/Top|
|1|Trouser|
|2|Pullover|
|3|Dress|
|4|Coat|
|5|Sandal|
|6|Shirt|
|7|Sneaker|
|8|Bag|
|9|Ankle Boot|

The dataset is downloaded automatically through `torchvision.datasets.FashionMNIST`.

---

## 🧠 Model Architecture

```
Input (1×28×28)

↓

Conv2D (1 → 8, kernel=3)
ReLU
MaxPool

↓

Conv2D (8 → 16, kernel=3)
ReLU
MaxPool

↓

Flatten

↓

Linear (16×7×7 → 128)
ReLU

↓

Linear (128 → 10)
```

---

## ⚙️ Training Configuration

| Parameter | Value |
|------------|-------|
|Framework|PyTorch|
|Epochs|5|
|Batch Size|32|
|Optimizer|Adam|
|Learning Rate|0.002|
|Loss Function|CrossEntropyLoss|

---

## 📊 Evaluation

After training, the notebook evaluates the model on the Fashion-MNIST test set and reports the classification accuracy.

---

## 🛠 Technologies

- Python
- PyTorch
- Torchvision
- Google Colab
---

## 📁 Project Structure

```
Fashion-MNIST-CNN/
│
├── Fashion_MNIST_main.ipynb
├── requirements.txt
├── README.md
└── data/
```

---

## 📜 License

This project is intended for educational and learning purposes.

---

## Author

Husanjon Kamolov