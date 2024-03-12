from fastapi import APIRouter
router=APIRouter()
wordcloud=[]
default_wordcloud=[
    {
    "word_text" :"hola"
    },
    {
    "word_text":"hola"
    },
    {
    "word_text":"perro"
    }]
def create_wordcloud():
    pass
create=False
if create==True:
    wordcloud=create_wordcloud()
else:
    wordcloud=default_wordcloud
@router.get('/wordcloud')
def read_db():
    return wordcloud
