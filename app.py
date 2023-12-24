import streamlit as st
import pickle
from functions import transform_text

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

st.set_page_config(page_title='Text Message Spam Classifier', layout='wide', initial_sidebar_state='auto')

cv = pickle.load(open('./model_data/vectorizer.pkl', 'rb'))
model = pickle.load(open('./model_data/model.pkl', 'rb'))


st.title("Text Message Spam Classifier")

st.markdown("Not sure if a text you received is spam? This project uses a machine learning model (multinomial Naive "
            "Bayes) to determine whether a given message is or is not spam **with 96% accuracy**")

sms = st.text_input("Enter message")

transformed_sms = transform_text(sms)

vector = cv.transform([transformed_sms])

result = model.predict(vector)[0]

if sms != "":
    if result == 1:
        st.subheader(" Your message was detected as :red[Spam]")
    else:
        st.subheader("Your message was detected as :green[Safe]")

dataset_url = "https://archive.ics.uci.edu/dataset/228/sms+spam+collection"
github_url = "https://github.com/tg1702/detecting-sms-spam"
colab_url = "https://colab.research.google.com/drive/18ZqnOXJ0KCw6PDuNiV1FioJGFyAjsVkG?usp=sharing"
kaggle_url = "https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset"

st.header("Why Spam?")
st.markdown(
    " Many of us are familiar with receiving spam messages via Whatsapp, Instagram or other social media platforms."
    " By training a model on a Kaggle dataset of spam and ham (non-spam) messages, we can detect whether a message is spam or not."
    " Spam messages contain certain frequently-used keywords, helping a program to discern them from normal messages."
    " Here are some of the most common spam keywords:")

st.image("./images/keywords.png")
st.caption("Word cloud showing most common spam words. See %s for more " % colab_url)

st.header("About Project")

st.markdown("Original dataset available at: %s" % dataset_url)
st.markdown("Kaggle .csv file: %s" % kaggle_url)
st.markdown("See all of my code on my Github: %s " % github_url)
st.markdown("Colab file: %s" % colab_url)
