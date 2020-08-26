import logging
import random
# import keras
# import tensorflow as tf
# import pandas as pd
# from sklearn.pipeline import Pipeline
# from tensorflow import keras
# import sklearn
import joblib




#Imports 

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

# Load Pickled Module
# model = keras.models.load_model("app/model.hdf5")
# pipeline = joblib.load('app/sklearn_pipeline.pkl')

model = joblib.load('app/tree_reg.pkl')
pipeline = joblib.load('app/sklearn_pipeline_tree.pkl')
####

# def predict_text(text, model = model):
#     xtemp = pipeline.transform([text])
#     predictions = model.predict(xtemp)
#     print(predictions)
#     return predictions
# print(keras.__version__)
# print(sklearn.__version__)
# print(tf.__version__)
# preds = predict_text("I hate all this all of you")


###

class Comment(BaseModel):
    """Use this Data Model to Parse requests for Comments"""
    #timestamp: str = Field(...,example='2020-01-01') # Date or Timestamp. tbd
    #objectid: int = Field(...,example=8409948) # Comment ID
    author: str = Field(...,example='imanaccount247') # User Id/ Author
   # parent_id: int = Field(...,example=8409924)
    comment_text: str = Field(...,example='No it is not. objects make it le')
   # points: int = Field(...,example=2)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    x1: float = Field(..., example=3.14)
    x2: int = Field(..., example=-42)
    x3: str = Field(..., example='banjo')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(comment: Comment):
    """
    Predict Comment Toxicity from Comment. 
    Takes author(username) and comment

    ### Request Body
    - `author`: string
    - `comment`: string

    ### Response
    - `username`: string
    - `comment`: string
    - `saltiness`: float
    """

    X_new = comment.to_df()
    username = comment.author
    saltiness = predict(comment.comment_text)
    comment = comment.comment_text
    log.info(X_new)
    print(X_new)
   # y_pred = random.choice([True, False])
    #y_pred_proba = random.random() / 2 + 0.5
    return {
        'username': username,
        'saltiness': saltiness,
        'comment': comment
    }
def predict(text,model=model):
    xtemp =pipeline.transform([text])
    predictions = model.predict(xtemp)
    print(predictions)
    return predictions[0]
