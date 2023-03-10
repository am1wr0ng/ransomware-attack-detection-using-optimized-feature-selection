# -*- coding: utf-8 -*-
"""KNN_Y_Team

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rUeToYjwfXMpBMuP0dWn5c-gENh6_kob
"""

!pip install category_encoders

import numpy as np
import pandas as pd
import time
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('GFS_Feature.csv')
print(data.head())

from category_encoders import OrdinalEncoder
#OFS
#enc1 = OrdinalEncoder(cols = ['basename','remote_address.ip','st_mtime','st_atime','st_ctime'])

#GFS
enc1 = OrdinalEncoder(cols = ['metadata.source_urn','urn','basename','st_atime','local_address.port'])
data = enc1.fit_transform(data)
data

data = data.fillna(0)

#컬럼명이 labeling인 부분을 삭제하고, 그걸 X로로
X =  data.drop(labels='labeling',axis=1)
X

#컬럼명이 labeling인 부분을 y (공격/정상을 분류하는 문제이므로로)
y = data['labeling']
y

#데이터셋 스케일링링
from sklearn.preprocessing import StandardScaler

# 변형 객체 생성
std_scaler = StandardScaler()

# 학습데이터의 모수 분포 저장
std_scaler.fit(X)

# 학습 데이터 스케일링
X_train_scaled = std_scaler.transform(X)
X = X_train_scaled

#training set:test set = 7:3비율로 맞춰놓고 학습하기 위함

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state = 42
)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification

#KNeighborClassifier를 정의하고 핵심 파라미터인 n_neighbors를 지정함
#n_jobs는 학습에 사용할 코어의 숫자를 지정함(-1은 모든 코어를 사용한다는 뜻)
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)

#fit은 학습 시키는 과정A
knn.fit(X_train, y_train)

pred = knn.predict(X_test)

end = time.time()

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import classification_report
print(classification_report(y_test,pred))
#정상행위: 0, trojan: 1, psransom: 2, apt: 3



