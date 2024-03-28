from fastapi import APIRouter,Query
from info.word_input import input
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from methods.model_polarity import prediction,clf
from routers.wordcloud import wordcloud
db_sent=[]
for text in wordcloud:
    prediction_out=int(prediction(text['word_text'],clf))
    output={"text": text['word_text'],"sentiment":prediction_out}
    db_sent.append(output)
router=APIRouter()
@router.get('/db_sentiment')
def read_db_sentiment():
    return db_sent
@router.post('/search_db_sent')
def query_db_sentiment(query:input):
    for file in db_sent:
        if file['text']==query.word_text:
            output=file
            return output
        else:
            prediction_out=int(prediction(query.word_text,clf))
            output={"text": query.word_text,"sentiment":prediction_out}
            return output