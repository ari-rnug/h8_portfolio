from sklearn.base import BaseEstimator, TransformerMixin
import re
import string

class proces_case_folding(BaseEstimator, TransformerMixin):
    
    def __init__(self, create = True):
        self.create = create
        
    def fit(self, X, y=None):
        return self
    
    def process(self, X):
        text = X.lower()
        text = re.sub(f'\d','', text)
        text = text.translate(str.maketrans(" "," ", string.punctuation))
        text = text.strip()
        return text
    
    def transform(self, X):
        X['Case Folding'] = X['Text'].apply(self.process)
        return X['Case Folding']