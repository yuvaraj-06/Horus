from flask import Flask, render_template, Response
from camera import VideoCamera
import json
import nltk
nltk.download("stopwords")
nltk.download('punkt')
from math import log
from nltk.tokenize import sent_tokenize
# from nltk.tokenize import PunktWordTokenizer
# tokenizer=PunktWordTokenizer()
from nltk.tokenize import WordPunctTokenizer   
tokenizer = WordPunctTokenizer() 
from nltk.corpus import stopwords
from itertools import islice
import collections

from collections import Counter
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from connect_database import Database
import nltk
nltk.download("stopwords")
nltk.download('punkt')
from math import log
from nltk.tokenize import sent_tokenize
# from nltk.tokenize import PunktWordTokenizer
# tokenizer=PunktWordTokenizer()
from nltk.tokenize import WordPunctTokenizer   
tokenizer = WordPunctTokenizer() 
from nltk.corpus import stopwords
from itertools import islice
import collections
db=Database()
with open('interview1.json') as file:
    data = json.load(file)

from sklearn.preprocessing import LabelEncoder

training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])


enc = LabelEncoder()
enc.fit(training_labels)
training_labels = enc.transform(training_labels)


vocab_size = 10000
embedding_dim = 16
max_len = 20
trunc_type = 'post'
oov_token = "<OOV>"
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, truncating=trunc_type, maxlen=max_len)


classes = len(labels)


model = tf.keras.models.Sequential()
model.add(keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(classes, activation='softmax'))
training_labels_final = np.array(training_labels)
EPOCHS = 500
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(padded, training_labels_final, epochs=EPOCHS)
 
app = Flask(__name__)

CORS(app)
@app.route('/')
def index():
    return render_template('index.js')

@app.route('/login/<name>/<passw>')
def login(name,passw):
     ans=db.show("employee_table")
     for i in ans:
         if i["name"]==name:
             if i["password"]==passw:
                 return i["id"]
@app.route('/hr')
def hr():
     di=dict()

     ans=db.show("employee_table")
     for i in ans:
         di[i["id"]]=i
   #  print(tuple(ans))
     return di
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/res/<id>', methods = ["GET"])
def res(id):
  #  print(id,"ssssssssssssss")
    col=["id","prod_score","emotion_score","mentalhealth_score"]
    s=' ("id","prod_score","emotion_score","mentalhealth_score") '
    with open('sav.json') as json_file:
            data = json.load(json_file)
            try:
                sc=dict(Counter(data["emo"]))["sad"]
            except:
                sc=0
            db.insert("employee_table",s,col,[str(id),str(data["out"]),str(dict(Counter(data["emo"]))),str(sc)])
            db.show("employee_table")
            return data
@app.route("/<inp>", methods = ["GET"])
@cross_origin()
def output(inp):
    string = inp
    kk=inp.split()
    print(kk)
    if "zoom" in kk:

        import jwt
        import requests
        
        from time import time
        import sys
        
        import requests
        import authlib
        import os
        import urllib.request 
        from pathlib import Path
        from typing import Optional, Dict, Union, Any
        from authlib.jose import jwt
        from requests import Response
        import http.client
        import json
        API_SEC= 'huOp7UmoZULenoebGtD6xTnvJp8OwsHk6gUn'
        API_KEY = 'pc4mHiLdQnSb7MKrz3pj7A'

        def generateToken():
            api_key = API_KEY
            api_secret = API_SEC
            jwt_token_exp = 518400
            jwt_token_algo = "HS256"


            iat = int(time())

            jwt_payload: Dict[str, Any] = {
                "aud": None,
                "iss": api_key,
                "exp": iat + jwt_token_exp,
                "iat": iat
            }

            header: Dict[str, str] = {"alg": jwt_token_algo}

            jwt_token: bytes = jwt.encode(header, jwt_payload, api_secret)

            return  jwt_token.decode('UTF-8') 

        meetingdetails = {"topic": "Stand Up Call",
                       "type": 2,
				"start_time": "2019-06-14T10: 21: 57",
				"duration": "45",
				"timezone": "Europe/Madrid",
				"agenda": "test",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": "true",
							"participant_video": "true",
							"join_before_host": "False",
							"mute_upon_entry": "False",
							"watermark": "true",
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}


        def createMeeting():
            headers = {'authorization': 'Bearer ' + generateToken(),
                    'content-type': 'application/json'}
            r = requests.post(
                f'https://api.zoom.us/v2/users/me/meetings',
                headers=headers, data=json.dumps(meetingdetails))

            print("\n creating zoom meeting ... \n")
            y = json.loads(r.text)
            join_URL = y["join_url"]
            meetingPassword = y["password"]

            print(
                f'\n here is your zoom meeting link {join_URL} and your \
                password: "{meetingPassword}"\n')
            ss="here is your zoom meeting link "+ str(join_URL) + "and your password: "+str(meetingPassword)
            return {"link": str(join_URL),"pass":str(meetingPassword)}
        asa=createMeeting()
        print(asa)
        return asa
    else:

        result = model.predict(pad_sequences(tokenizer.texts_to_sequences([string]),
                                                        truncating=trunc_type, maxlen=max_len))
        category = enc.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag']==category:
                return np.random.choice(i['responses'])
