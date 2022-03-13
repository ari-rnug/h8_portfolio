import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, GRU, Dropout
from tensorflow.keras.layers import TextVectorization
import pickle




max_vocab_length = 30000 #untuk membatasi vocabnya sampai brp
max_length = 30 #maksimal kata dalam satu kalimat
shuffler = 5
batch_size = 32
text_vectorization = TextVectorization(max_tokens=max_vocab_length, #seberapa banyak token atau vocab
                                       standardize="lower_and_strip_punctuation", #auto menghilangkan tanda baca atau mengecilkan kata
                                       split="whitespace", #split berdasarkan spasi/jeda
                                       ngrams=None, #berapa kata yg ingin dijadikan vocab.
                                       output_mode='int',
                                       output_sequence_length=max_length)

embedding = Embedding(input_dim=max_vocab_length, #batas kata untuk input (4000 tadi seperti di atas)
                      output_dim=max_length, #angka boleh berapapun
                      #embeddings_initializer="uniform",
                      input_length=max_length)

from_disk = pickle.load(open("tv_layer.pkl", "rb"))
text_vectorization = TextVectorization.from_config(from_disk['config'])
# You have to call `adapt` with some dummy data (BUG in Keras)
text_vectorization.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
text_vectorization.set_weights(from_disk['weights'])
#print(text_vectorization("dumb"))
# Membuat rancangan model untuk versi sequential API.
def get_basic_model():
    #text_vectorization.adapt(tf.data.Dataset.from_tensor_slices(pd.Series(["xyz"])))
    model = Sequential([
        text_vectorization,
        embedding,
        LSTM(128),
  #      Dropout(0.2),
 #       Dense(32, activation='relu'),
        Dense(6, activation='softmax')
])

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
    return model


