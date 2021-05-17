# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import plotly
import pickle

df=pd.read_csv(r"C:\Users\nikit\ITProject2\.vscode\heart.csv")
print(df)

print(df.shape)

print(df.size)

print(df.info())

df.hist(figsize=(16,16))
plt.show()

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

classifier2 = RandomForestClassifier(random_state=1)# get instance of model
classifier2.fit(X_train, y_train)

#Neural Network
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
mlp.fit(X_train,y_train)

predict_train = mlp.predict(X_train)
predict_test = mlp.predict(X_test)

filename2 = 'heart.pkl'
pickle.dump(mlp, open(filename2, 'wb'))