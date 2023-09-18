from flask import Flask,render_template
import pandas as  pd
from datetime import date
import csv
class expenses:
    dic={}
    def __init__(self,dt,xp):
        self.dt=dt
        self.xp=xp
        expenses.dic['Date']=dt
        expenses.dic['Expenses']=xp
    @classmethod
    def exp(self):
        filename="expenses.csv"
        dt=date.today()
        dt=dt.strftime("%d/%m/%y")
        stopped=False
        with open(filename,'a',newline="") as file:
            field_names=['Date','Expenses']
            csvwriter=csv.DictWriter(file,fieldnames=field_names)
            while not stopped:
                xp=int(input("enter your expenses(type 0 to stop)"))
                expenses(dt,xp)
                if xp==0:stopped=True
                else:
                    csvwriter.writerow(expenses.dic)
        file.close()
    #app=Flask(__name__)
    #@classmethod
    #@app.route('/expenses')
    #def xps(self):
expenses.exp()

df=pd.read_csv("expenses.csv")
print(df)
#>>>

    