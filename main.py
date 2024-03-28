from fastapi import FastAPI,Query,Path,Response
import uvicorn
from info.word_input import input
from routers.wordcloud import router as wordcloud_router
from routers.wordcloud import wordcloud
from routers.sentiment_polarity import router as sent_router
from methods.plot import db_to_db_words,db_count
app=FastAPI()
db=db_to_db_words(wordcloud)
db_cloud=db_count(db)
@app.get('/')
def wordcloud_db():
    return db_cloud
app.include_router(wordcloud_router)
app.include_router(sent_router)
@app.post('/search')
def search_word_frecuency(query:input):
    count=0
    for file in db:
        if file['word_text']==query.word_text:
            count+=1
    output=[
        {
            'word':query.word_text,
            'count': count
        }
    ]
    return output
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)