from fastapi import FastAPI,Query,Path
from info.word_input import input
from routers.wordcloud import router as wordcloud_router
from routers.wordcloud import wordcloud
app=FastAPI()
db=wordcloud
app.include_router(wordcloud_router)
@app.post('/search')
def count(query:input):
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