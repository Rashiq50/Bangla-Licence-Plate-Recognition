from PIL import Image
import os
import numpy as np
import re
import cv2

def get_label(path):
    # print(os.listdir(path))

    label = []
    for filename in os.listdir(path):
        try:
            if re.match(r'0', filename):
                label.append(0)
            else:
                label.append(1)
        except:
            continue
    return np.array(label)


def get_data_image(path):
    all_images_as_array = []
    for filename in os.listdir(path):
        dir = path + filename
        np_array = cv2.imread(dir)
        l, b, c = np_array.shape
        np_array = np_array.reshape(l * b * c, )
        all_images_as_array.append(np_array)

    return np.array(all_images_as_array)


train_set = "Dataset/train/"
test_set = "Dataset/test/"

X_train = get_data_image(train_set)
X_test = get_data_image(test_set)

y_train = get_label(train_set)
y_test = get_label(test_set)

print(X_train)
print('y_train set : ', y_train)
print(X_test)
print('y_test set : ', y_test)
