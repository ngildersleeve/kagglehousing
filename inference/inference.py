# inference.py
import joblib
import pandas as pd
import os

def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "xgb_pipeline.joblib"))
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "text/csv":
        return pd.read_csv(pd.compat.StringIO(request_body))
    else:
        raise ValueError("Unsupported content type: {}".format(request_content_type))

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    return ",".join(str(x) for x in prediction)