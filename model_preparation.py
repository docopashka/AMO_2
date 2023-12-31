# -*- coding: utf-8 -*-
"""model_preparation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m_iyaB5MT44U9IEN9HMMeQXTiLKUPLBR
"""

import pandas as pd

df=pd.read_csv("train/train_preprocessing.csv")

df.info()

X=df.drop("precipitation", axis=1)
y=df.precipitation

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,stratify=y, shuffle = True)

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,BaggingClassifier
import xgboost
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

classifiers = [
    RandomForestClassifier(max_depth=15,min_samples_split=4,n_estimators = 600, criterion='gini',random_state=33),
    AdaBoostClassifier(random_state=33),
    BaggingClassifier(random_state=33),
    xgboost.XGBClassifier(random_state=33),

    LogisticRegression(solver='lbfgs',random_state=33)
    ]
log=[]
for clf in classifiers:
    clf.fit(x_train, y_train)
    name = clf.__class__.__name__

    print('='*30)
    print(name)

    print('****Results****')
    test_predictions = clf.predict(x_test)
    print(classification_report(y_test, test_predictions))
    acc = accuracy_score(y_test, test_predictions)
    print('Accuracy:{:.4%}'.format(acc))
    log.append([name,acc*100])

print('='*30)

log = pd.DataFrame(log)
log

import pickle
model=xgboost.XGBClassifier(random_state=33)
model.fit(x_train, y_train)

name = clf.__class__.__name__

print('='*30)
print(name)

print('****Results****')
test_predictions = model.predict(x_test)
print(classification_report(y_test, test_predictions))
acc = accuracy_score(y_test, test_predictions)
print('Accuracy:{:.4%}'.format(acc))
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))