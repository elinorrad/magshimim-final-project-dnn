# -*- coding: utf-8 -*-
"""DNN_07/03/25 final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yRfPoz9maivjT6nCGH--9k63DJiMKXZI
"""

import pandas as pd
from google.colab import files

uploaded = files.upload()

df = pd.read_csv(list(uploaded.keys())[0])

df = df.iloc[:, 1:]

print("מספר שורות:", df.shape[0])
print("מספר עמודות:", df.shape[1])
df.head()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

label_encoder = LabelEncoder()
df['Category'] = label_encoder.fit_transform(df['Category'])

df.fillna(df.mean(), inplace=True)

X = df.iloc[:, 1:]
y = df['Category']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

num_classes = len(label_encoder.classes_)

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"דיוק המודל: {test_acc:.4f}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_pred = np.argmax(model.predict(X_test), axis=1)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("מטריצת בלבול - רשת נוירונים")
plt.show()

import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)

from google.colab import files
files.download("model.tflite")

import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # הוספת אופטימיזציה
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)

from google.colab import files
files.download("model.tflite")

import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

print("המודל נטען בהצלחה!")