from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from src.model.model import my_model
from src.logger import logging

logging.info("server Started")

app = FastAPI()

# Allow requests from Chrome extension (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing, allow all
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)
#loading modal
logging.info('Loading Model')
model=my_model()

logging.info('Model Loaded successfully')
# Define request body
class CommentRequest(BaseModel):
    comments: List[str]

logging.info('starting server')
# POST endpoint for /preprocess
@app.post("/preprocess")
def preprocess(data: CommentRequest):
  
    comments = data.comments
    logging.info('Entered preprocessing')
    result=model.return_sentiment_count(comments)

    return result
