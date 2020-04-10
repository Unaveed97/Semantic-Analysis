# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 07:24:41 2019

@author: Umer's Pc
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import naive_bayes
import csv
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import Statistics as sta

class SciKitLearn:
    
    def SciFunc(self,msg): 
        str=[]
        with open("movie-pang02.csv", "r") as file:
            freereader = csv.reader(file)
            for row in freereader:
                str.append(row)
        
        str.pop(0)
        df=pd.DataFrame(str)
        print(df)
        
        y=df[0]
        stopWords=set(stopwords.words('english'))
        
        # tfidf frequency reverse krta hai taka the,a jese words jinki sentiment value nhai hoti lekin frequency ziada hoti hai
        # word count de raha hai humne tfidf wale function ko yeh btayaa haai ke jo usne frequency jo calculate krni hai woh words ki krni
        # hai iss liye ascci likha hai
        vectorizer=TfidfVectorizer(use_idf=True,lowercase=True,strip_accents='ascii',stop_words=stopWords)
        x=vectorizer.fit_transform(df[1])
        print(x)
        
        print(y.shape)
        print(x.shape)
    
        clf=naive_bayes.MultinomialNB()
        clf.fit(x,y)    
        
        test = vectorizer.transform([msg])
        print(test)
        return clf.predict(test)
        

