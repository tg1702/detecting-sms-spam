# detecting-sms-spam

## Description
This project is a web app that uses a Multinomial Naive Bayes model to detect SMS/text message spam. A dataset of spam and ham (non-spam) messages was obtained from Kaggle. The model was created and trained using Google Colab and downloaded and saved into the <code>model.pkl</code> file. A web app was built using the Streamlit library in Python in order to send data to the model.

## Run on web
Hosted on the Streamlit Community Cloud service at https://detecting-sms-spam.streamlit.app/. 
You can enter the message you would like to check in the available input box.

## Install and Run locally
1. Clone the repo using <code>git clone</code>
2. Make sure the following libraries are installed in your Python venv. These are located in the requirements.txt file and can be installed using<br>
   <code>!pip install -r requirements.txt </code>
4. Once the libraries are installed, run the command <code>streamlit run app.py</code> to view the streamlit app
   
## About Project

Original dataset available at: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

Tutorial referenced for model training: https://www.youtube.com/watch?v=YncZ0WwxyzU

Kaggle .csv file: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

My Colab file: https://colab.research.google.com/drive/18ZqnOXJ0KCw6PDuNiV1FioJGFyAjsVkG?usp=sharing


