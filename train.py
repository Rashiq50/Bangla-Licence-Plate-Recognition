import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
import pickle
import tensorflow as tf

DATADIR = "Dataset"
CATEGORIES = ["0", "1"]

train_data = []

for ct in CATEGORIES:
    path = os.path.join(DATADIR,ct)  # Dataset // 1 folder
    print(path)
    class_num = CATEGORIES.index(ct)
    print(class_num)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path, img))
        train_data.append([img_array, class_num])

random.shuffle(train_data)

for i in train_data:
    print(i[1])

X = []
Y = []

for feature, labels in train_data:
    X.append(feature)
    Y.append(labels)

X = np.array(X).reshape(-1, 100, 90, 1)

pickle_out = open("X.pickle", "wb")
pickle_dump = (X, pickle_out)
pickle_out.close()

pickle_out = open("Y.pickle", "wb")
pickle_dump = (Y, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)
