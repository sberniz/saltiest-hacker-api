import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

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
    - `x3`: string

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
def predict(comment):
    y_pred = random.random() / 2 + 0.5
    return y_pred
