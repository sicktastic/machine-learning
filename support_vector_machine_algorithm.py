from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y) 
clf = clf.predict([[2., 2.]])
print(clf)

# from sklearn.svm import SVC
# clf = SVC(kernel="linear")
# clf.fit( features_train, labels_train )
# pred = clf.predict( features_test, labels_test )

# from sklearn.metrics import accuracy_score
# acc = accuracy_score(pred, labels_test)
