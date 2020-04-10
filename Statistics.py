# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:36:09 2019

@author: DELL
"""
import DataReader as db

class Stats:
    
    def __init__(self,Pos_Unique_words,Neg_Unique_words):
        count=self.getCount(Pos_Unique_words,Neg_Unique_words)
        self.posCount = count[0]
        self.negCount = count[1]
        tempStat=self.getProbabilities(Pos_Unique_words.copy(),Neg_Unique_words.copy(),self.posCount,self.negCount)
        self.Posstat = tempStat[0]
        self.Negstat =tempStat[1]
        
    def getCount(self,Pos_Unique_words,Neg_Unique_words):
        pos=0
        neg=0
        for key_pos in Pos_Unique_words.keys():
            pos += Pos_Unique_words[key_pos]["Pos"]
        for key_neg in Neg_Unique_words.keys():
            neg += Neg_Unique_words[key_neg]["Neg"]
        return pos, neg
    
    def getProbabilities(self, posUnique, negUnique, posCount, negCount):
        for key_pos in posUnique.keys():
            posUnique[key_pos]["PosProb"] = float((posUnique[key_pos]["Pos"] + 1) / (posCount + len(posUnique)))
        for key_neg in negUnique.keys():
            negUnique[key_neg]["NegProb"] = float((negUnique[key_neg]["Neg"] + 1) / (negCount + len(negUnique)))
        return posUnique, negUnique 
    
    def DefaultProbability(self, type):
        if type == "Pos":
            return float(1 / (self.posCount + len(self.Posstat)))
        elif type == "Neg":
            return float(1 / (self.negCount + len(self.Negstat)))
        return 1

#dataset=db.DataReader()    
#sta=Stats(dataset.unique_pos,dataset.unique_neg)
#print(sta.posCount)
#print(sta.negCount)