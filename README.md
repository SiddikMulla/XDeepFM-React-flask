# XDeepFM Product Recommendation System

A product recommendation engine built on the **eXtreme Deep Factorization Machine (XDeepFM)** algorithm, served via a Flask API and visualized in a React-based Amazon clone frontend.

---

## 🧠 What is XDeepFM?

XDeepFM combines a **Compressed Interaction Network (CIN)** with a standard deep neural network to model both explicit and implicit high-order feature interactions — making it highly effective for recommendation tasks compared to traditional collaborative filtering.

**Dataset:** Amazon product reviews (ratings matrix)

## ✨ Features

- XDeepFM model trained on Amazon reviews interaction matrix
- Flask REST API serving personalized product recommendations
- React Amazon-clone UI consuming the API via Axios
- Jupyter notebooks with full model training pipeline

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML Model | XDeepFM (PyTorch/TensorFlow) |
| Backend | Flask (Python) |
| Frontend | React.js |
| Data | Amazon Reviews Dataset |
| Notebooks | Jupyter (Google Colab) |

## 🚀 Getting Started

### Backend

```bash
cd server
pip install -r requirements.txt
python3 app.py
```

### Frontend

```bash
cd Amazon-Clone/client
npm install
npm start
```

Login using credentials stored in the Flask user dictionary.

## 📓 Notebooks

| File | Description |
|---|---|
| `amazon_reviews.ipynb` | Data exploration & preprocessing |
| `amazon_ratings_T4_linear.ipynb` | XDeepFM model training (T4 GPU) |

## 📄 License

MIT
