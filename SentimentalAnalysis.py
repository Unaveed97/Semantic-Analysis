# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:39:54 2019

@author: DELL
"""
import DataReader as db
import Statistics

class SentimentalAnalysis:
    
    def NaiveBayes(self , msg ,sts):
        PosProb = NegProb = 1
        for word in msg.split(' '):
            if not self.StringCheck(sts.Posstat , sts.Negstat, word):
                PosProb=sts.DefaultProbability("Pos")
                NegProb=sts.DefaultProbability("Neg")
            elif self.StringCheck(sts.Posstat , sts.Negstat, word):
                PosProb *= sts.Posstat[word]["PosProb"]
                NegProb *= sts.Negstat[word]["NegProb"]
        if(PosProb > NegProb):
            return "Positive"
        elif(PosProb < NegProb):
            return "Negative"
        
    def BayesianBayesResult(self, msg, sts):
         PosProb = NegProb = 1
         for word in msg.split(' '):
            if not self.StringCheck(sts.Posstat , sts.Negstat, word):
                PosProb=sts.DefaultProbability("Pos")
                NegProb=sts.DefaultProbability("Neg")
            elif self.StringCheck(sts.Posstat , sts.Negstat, word):
                PosProb *= sts.Posstat[word]["PosProb"]
                NegProb *= sts.Negstat[word]["NegProb"]
         PosProb *= (sts.posCount / (sts.posCount + sts.negCount))
         NegProb *= (sts.negCount / (sts.posCount + sts.negCount))
         if(PosProb > NegProb):
            return "Positive"
         elif(PosProb < NegProb):
            return "Negative"
        
    def StringCheck(self,PosDic,NegDic,word):
        for i in PosDic.keys():
            if i == word:
                return True
        for j in NegDic.keys():
            if j == word:
                return True
        return False
    
dataset = db.DataReader()
sta= Statistics.Stats(dataset.unique_pos,dataset.unique_neg)
msg="Untill season 6 it was a great show, after that it becomes a Moneygrabber show."

for i in msg.split():
    if i in sta.Posstat:
        print(i, sta.Posstat[i])
    if i in sta.Negstat:
        print(i, sta.Negstat[i])
        
sa = SentimentalAnalysis()
print("NaiveBayes Result :" , sa.NaiveBayes(msg,sta))
print("BayesianBayes Result :" , sa.BayesianBayesResult(msg,sta))

