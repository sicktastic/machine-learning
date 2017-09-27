import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

print(iris)

X = iris.data[:, :3]
y = iris.target

print(X)


