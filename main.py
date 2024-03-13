from fastapi import FastAPI,Query,Path
from info.word_input import input
from routers.wordcloud import router as wordcloud_router
from routers.wordcloud import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def  api_to_list(db):
    lista_keys=[]
    for file in db:
        lista_keys.append(file['word_text'])
    corpus=dict(zip(lista_keys,map(lambda x: lista_keys.count(x),lista_keys)))
    return corpus
app=FastAPI()
db=wordcloud
db_cloud=api_to_list(db)
print(db_cloud)
wordcloud_corpus = WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(db_cloud)
plt.imshow(wordcloud_corpus, interpolation='bilinear')
plt.axis("off")
plt.show()
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