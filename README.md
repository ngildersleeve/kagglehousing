# 🏡 Kaggle Housing Prices: End-to-End Machine Learning Pipeline on AWS SageMaker

This project implements a **complete production-style ML workflow for the Kaggle House Prices dataset**, using:
- AWS SageMaker for managed infrastructure
- S3 for storage
- XGBoost and Scikit-learn for model building
- SageMaker Batch Transform for production-ready batch predictions

It demonstrates key steps in **moving beyond a notebook** into an **automated, reproducible, and scalable workflow suitable for real-world deployment**.

---

## 📦 Project structure

---

## 🚀 Workflow summary
✅ **Steps performed in this project:**

1️⃣ **Data analysis** (`01-eda.ipynb`):
- Investigated 81 features.
- Visualized missing values and relationships with the target (`SalePrice`).

2️⃣ **Feature engineering & model training** (`02-modeling.ipynb`):
- Created a robust `scikit-learn.Pipeline` handling:
  - Column selection
  - Imputation (MICE/other strategies)
  - One-hot encoding
  - Scaling
- Performed hyperparameter tuning on `XGBoostRegressor` using `GridSearchCV`.
- Achieved:
  - **Train R² ≈ 93%**
  - **Test R² ≈ 83%**

3️⃣ **Model packaging**:
- Saved pipeline as `xgb_pipeline.joblib`.
- Compressed and uploaded to S3 for deployment.

4️⃣ **Production deployment** (`03-deploy.ipynb`):
- Registered model as a **SageMaker model object**.
- Launched a **SageMaker Batch Transform job** for scalable, auditable predictions.
- Post-processed predictions to produce a `result.csv` file with:
  - `Id`
  - `SalePrice`

---

## ☁️ Tech stack:
- **AWS SageMaker**
  - Studio Notebooks
  - Model registration
  - Batch Transform
- **S3** for storage of artifacts, data, and results.
- **Scikit-learn pipelines**
- **XGBoost**
- **Python 3.12 environment**

---

## 🔧 How to reproduce:
### Prerequisites:
- AWS account with SageMaker and S3 access
- (Optional) Quota increase for `ml.m5.large` for Transform Jobs

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
