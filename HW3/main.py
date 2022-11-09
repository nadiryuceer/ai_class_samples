import numpy as np
import pandas as pd
import sklearn

from KNN import KNN
from NB import NB
from DT import DT
import time


def testkneighbour():
    algorithm = None
    test = 0.2
    import matplotlib.pyplot as plt
    while float(test) < 1:
        neighbourk = []
        neighbour = []
        for i in range(1, 20):
            algorithm = KNN(i, test)
            neighbourk.append(i)
            timepass=time.time()
            neighbour.append(algorithm.run(digits, data))
            print(time.time()-timepass)
        plt.plot(neighbourk, neighbour, label='test_size=' + str(test))
        test += 0.3
    plt.xlabel("k")
    plt.ylabel("Accuracy")
    plt.title("KNearestNeighbours")
    plt.grid(ls="-.", lw=0.50)
    plt.legend()
    plt.show()


def testbayesian():
    algorithm = None
    test = 0.2
    alpha = 0.1
    import matplotlib.pyplot as plt
    for j in range(0, 2):
        test = 0.2
        while float(test) < 1:
            Naivealpha = []
            Alphaacc = []
            algorithm = NB(j, test)
            Naivealpha.append(1)
            timepass=time.time()
            Alphaacc.append(algorithm.run(digits, data))
            print(time.time()-timepass)
            if j == 0:
                plt.scatter(Naivealpha, Alphaacc, label='Multinomial:test_size=' + str(test), marker="*", s=30)
            else:
                plt.scatter(Naivealpha, Alphaacc, label ='Gaussian:test_size=' + str(test), marker=".", s=30)
            test += 0.3
    plt.xlabel("run")
    plt.ylabel("Accuracy")
    plt.title("Naive Bayes")
    plt.legend()
    plt.show()


def testdectree():
    algorithm = None
    import matplotlib.pyplot as plt
    test = 0.2
    while float(test) < 1:
        depthmax = []
        results = []
        for i in range(1, 20):
            algorithm = DT(i, test)
            depthmax.append(i)
            timepass=time.time()
            results.append(algorithm.run(digits, data))
            print(time.time()-timepass)
        plt.plot(depthmax, results, label='test_size=' + str(test))
        test += 0.3
    plt.xlabel("Max Tree Depth")
    plt.ylabel("Accuracy")
    plt.title("Decision Tree Classifier")
    plt.xlim(0, 20)
    plt.grid(ls="-.", lw=0.50)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    from sklearn.datasets import fetch_openml
    print("fetching")
    digits = fetch_openml('mnist_784')
    print("fetch done")
    print(digits)
    print(digits.keys())
    n_samples = len(digits.data)
    data = digits.data.reshape(n_samples, -1)
    #   These methods are predicting the class with different parameters
    #   Also you should remove comments from the classes if you want to see
    #   the confusion matrix of the results.
    #   There is a results.txt file which shows runtime and accuracy of the previous runs I made.
    #testkneighbour()
    testbayesian()
    testdectree()
