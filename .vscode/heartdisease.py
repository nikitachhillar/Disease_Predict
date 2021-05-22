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

#assigning and normalizing 
Y = df.target
x = df.drop("target", axis = 1)
columns = x.columns
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(x)
data_x = pd.DataFrame(X, columns = columns)

#splitting 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_x, Y, test_size = 0.20, random_state = 40)

#applying model

from sklearn.metrics import classification_report 
from sklearn.neighbors import KNeighborsClassifier

classifier2 = KNeighborsClassifier(n_neighbors=30) # get instance of model
classifier2.fit(X_train, y_train) # Train/Fit model 

y_pred6 = classifier2.predict(X_test) # get y predictions
print(classification_report(y_test, y_pred6))



filename2 = 'heart.pkl'
pickle.dump(classifier2, open(filename2, 'wb'))
