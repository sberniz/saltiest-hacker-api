from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from os import getenv

from app.api import predict, viz, salty

app = FastAPI(
    title='Saltiest Hacker API',
    description='Predicts the Saltiest comment on Hacker News Depending on the Text of the Comment',
    version='0.1',
    docs_url='/',
)
#app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.include_router(predict.router)
app.include_router(salty.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
