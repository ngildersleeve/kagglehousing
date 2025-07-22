# 🏡 Kaggle Housing Prices: End-to-End Machine Learning Pipeline on AWS SageMaker

This project implements a **complete production-style ML workflow for the Kaggle House Prices dataset**, using:
- AWS SageMaker for managed infrastructure
- S3 for storage
- XGBoost and Scikit-learn for model building
- SageMaker Batch Transform for production-ready batch predictions

It demonstrates key steps in **moving beyond a notebook** into an **automated, reproducible, and scalable workflow suitable for real-world deployment**.

---

## 📦 Project structure

├── data/
│   ├── train.csv
│   └── test.csv
├── notebooks/
│   ├── 01-eda.ipynb
│   ├── 02-modeling.ipynb
│   └── 03-deploy.ipynb
├── inference/
│   ├── inference.py
│   ├── preprocess.py
│   └── endpoint_name.txt
├── model/
│   └── preprocessor.joblib
├── deploy/
│   └── test_inference.py
└── README.md
---

## 🚀 Workflow summary
✅ **Steps performed in this project:**

1️⃣ **Data analysis** (`01-eda.ipynb`):
- Explored 81 features.
- Visualized missingness and relationships with `SalePrice`.

2️⃣ **Feature engineering & model training** (`02-modeling.ipynb`):
- Created a robust `scikit-learn.Pipeline` for:
  - Column selection
  - Imputation
  - One-hot encoding
  - Scaling

3️⃣ **Model packaging & deployment**:
- Saved the preprocessing pipeline (`preprocessor.joblib`).
- Saved the trained XGBoost model (`model.joblib`).
- Uploaded to S3.
- Deployed as a **SageMaker real-time inference endpoint** for on-demand predictions.

4️⃣ **Production prediction script** (`deploy/test_inference.py`):
- Loads `test.csv`
- Applies **identical preprocessing**
- Sends the data to the live SageMaker endpoint
- Writes predictions to `result.csv` with columns:
  - `Id`
  - `SalePrice`

---

## ☁️ Tech stack:
- **AWS SageMaker**
  - Studio Notebooks
  - Model packaging
  - Real-time inference endpoints
- **S3** for data and artifact storage
- **Scikit-learn pipelines**
- **XGBoost**
- **Python 3.12 environment**

---

## 🔧 How to reproduce:
### Prerequisites:
- AWS account with SageMaker and S3 access
- Python environment with `boto3`, `sagemaker`, `scikit-learn`, `pandas`, `joblib`, etc.

### Steps:
1️⃣ Upload your datasets:
s3://<your-bucket>/train.csv
s3://<your-bucket>/test.csv

2️⃣ Run:
- `notebooks/01-eda.ipynb` for analysis
- `notebooks/02-modeling.ipynb` for training and packaging
- `notebooks/03-deploy.ipynb` for deployment and batch prediction

3️⃣ Result file:

s3://<your-bucket>/results/result.csv


---

## 📸 Optional screenshots:
*(Add screenshots in future.)*

---

## 📝 Notes:
- Dataset from Kaggle House Prices: [https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)


---

## 📄 License:
MIT License — feel free to reference or build on this project structure.

---
