#importing the libraries required
from matplotlib import pyplot as plt
import numpy as np

#data for the pie
name = input("enter the names of set:")
name1= name.split()
dataset = input("enter the data according to the set:")
dataset1 = dataset.split()
title1 = input("enter the title:")


#creating of the plot

fig = plt.figure(figsize=(10,7))
plt.title(title1)
plt.pie(dataset1,labels = name1)

#plot representation
plt.show()