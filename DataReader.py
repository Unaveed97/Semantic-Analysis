# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:02:59 2019

@author: DELL
"""

import csv
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class DataReader:
    
    def __init__(self):
        self.data = self.getRecord()
        self.positive = []
        self.negative = []
        self.Separate_Data()
        self.unique_pos = self.PositiveUnique()
        self.unique_neg = self.NegativeUnique()
        
    def getRecord(self):
        data=[]
        with open("movie-pang02.csv",'r') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                data.append(row)
        data.pop(0)
        print(len(data))
        return data
    
    #Separating the data in to two lists
    def Separate_Data(self): 
        for i in self.data:
            if i[0] == "Pos":
                self.positive.append(i)
            elif i[0] == "Neg":
                self.negative.append(i)
        #print(self.positive)
            
    def PositiveUnique(self):
        StopWords = set(stopwords.words('english'))
        unique={}
        #print(StopWords)
        for i in range(len(self.positive)):
            words=self.positive[i][1].split()
            for word in words:
                if word in StopWords or word in string.punctuation:
                    continue
                if word not in unique:
                    unique[word] = {"Pos": 0}
                if word in unique:
                    unique[word]["Pos"] += 1
        return unique
    
    def NegativeUnique(self):
        StopWords = set(stopwords.words('english'))
        unique={}
        for i in range(len(self.negative)):
            words=self.negative[i][1].split()
            for word in words:
                if word in StopWords or word in string.punctuation:
                    continue
                if word not in unique:
                    unique[word] = {"Neg": 0}
                if word in unique:
                    unique[word]["Neg"] += 1
        return unique
    
    def Store_data(self,value,review):
        mydata=[value,review]
        with open('movie-pang02.csv','a',newline='') as fd:
            writer = csv.writer(fd)
            writer.writerow(mydata)

db= DataReader()
            