#Compatible with Python 2.7 and higher
import random
import numpy as np
import matplotlib.pyplot as plt

'''n is taken as an input'''
n = int(input("Enter n:"))

'''Initialisation'''
scores = np.zeros(n) #Scores are initialised to zero
episodes = 5000 #episodes can be set to be higher, we worked with 100000

'''Running the episodes'''
for episode in range(1, episodes + 1):
    L = np.random.random(n) #Generates a random array
    print("episode-", episode)
    for k in range(1, n): #Runs loop on k
        max_k = max(L[:k])
        for idx in range(k, n):
            if max_k < L[idx]:
            #Number just greater than maximum in subset of first k elements
                break
        if idx == np.argmax(L):
            #Maximum is obtained
            scores[k] += 1
k = np.argmax(scores) + 1 #Value of k, one added as indexing of list from 0
print("Optimum k=", k)
probs = scores*1.0/episodes
print("prob-", max(probs))


#Uncomment to plot the graph
# '''Plotting'''
# plt.figure(1)
# plt.plot(probs)
# plt.title(r'$n = 1000$')
# plt.xlabel(r'$k$')
# plt.ylabel(r'$p_{k, n}$')
# plt.plot(k, probs[k], 'go') #the maxima is marked
#
# plt.show()
