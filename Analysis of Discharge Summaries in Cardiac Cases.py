import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt 

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/pro1.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')
df

df['Final'] = df['Final Diagnosis'].str.split(' - ').str[0]
x=df['Final']
#x

df['Final'] = df['Investigative Procedures'].str.split(' - ').str[0]
x=df['Final']
#x

df['Final'] = df['Symptoms'].str.split(' - ').str[0]
x=df['Final']
#print(x)

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')
df

df.drop(['IP No'], 1, inplace=True)
df.drop(['Hospital No'], 1, inplace=True)
df.drop(['Past History'], 1, inplace=True)
df.drop(['Laboratory Data'], 1, inplace=True)
df.drop(['Therapeutic Procedures'], 1, inplace=True)
df.drop(['Dietry Advice'], 1, inplace=True)
df.drop(['Prepared'], 1, inplace=True)
df.drop(['To contact'], 1, inplace=True)
df.drop(['Complaints on Reporting'], 1, inplace=True)
df.drop(['Phsical findings of Examination'], 1, inplace=True)
df.drop(['Courses of Treatment in the Hospital'], 1, inplace=True)
df.drop(['Further Advice on Discharge'], 1, inplace=True)
df.to_csv('new discharge summary.csv')

data

import datetime

data = pd.read_csv('new discharge summary.csv')
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Date of Discharge'] = pd.to_datetime(df['Date of Discharge'])
df['number of days'] = (df['Date of Admission'] - df['Date of Discharge']).abs()
df.to_csv('new discharge summary.csv')
df

data = pd.read_csv('new discharge summary.csv')
var = (df['number of days'].value_counts())
fig = plt.figure()
bar_width = 0.35
opacity = 0.8
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('days')
ax1.set_ylabel('NUMBERS')
var.plot(kind='bar')
plt.title('DAYS REQUIRED FOR RECOVER')

plt.show()

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')
#df

print("The number of males and females patient")
b=df['Sex'].value_counts()
print(b)

var = (df['Sex'].value_counts())
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('GENDER')
ax1.set_ylabel('NUMBERS')
var.plot(kind='bar')
plt.title('Number of Males and Females')

plt.show()

e = df.groupby('Age').agg({'Age':'count'})
e =e.rename(columns={'Age': 'count'})
e =e.reset_index()
e = e.sort_values('Age')
#e


df['count'] = 1
df['age_group'] = pd.cut(df.Age, [0, 20, 40, 60, 80, 100])
d = df.pivot_table('count', index='age_group', columns='Sex', aggfunc='sum')
#d


d.to_csv("plot.csv")


data = pd.read_csv("plot.csv")
data.set_index('age_group', inplace=True)
get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')
data.plot(kind='bar', figsize=(20,8), color=['skyblue','gray'])
plt.xlabel('AGE GROUPS')
plt.ylabel('NUMBERS')
plt.title('COMPARISION OF AGE GROUP')

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')

print("The patient got discharged on the following condition")
a=df['Condition on Discharge'].value_counts()
print(a)

b.to_csv("condition plot.csv")

data = pd.read_csv("symp plot1.csv")
data.set_index('Symptoms', inplace=True)
get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')
data.plot(kind='bar', figsize=(20,8), color=['pink'])
plt.xlabel('SYMPTOMS')
plt.ylabel('NUMBERS')
plt.legend()
plt.title('NUMBER OF PEOPLE SUFFERING FROM')


a=df['Symptoms']
b=a.value_counts().head(5)
#b

b.to_csv("Symp plot.csv")

my_columns = ["Symptoms", "Numbers"]
b = pd.read_csv("symp plot.csv",names=my_columns)
#b.to_csv("symp plot1.csv")

df = pd.read_csv("symp plot1.csv")
df = df.groupby('Symptoms').sum().reset_index()
#df

data = pd.read_csv("symp plot1.csv")
data.set_index('Symptoms', inplace=True)
get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')
data.plot(kind='bar', figsize=(20,8), color=['pink'])
plt.xlabel('SYMPTOMS')
plt.ylabel('NUMBERS')
plt.legend()
plt.title('NUMBER OF PEOPLE SUFFERING FROM')

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')

a=df['Final Diagnosis']
b=a.value_counts().head(7)
#b

b.to_csv("diag plot.csv")

my_columns = ["diagnosis procedure", "Numbers"]
z = pd.read_csv("diag plot.csv",names=my_columns)
#z.to_csv("diag plot1.csv")

df = pd.read_csv("diag plot1.csv")
df = df.groupby('diagnosis procedure').sum().reset_index()
df

data = pd.read_csv("diag plot1.csv")
data.set_index('diagnosis procedure', inplace=True)
get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')
data.plot(kind='bar', figsize=(20,8), color=['yellow'])
plt.xlabel('PROCEDURE')
plt.ylabel('NUMBERS')
plt.title('FINAL DIAGNOSIS')

xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls')
xls_file
xls_file.sheet_names
df = xls_file.parse('discharge summary')

a=df['Investigative Procedures'] 
b=a.value_counts().head(10) 
#b 
 
b.to_csv("investigative plot.csv") 
 
my_columns = ["investigative procedure", "Numbers"] 
z = pd.read_csv("investigative plot.csv",names=my_columns) 
#z.to_csv("investigative plot1.csv") 
 
df = pd.read_csv("investigative plot1.csv") 
df = df.groupby('investigative procedure').sum().reset_index() 
df 
 
data = pd.read_csv("investigative plot1.csv") 
data.set_index('investigative procedure', inplace=True) 
get_ipython().magic('matplotlib inline') 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
mpl.style.use('ggplot') 
data.plot(kind='bar', figsize=(20,8), color=['orange']) 
plt.xlabel('PROCEDURE') 
plt.ylabel('NUMBERS') 
plt.title('INVESTIGATIVE PROCEDURES') 

 
xls_file = pd.ExcelFile('C:/Users/vidyamani.k.c/pro/proj.xls') 
xls_file 
xls_file.sheet_names 
df = xls_file.parse('discharge summary') 
 
r = df.groupby(['Symptoms','Investigative Procedures'])['Final Diagnosis'].value_counts() 
#r 
 
r.to_csv("final plot.csv") 
 
my_columns = ["symptoms","Investigative Procedures" "Final Diagnosis"] 
z = pd.read_csv("final plot.csv",names=my_columns) 
#z.to_csv("final plot1.csv") 
 
df = pd.read_csv("final plot1.csv") 
#df = df.groupby('investigative procedure').sum().reset_index() 
df 