import tkinter as tk
from tkinter import *
import SentimentalAnalysis as Senti
import DataReader as db
import Statistics

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class Application():
    
    def __init__(self):
        self.Window_Create()
        #self.Second_window()
        
        
    def Window_Create(self):
        top = tk.Tk()
        top.title("Movie review")
        top.geometry("500x180")

        self.frame = Frame(top)
        self.frame.grid()
        
        self.label = Label(top, text="Review")
        self.label.grid(row = 0 , column = 0)
        
        self.text = Entry(top , width=55)
        self.text.grid(row = 0,column = 1, columnspan = 2)
        
        self.textbox = Text(top,width=40,height=8)
        self.textbox.grid(row = 1, column=1, columnspan = 2)
        self.textbox.insert(tk.END,"After Entering review press Enter:\n")
        
        self.btn1=Button(top,text="Enter", width=20, command=self.Btn_Submit)
        self.btn1.grid(row = 2 , column = 0)

        self.btn2=Button(top,text="Clear", width=20, command=self.Btn_Clear)
        self.btn2.grid(row = 2, column = 1)
        
        self.btn4=Button(top,text="Submit", width=20, command=self.popupmsg)
        self.btn4.grid(row = 2, column = 2)
        
        
        top.mainloop()
    
    def Btn_Submit(self):
        StopWords = set(stopwords.words('english'))
        dataset = db.DataReader()
        sta= Statistics.Stats(dataset.unique_pos,dataset.unique_neg)
        self.data = self.text.get()
        words=self.data.split()
        for word in words:
            if word in StopWords or word in string.punctuation:
                continue
            else:
                temp=word       
                print(temp)
        sa = Senti.SentimentalAnalysis()
        self.textbox.insert(tk.END,self.data)
        self.textbox.insert(tk.END,"\nNaiveBayes Result :")
        self.textbox.insert(tk.END,sa.NaiveBayes(temp,sta))
        self.textbox.insert(tk.END,"\nBayesianBayes Result :")
        self.textbox.insert(tk.END,sa.BayesianBayesResult(temp,sta))
        
    def Btn_Clear(self):
        self.text.delete('0',tk.END)
        self.textbox.delete(1.0,tk.END)
        
    def popupmsg(self):
        NORM_FONT = ("Helvetica", 10)
        self.popup = tk.Tk()
        self.popup.wm_title("!")
        msg="Is The Result Correct"
        self.label = Label(self.popup, text=msg, font=NORM_FONT)
        self.label.pack(side="top", fill="x", pady=10)
        self.B1 = Button(self.popup, text="Yes", width= 20, command = self.store_data)
        self.B1.pack()
        self.B2 = Button(self.popup, text="No", width= 20 ,command = self.Second_window)
        self.B2.pack()
        self.popup.mainloop()
    
    def store_data(self):
        self.popup.destroy()
        dataset = db.DataReader()
        sta= Statistics.Stats(dataset.unique_pos,dataset.unique_neg)
        sa = Senti.SentimentalAnalysis()
        
        if((sa.NaiveBayes(self.data,sta) == "Positive") and (sa.BayesianBayesResult(self.data,sta) == "Positive")):
            value="Pos"
        if((sa.NaiveBayes(self.data,sta) == "Negative") and (sa.BayesianBayesResult(self.data,sta) == "Negative")):
            value="Neg"    
        dataset.Store_data(value,self.data)
    
    def Second_window(self):
        window=tk.Tk()
        window.title("Edit Answer")
        window.geometry("400x180")
        
        self.frame2 = Frame(window)
        self.frame2.grid()
        
        self.label2 = Label(window, text="Review")
        self.label2.grid(row = 0 , column = 0)
        
        self.text2 = Entry(window , width=55)
        self.text2.grid(row = 0,column = 1, columnspan=2)
        
        self.textbox2 = Text(window,width=40,height=8)
        self.textbox2.grid(row = 1, column=1, columnspan = 2)
        self.textbox2.insert(tk.END,self.data)
        
        self.btn3=Button(window,text="Submit", width=25, command=self.update_answer)
        self.btn3.grid(row = 2 , column = 1)
       
        self.btn5=Button(window,text="Close", width=25, command=window.destroy)
        self.btn5.grid(row = 2 , column = 2)
        
        window.mainloop()
        
    def update_answer(self):
        dataset = db.DataReader()
        self.data2 = self.text2.get()
        if(self.data2 == "Positive" or self.data2 == "positive"):
            value = "Pos"
        if(self.data2 == "Negative" or self.data2 == "negative"):
            value = "Neg"
        dataset.Store_data(value,self.data)
            
        
        
        
        
        
app = Application()

