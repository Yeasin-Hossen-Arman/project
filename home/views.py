from django.shortcuts import render

import pandas as pd
from sklearn.preprocessing import LabelEncoder
#import train test split from sklearnin
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV

# Create your views here.
def index(request):
    return render(request,"index.html")


#first stage input manage 

def result(request):

    # db = pd.read_csv(r'E:\Computer_Science\Mechine_Learning\projects\Diabetes_predection\Data\diabetes.csv')
    df = pd.read_csv(r'Date\afkldjdjlfdj.csv')
    df=df[df['Disease'] != 'Anemia']
    df=df[df['Disease'] != 'Polio']
    df=df[df['Disease'] != 'Brain Tumor']
    df=df[df['Disease'] != 'Rabies']
    df=df[df['Disease'] != 'Hepatitis B']
    df=df[df['Disease'] != 'Cholera']
    df=df[df['Disease'] != 'Mumps']
    df=df[df['Disease'] != 'Dengue Fever']
    df=df[df['Disease'] != 'Typhoid Fever']
    df=df[df['Disease'] != 'Malaria']


    df['Fever']=df['Fever'].map({'No':0,'Yes':1})
    df['Cough']=df['Cough'].map({'No':0,'Yes':1})
    df['Fatigue']=df['Fatigue'].map({'No':0,'Yes':1})
    df['Difficulty Breathing']=df['Difficulty Breathing'].map({'No':0,'Yes':1})
    df['Blood Pressure']=df['Blood Pressure'].map({'Low':1,'Normal':2,'High':3})
    df['Cholesterol Level']=df['Cholesterol Level'].map({'Low':1,'Normal':2,'High':3})
    df['Outcome Variable']=df['Outcome Variable'].map({'Negative':0,'Positive':1})



    df= df.drop(['Outcome Variable'], axis =1)
    le = LabelEncoder()
    le.fit(df['Disease'])
    df['DiseaseNum']=le.fit_transform(df['Disease'])
    df = df.drop(['Age'], axis =1)
    df = df.drop(['Disease'], axis =1)
    df = df.drop(['Gender'], axis =1)
    X = df.drop(['DiseaseNum'], axis = 1)
    y = df['DiseaseNum']
    # split train 70% and test 30% of dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=20)
    clf = MultinomialNB()
    clf.fit(X, y)
    parameters = {'alpha':[1,2,4,5,10,12,15,17,20,22,25]}
    clfcv= GridSearchCV(clf,parameters,cv = 5)
    clfcv.fit(X_train,y_train)
    

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])

    

    pred = clfcv.predict([[val1,val2,val3,val4,val5,val6]])
    

    result2 = ''


    #['Asthma--0',
#'Common Cold--1',
#'Depression--2',
#Diabetes--3',
#'Hepatitis----4',
#'Influenza---5',
#"Parkinson's Disease---6",
#'Pneumonia----7',
#'Stroke'-----8]

    if pred == [0]:
        result2 = "Asthma"
    elif pred == [1]:
        result2 = 'Common Cold'
    elif pred == [2]:
        result2 = 'Depression'
    elif pred == [3]:
        result2 = 'Diabetes'
    elif pred == [4]:
        result2 = 'Hepatitis'
    elif pred == [5]:
        result2 = 'Influenza'
    elif pred == [6]:
        result2 = 'Parkinsons Disease'
    elif pred == [7]:
        result2 = 'Pneumonia'
    else:
        result2 = "Stroke"

    return render(request,"index.html",{"result2":result2})
