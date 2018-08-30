# Table of Contents
1. [Language](README.md#Language)
1. [libraries](README.md#Libraries)
1. [Approach](README.md#Approach)


## Language
Python 2


## Libraries
I have used the following python libraries.  
1. pandas
1. sys


## Approach

### Reading the data
I have used pandas for reading both the data files, namely the actual and predicted values and converting it to pandas data frame.

### Function for calculating price corresponding to a particular stock and time  
This function returns the price, given the time and the stock name. It returns the price as 'NA', if there is no data available for a particular time and stock name, which may happen in the case of the predictions data.

### Function for calculating the average error for a given time window
This function returns absolute error corresponding to a given time window. Here, I have used list comprehension to iterate over the time duration belonging to a particular time window as well as iterating over all the stocks in the actual observations data. Then I used all the error values to calculate the average error.

### map function to iterate over the entire dataset    
In order to write all errors for the windows corresponding to entire dataset I used a map function to cover all the time windows for the above mentioned function for finding error.

