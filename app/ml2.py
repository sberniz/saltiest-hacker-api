import keras
import tensorflow as tf
import pandas as pd
from sklearn.pipeline import Pipeline
from tensorflow import keras
import sklearn
import joblib
model = keras.models.load_model("model.hdf5")
pipeline = joblib.load('sklearn_pipeline.pkl')
model = keras.models.load_model("model.hdf5")
pipeline = joblib.load('sklearn_pipeline.pkl')
def predict_text(text, model = model):
    xtemp = pipeline.transform([text])
    predictions = model.predict(xtemp)
    print(predictions)
    return predictions

print(keras.__version__)
print(sklearn.__version__)
print(tf.__version__)

preds = predict_text("I hate all this all of you")
