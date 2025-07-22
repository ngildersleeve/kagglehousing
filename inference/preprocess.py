# preprocess.py
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Identify column types

from sklearn.preprocessing import FunctionTransformer

categorical_cols = ['BsmtQual']
numerical_cols = ['OverallQual', 'GarageCars', 'GrLivArea']
all_features = numerical_cols + categorical_cols

def select_features(X):
    return X[all_features]

feature_selector = FunctionTransformer(select_features)
# Pipelines
numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='NA')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Full transformer
preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numerical_cols),
    ('cat', categorical_pipeline, categorical_cols)
])