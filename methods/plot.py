from wordcloud import WordCloud
import io
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import spacy
def db_to_db_words(db):
    db_words=[]
    nlp=spacy.blank("es")
    for file in db:
        sentence=file['word_text']
        doc=nlp(sentence)
        words=len(doc)
        if words>1:
            for word in doc:
                new_file={"word_text":word.text}
                db_words.append(new_file)
        elif words==1:
            db_words.append(file)
    return db_words
def  db_count(db_words):
    lista_keys=[]
    for file in db_words:
        lista_keys.append(file['word_text'])
    corpus=dict(zip(lista_keys,map(lambda x: lista_keys.count(x),lista_keys)))
    return corpus
def create_wordcloud_plot(db_cloud):
    wordcloud_corpus = WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(db_cloud)
    plt.imshow(wordcloud_corpus, interpolation='bilinear')
    plt.axis("off")
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    plt.close()
    return img_buf
