import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
import re
import string

from mixin import proces_case_folding
from model import get_basic_model



app = Flask(__name__)

#model filter
with open("model_filter_language.pkl", 'rb') as model_filter:
    model_filter = joblib.load(model_filter)

#model predCB
model = get_basic_model()
#model.built = True
model.load_weights('cp.ckpt')

@app.route('/predict/<string:text>', methods = ['GET'])
    
def model_predic(text):
    #text = request.args.get('text')
    out = {'Text' : [text]}
    out = pd.DataFrame(data = out)
        
    model_fil_pred = model_filter.predict(out)
    
    if model_fil_pred != [3]:
        print('Sorry, this is not english')
    
    else:
        
        pred = model.predict(out['Case Folding'])
        pred = np.argmax(pred)
        
        if(pred == 0):
            print("This tweet is detected as cyberbullying. It is cyberbullying related to age")
        elif(pred==1):
            print("This tweet is detected as cyberbullying. It is cyberbullying related to ethnicity")
        elif(pred==2):
            print("This tweet is detected as cyberbullying. It is cyberbullying related to gender")
        elif(pred==3):
            print("This tweet is safe!")
        elif(pred==4):
            print("This tweet is detected as cyberbullying with no specific category.")
        elif(pred==5):
            print("This tweet is detected as cyberbullying. It is cyberbullying related to religion")
        print(out)
        
    respons = {'sucess' : 'nice',
                'code' : 200,
                'result' : str(model_fil_pred)}
        
    return jsonify(respons)
    
app.run(debug = False)