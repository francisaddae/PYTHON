import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import graphviz

####            1.Data Preparation            ####
print('========================= Data Preparation =========================')
data = pd.read_csv("winequality-white.csv", header=0, sep=';')
labels = data["quality"].values
data = data.drop("quality", axis=1)

# Randomly spliting the data into 2 (traindata & testdata)
# Randomly spliting the labels into train and test labels
traindata, testdata = train_test_split(data, test_size=0.2, random_state=80)
train_labels, test_labels = train_test_split(
    labels, test_size=0.2, random_state=80)
traindata = traindata.values
testdata = testdata.values
print(
    'Variables are: {traindata,train_labels} --> for training, {testdata, test_labels} -> for testing')
print("========================= Preparation Ended =========================\n")

####            2.Parameter Tuning using 5-fold cross Validation            ####
# Decision Tree


def dtc_parameter_tune1(traindata, train_labels):
    print('''========================= Parameter Tuning using 5 - Fold Cross Validation =========================
    !!!!!!!!      FOR DECISION TREE using DecisionTreeClassifier(max_depth = depth)      !!!!!! ''')
    depths = [x for x in range(1, 125, 29)]
    All_train_accScore = []
    All_val_accScore = []

    kf = KFold(n_splits=5)
    for depth in depths:
        train_acc = []
        val_acc = []
        for x, y in kf.split(traindata):
            train_X = traindata[x, :]
            val_X = traindata[y, :]

            train_Y = train_labels[x]
            val_Y = train_labels[y]

            dtc = tree.DecisionTreeClassifier(max_depth=depth)
            dtc.fit(train_X, train_Y)
            train_acc.append(dtc.score(train_X, train_Y))
            val_acc.append(dtc.score(val_X, val_Y))

        avg_train_acc = sum(train_acc) / len(train_acc)
        avg_val_acc = sum(val_acc) / len(val_acc)
        print("Depth: ", depth)
        print("Training accuracy: ", avg_train_acc * 100, "%")
        print("Validation accuracy: ", avg_val_acc * 100, "%")
        All_train_accScore.append(avg_train_acc)
        All_val_accScore.append(avg_val_acc)
    return depths, All_train_accScore, All_val_accScore


depths, DTtrain, DTval = dtc_parameter_tune1(
    traindata, train_labels)
'''plt.plot(depths, DTtrain, marker='*', label='Training Accuracy')
plt.plot(depths, DTval, marker='*', label='Validation Accuracy')
plt.title('DECISION TREE using DecisionTreeClassifier(max_depth=depth)')
plt.xlabel('Depth of Tree')
plt.ylabel('Accuracy')
plt.legend()
plt.show()'''

# Using RandomForest


def dtc_parameter_tune2(traindata, train_labels):
    print('''\n           Parameter Tuning using 5 - Fold Cross Validation:
    !!!!!!!!     FOR RANDOM FOREST TREE using RandomForestClassifier(n_estimator = depth)     !!!!!!''')
    depths = [x for x in range(1, 125, 29)]
    All_train_accScore = []
    All_val_accScore = []

    kf = KFold(n_splits=5)
    for depth in depths:
        train_acc = []
        val_acc = []
        for x, y in kf.split(traindata):
            train_X = traindata[x, :]
            val_X = traindata[y, :]

            train_Y = train_labels[x]
            val_Y = train_labels[y]

            clf = RandomForestClassifier(n_estimators=depth)
            clf.fit(train_X, train_Y)
            train_acc.append(clf.score(train_X, train_Y))
            val_acc.append(clf.score(val_X, val_Y))

        avg_train_acc = sum(train_acc) / len(train_acc)
        avg_val_acc = sum(val_acc) / len(val_acc)
        print("Depth: ", depth)
        print("Training accuracy: ", avg_train_acc * 100, "%")
        print("Validation accuracy: ", avg_val_acc * 100, "%")
        All_train_accScore.append(avg_train_acc)
        All_val_accScore.append(avg_val_acc)
    return depths, All_train_accScore, All_val_accScore


depths, RFtrain, RFval = dtc_parameter_tune2(traindata, train_labels)
'''plt.plot(depths, RFtrain, marker='*', label='Training Accuracy')
plt.plot(depths, RFval, marker='*', label='Validation Accuracy')
plt.title('RANDOM FOREST TREE using RandomForestClassifier(n_estimator=depth)')
plt.xlabel('Depth of Tree')
plt.ylabel('Accuracy')
plt.legend()
plt.show()'''
print("========================= Parameter Tuning Ended =========================\n")

####            3. Test the classifiers            ####


def BestValueParameter(depths, DTtrain, DTtval, RFtrain, RFval):
    print('========================= BEST Parameter Testing =========================')
    # For the decision tree Only
    best1 = depths[np.argmax(DTval)]
    dtc = tree.DecisionTreeClassifier(max_depth=best1)
    dtc = dtc.fit(traindata, train_labels)
    DTtrain = dtc.score(traindata, train_labels)
    DTtest = dtc.score(testdata, test_labels)
    DTPred = dtc.predict(testdata)

    # For Random Forest
    best2 = depths[np.argmax(RFval)]
    clf = RandomForestClassifier()
    clf = clf.fit(traindata, train_labels)
    RFtrain = clf.score(traindata, train_labels)
    RFtest = clf.score(testdata, test_labels)
    RFPred = clf.predict(testdata)

    return best1, DTtrain, DTtest, DTPred, best2, RFtrain, RFtest, RFPred


DTbest, DTtrainScore, DTvalScore, DT_Predicted, RFbest, RFtrainScore, RFvalScore, RF_Predicted = BestValueParameter(
    depths, DTtrain, DTval, RFtrain, RFval)
print("\nFor DecisionTreeClassifier Only")
print("Best depth:  ", DTbest)
print("Training accuracy: ", DTtrainScore * 100, "%")
print("Test accuracy: ", DTvalScore * 100, "%")
print('\nFor RandomForestClassifier')
print("Best depth: ", RFbest)
print("Training accuracy: ", RFtrainScore * 100, "%")
print("Test accuracy: ", RFvalScore * 100, "%")

print("\nConfusion matrix:")
print("For DecisionTreeClassifier")
# print(len(DT_Predicted))
print(confusion_matrix(test_labels, DT_Predicted))
print("For RandomForestClassifier")
print(confusion_matrix(test_labels, RF_Predicted))
# print(len(RF_Predicted))
print('========================= BEST Parameter Testing  Ended =========================')

####            4. Vizualize the Tree/Forest            ####
print('========================= Vizualize the Tree/Forest =========================')
print('For RandomForest Classifier Vizualization')
clf = RandomForestClassifier(n_estimators=3)
clf = clf.fit(traindata, train_labels)
dot_data = tree.export_graphviz(clf.estimators_[0], max_depth=3, filled=True, rounded=True, feature_names=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                                                                                                           'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                                                                                                           'pH', 'sulphates', 'alcohol'], class_names='quality')
graph = graphviz.Source(dot_data)
graph
# print('\nFor DecisionTree Classifier Vizualization')
# dtc = tree.DecisionTreeClassifier()
# dtc = dtc.fit(traindata, train_labels)
# dot_data = tree.export_graphviz(dtc, max_depth=3, filled=True, rounded=True, feature_names=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
#                                                                                             'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
#                                                                                             'pH', 'sulphates', 'alcohol'], class_names='quality')
# graph = graphviz.Source(dot_data)
# graph
