#Library
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
df_train=pd.read_csv('C:/Users/56975/Desktop/chat-inspector/proces/testing_data/data_sklearn/train_dataset_preproces.csv')
def create_data_train(dataframe,columna_mensaje,columna_label):
    df = pd.DataFrame({
    'Sentiment': dataframe[columna_label],
    'Phrase':dataframe[columna_mensaje]
    })
    train=df
    train_y = train.iloc[:,0]
    train_X = train.iloc[:,1]
    return train_y,train_X
def entrenar_TF_IDF(train_X,train_y):
    vec = TfidfVectorizer(min_df=3)
    model = MultinomialNB()
    clf = make_pipeline(vec,model)
    clf = clf.fit(train_X, train_y)
    return clf
#Data train
train_y,train_X=create_data_train(df_train,'preprocess_message','Label')
#Train model
clf=entrenar_TF_IDF(train_X,train_y)
def prediction(text,clf):
        array=[text]
        predic_test=clf.predict(array)
        return predic_test[0]