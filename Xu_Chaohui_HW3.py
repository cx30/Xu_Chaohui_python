# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:55:01 2016

@author: chaohuixu
"""
##Prof G - Nice work.
### Question 1 ###
'''
Search for the IRIS dataset on the internet.	You should quickly find the	UCI Machine	 Learning	
repository. Instead of	 downloading the	files, figure out how	to directly	 load	the files from the	
internet into Python and add the	column names using Python code instead	of an	editor.
'''
import pandas as pd  #import pandas
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
        #read comma separated file into dataframe, and create a list of column names to use

### Question 2 ###
'''
Using pandas, display the first ten and the last ten rows of the data
'''
##Prof G - Need to call print() function to get output onto console
first10row = data.head(n = 10) #using pandas to display the first 10 rows of the data
last10row = data.tail(n = 10) #using pandas to display the last 10 rows of the data

### Question 3 ###
'''
Using pandas, print simple location statistics(Count, Mean, STD, MIN, 25%, 50%, 75%, MAX).
There is a single method call that will accomplish this.
'''
data.describe() #This single method call will give count, mean, std, min, 25%, 50%, 75%, max of the data

### Question 4 ###
'''
Write a function that accepts a list of numbers that represent numbers of bins and, using pandas, plots a 
histogram for each of the numeric columns at each bin size. For example, if I call your function with [10,50,100]
as bin sizes, the function should plot histograms (3 for each numeric variable). Group the histogram by the column 
name.
'''

column = ['sepal length', 'sepal width','petal length','petal width'] 
def hist(list1):
    for col in column: #select column
        for i in list1:  #select bin size
            data.hist(column = col, bins = i) #plot the histogram of selected column with choosen bin size i

##Prof G - Testing
hist([10,50,100])

### Question 5 ###
'''
Plot a box plot for each of the numeric column
'''
import matplotlib.pyplot as plt

plt.figure() #create a new object
data.boxplot(column = ['sepal length']) #draw the boxplot for the sepal length
plt.figure() #create a new object
data.boxplot(column = ['sepal width']) #draw the boxplot for the sepal width
plt.figure() #create a new object
data.boxplot(column = ['petal length']) #draw the boxplot for the petal length
plt.figure() #create a new object
data.boxplot(column = ['petal width']) #draw the boxplot for the petal width

### Question 6 ###
'''
Plot a bar chart for the nominal column
'''
data['class'].value_counts().plot(kind = 'bar') #get the last column and use value_counts() to
                                                #count frequency that a value occurs in that column, 
                                                #and plot the bar chart






        


        
        



