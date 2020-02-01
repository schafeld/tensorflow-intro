import tensorflow as tf
from tensorflow import keras
import numpy as np
# I had numpy 1.16.3, tutorial needed specific version:
# pip install numpy==1.16.1

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000) # use only 10000 most used words

# Debugging output
# print(train_labels[0]) # print single label number
# print(train_data[0]) # print array of integers representing words in actual text

word_index = data.get_word_index()

word_index = {key:(value + 3) for key, value in word_index.items()} # +3 to provide space for special keys in dictionary, see below
word_index["<PAD>"] = 0 # padding to equalize text lengths
word_index["<START>"] = 1
word_index["<UNK>"] = 2 # unknown
word_index["<UNUSED"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()]) # reverse key value order

def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

print(decode_review(test_data[1]))