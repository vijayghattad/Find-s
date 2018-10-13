# Find-s 
Find-s means finding the maximally specific hypothesis.
There are mainly 2 data sets[pd1.csv and pd2.csv], The code works for both the data sets.
At present the code is written as per the first data set.
To execute the second data set we need to modify 2 lines od code that is 
S=['?','?','?','?','?','?']
X = data.values[:, 0:6]

To

S=['?','?','?']
X = data.values[:, 0:3]

why modification?
Because the second data set includes only 4 columns and we are displaying the data of first 3 columns
