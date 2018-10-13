#Python program to implement find-s algorithm

import pandas as pd #helps in accessing of data

#reading of the data sep->separates by , and header is the heading
data = pd.read_csv('pd1.csv', sep=',', header=None)  

S=['?','?','?','?','?','?']
X = data.values[:, 0:6]


#generalization function where Exin->example in ,S_in->specific in
def Generalize(S_in, Exin): 
   features = len(Exin)   #length of the rows
   for i in range(features):
       if(S_in[i] !=Exin[i]):   #replaces with '?' if both values are different
          S_in[i]='?'
       else:
          S_in[i]=Exin[i]     #otherwise Exin value is placed in S_in
   return(S_in)

datalen = len(data)
for i in range(datalen):
    ex=data.values[i,:]
    if(ex[-1]=='Yes'):
        S = X[i,:]
        break
    else:
        S = X[i+1,:]  
    
for i in range(datalen-1):
    ex = data.values[i+1,:]
    if(ex[-1] == 'Yes'):
        S = Generalize(S, X[i+1,:])  #calls the generalize function
print('Specific Hypothesis = ',S)