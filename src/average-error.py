import pandas as pd 
import sys 

f_actual = sys.argv[1]
f_pred = sys.argv[2]
f_window = open(sys.argv[3],'r')
f_output = open(sys.argv[4],'w+')
w = int(f_window.read())  #w is the window size 

actual = pd.read_table(f_actual, sep='|',names = ['time','stock','price'], header = None)     
preds = pd.read_table(f_pred, sep='|',names = ['time','stock','price'], header = None)
       
#Function for calculating price of a particular stock and time 
def func(t,stock_name,df):
    df1 = df[(df.time ==t) & (df.stock == stock_name)] 
    if (len(df1) != 0): 
        value = df1.price[df1.index.values[0]]
    else: 
        value = 'NA' 
    return value  
    
#Function for calculating the average error for a given time window     
def error_func(w1,w2): 
    unique_name = actual.stock.unique() 
    err = [abs(func(t,name, actual) - func(t,name,preds)) 
            for t in range(w1,w2) 
            for name in unique_name 
            if(func(t,name,preds) != 'NA')]
        
    f_output.write("%1.0f|%1.0f|%0.2f \n" %(w1,w2-1,sum(err)/len(err)))  
        
T = max(actual.time)   #Total time for which the data is available

#Iterating over all the windows     
map(lambda i:error_func(i,i+w),list(range(1,T-w+2))) 
  
f_output.close()   