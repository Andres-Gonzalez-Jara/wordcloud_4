from fastapi import FastAPI,Query,Path,Response,BackgroundTasks
import uvicorn
from info.word_input import input
from routers.wordcloud import router as wordcloud_router
from routers.wordcloud import wordcloud
from methods.plot import db_to_db_words,db_count,create_wordcloud_plot
app=FastAPI()
db=db_to_db_words(wordcloud)
db_cloud=db_count(db)
@app.get('/')
async def wordcloud_img(background_tasks: BackgroundTasks):
    img_buf = create_wordcloud_plot(db_cloud)
    bufContents: bytes = img_buf.getvalue()
    background_tasks.add_task(img_buf.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(bufContents, headers=headers, media_type='image/png')
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
if __name__ == "__main__":
    uvicorn.run(app)