from numpy.random import permutation
from sklearn import svm, datasets

C = 1.0
gamma = 0.7
training_size = 90

iris = datasets.load_iris()
perm = permutation(iris.target.size)
iris.data = iris.data[perm]
iris.target = iris.target[perm]

clf = svm.SVC(C, 'rbf', gamma=gamma)
clf.fit(iris.data[:training_size],
        iris.target[:training_size])
print(clf.score(iris.data[training_size:],
                iris.target[training_size:]))