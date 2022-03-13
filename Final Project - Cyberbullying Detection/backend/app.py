import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import joblib
import re
import string

from mixin import proces_case_folding
from model import get_basic_model

import __main__
__main__.proces_case_folding = proces_case_folding


app = Flask(__name__)

#model filter
with open("model_filter_language.pkl", 'rb') as model_filter:
    model_filter = joblib.load(model_filter)

#model predCB
model = get_basic_model()
#model.built = True
model.load_weights('cp.ckpt')

@app.route('/')
    
def model_predic_get(text):
    #text = request.args.get('text')
    print(text)
    
    list_out = {0 : "This tweet is detected as cyberbullying. It is cyberbullying related to age",
                1 : "This tweet is detected as cyberbullying. It is cyberbullying related to ethnicity",
                2 : "This tweet is detected as cyberbullying. It is cyberbullying related to gender",
                3 : "This tweet is safe!",
                4 : "This tweet is detected as cyberbullying with no specific category.",
                5 : "This tweet is detected as cyberbullying. It is cyberbullying related to religion",
                6 : "Sorry, the text must be in English, we can't recognize your language."}

    out = {'Text' : [text]}
    out = pd.DataFrame(data = out)
        
    model_fil_pred = model_filter.predict(out)
    
    if model_fil_pred != [3]:
        pred = 6
        
    else:
        pred = model.predict(out['Case Folding'])
        pred = np.argmax(pred)


    respons = {'sucess' : 'nice',
                'code' : 200,
                'result_model_filter' : str(model_fil_pred),
                'result_model': str(list_out[pred])}
    return jsonify(respons)


@app.route('/predict', methods = ['POST'])
    
def model_predic():
    #text = request.args.get('text')
    content = request.json
    print(f'{content}\n')
    data = content['Out']
    
    list_out = {0 : "This tweet is detected as cyberbullying. It is cyberbullying related to age",
                1 : "This tweet is detected as cyberbullying. It is cyberbullying related to ethnicity",
                2 : "This tweet is detected as cyberbullying. It is cyberbullying related to gender",
                3 : "This tweet is safe!",
                4 : "This tweet is detected as cyberbullying with no specific category.",
                5 : "This tweet is detected as cyberbullying. It is cyberbullying related to religion",
                6 : "Sorry, the text must be in English, we can't recognize your language."}

    out = {'Text' : [data]}
    out = pd.DataFrame(data = out)
        
    model_fil_pred = model_filter.predict(out)
    
    if model_fil_pred != [3]:
        pred = 6
        
    else:
        pred = model.predict(out['Case Folding'])
        pred = np.argmax(pred)


    respons = {'sucess' : 'nice',
                'code' : 200,
                'result_model_filter' : str(model_fil_pred),
                'result_model': str(list_out[pred])}
        
    return jsonify(respons)