class DT:
    def __init__(self, dlimit, testsize):
        from sklearn.tree import DecisionTreeClassifier
        self.classifier = DecisionTreeClassifier(max_depth=dlimit)
        import matplotlib.pyplot as plot
        self.plot = plot
        self.testsize = testsize

    def plotMeasure(self, x_test, y_test, predict):
        from sklearn.metrics import plot_confusion_matrix
        """disp = plot_confusion_matrix(self.classifier, x_test, y_test)
        print(disp.confusion_matrix)
        self.plot.show()"""
        from sklearn.metrics import accuracy_score
        acc = accuracy_score(y_test, predict)
        print(acc)
        return acc

    def run(self, digits, data):
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(data, digits.target,test_size=self.testsize, random_state=0)
        self.classifier.fit(x_train, y_train)
        predicted = self.classifier.predict(x_test)
        return self.plotMeasure(x_test, y_test, predicted)