@app.route("/summary/<inpu>", methods = ["GET"])
@cross_origin()
def summary(inpu):
    
    vocab=[]

    def get_count(text):
        counts={}

        for word in text:
            word=word.lower()
            # print(counts)
            if word in counts:
                counts[word]+=1
                continue
            counts[word]=1
            if word not in vocab:
                vocab.append(word)
        return counts

    def get_doc_freq(sentences):
        # vocab_doc_counts
        for_df={}

        for word in vocab:
            for line in sentences:
                if word in line and word in for_df:
                    for_df[word]+=1
                else:
                    for_df[word]=1
        return for_df

    def score_sentences(sentences,tfidf_values):
        tfidf_scores_sentences={}
        # print(tfidf_values)
        tokenizer = WordPunctTokenizer() 
        for line in sentences:
            tfidf_scores_sentences[line]=0.0
            tokens=tokenizer.tokenize(line)
            for word in tokens:
                word=word.lower()
                if word not in tfidf_values:
                    continue
                tfidf_scores_sentences[line] += tfidf_values[word]
        return tfidf_scores_sentences

    def rank_sentences(score_dict):
        s=sorted(score_dict.items(), key=lambda pair: pair[1],reverse=True)
        sorted_dict = collections.OrderedDict(s)
        return sorted_dict

    def get_summary(paragraph,limit=10):
        # sentences=sent_tokenize(paragraph)
        sentences=paragraph.split(".")
        no_sentences=len(sentences)

        tfidf_scores_sentence={}
        tfidf_values={}
        # sents=[]

        from nltk.tokenize import sent_tokenize
        # from nltk.tokenize import PunktWordTokenizer
        # tokenizer=PunktWordTokenizer()
        from nltk.tokenize import WordPunctTokenizer   
        tokenizer = WordPunctTokenizer() 
        from nltk.corpus import stopwords
        from itertools import islice
        import collections
        for line in sentences:
            string=""
            tokens=tokenizer.tokenize(line)
            len_sentence=len(tokens)
            tokens=[word.lower() for word in tokens]
            filtered_tokens=[word for word in tokens if word not in stopwords.words('english')]
            counts=get_count(filtered_tokens)
            df=get_doc_freq(filtered_tokens)
    
            for word in filtered_tokens:
                # string+=" "+word
                tf = counts[word]/len_sentence
                idf = log(  (1+no_sentences) / (1 + df[word])    )
                tfidf_values[word] = tf*idf

            # sents.append(string)
        score_dict = score_sentences(sentences,tfidf_values)
        # print(score_dict)
        ranked_sents = rank_sentences(score_dict)  
        # print(no_sentences)
        # print(len(ranked_sents))


        return dict(islice(ranked_sents.items(),limit))

    a=inpu
    tfidf_dict = get_summary(a,limit=2)
    summary=""
    for key in tfidf_dict:
        summary+=""+key
    print(summary)
    # Import the required module for text
# to speech conversion
    from gtts import gTTS

    # This module is imported so that we can
    # play the converted audio
    import os

    # The text that you want to convert to audio
    mytext = summary
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("au.mp3")

    # Playing the converted file
    os.system("au.mp3")
    return {"summary":summary,"audio":"au.mp3"}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)
