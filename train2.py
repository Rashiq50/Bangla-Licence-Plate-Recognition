from PIL import Image
import os
import numpy as np
import re
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout, Flatten, Dense


def get_data(path):
    all_images_as_array = []
    label = []
    i = 0
    for filename in os.listdir(path):

        if re.match(r'1', filename):
            label.append(1)
        else:
            label.append(0)
        img = Image.open(path + filename)
        # ig = cv2.imread(path+filename)
        np_array = np.asarray(img)
        l, b = np_array.shape
        np_array = np_array.reshape(l * b, )
        all_images_as_array.append(np_array)
        # cv2.imwrite(str(label[i])+str(i)+".png", ig)
        # i = i+1

    return np.array(all_images_as_array), np.array(label)


path_to_train_set = "Dataset/train/"
path_to_test_set = "Dataset/test/"
X_train, y_train = get_data(path_to_train_set)
X_test, y_test = get_data(path_to_test_set)

trainig_data = []
for i in range(len(X_train)):
    trainig_data.append([X_train[i], y_train[i]])


print(trainig_data)

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(90, 90, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
#model.add(Dropout(0.3))
model.add(Dense(2, activation = 'softmax'))