# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zHMT6eP-Y9YKCX0JHM_5iX7SzPoK_nK8
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('zomato.csv')
df.head(5)

df.isna().sum()
plt.plot(df['Date'],df['Close'])
plt.show()

df['open-close'] = df['Open'] - df['Close']
df['high-low'] = df['High'] - df['Low']
X = df[['open-close','high-low']]
Y = np.where(df['Close'].shift(-1) > df['Close'],1,-1)
Y = pd.DataFrame(Y)

Y.head(5)
Y.rename(columns={0:'Target'},inplace=True)
Y.head(5)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
X_train.head(5)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train,Y_train)
y_pred = rf.predict(X_test)
rf.score(X_test,Y_test)
y_pred

comp = pd.DataFrame(Y_test)
comp['Predicted'] = y_pred
comp.head(5)