import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import log_loss

######################################    PART ONE. ######################################
# Data Loading and Visualization
files = []
for i in range(6):
    path = "lab2_data/day{:d}.txt".format(i)
    files.append(path)

# The training data is day0.txt
data = np.loadtxt(files[0], delimiter=',')
X, y = data[:, :-1], data[:, -1]

plt.scatter(X[y == 1, 0], X[y == 1, 1], marker='+', c='r', label='Hot Topic')
plt.scatter(X[y == 0, 0], X[y == 0, 1], marker='.', c='b', label='#ofDay')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='best')
plt.title('Visual Display of Data at Day 0 ')
plt.show()

#####    PART TWO. ######
# A. Training the logistic Regression Classifier


def train(X, y, l_rate):
    cls = SGDClassifier(max_iter=10000, loss='log',
                        penalty=None, learning_rate='constant', eta0=l_rate)
    # number of epochs = 10000
    # compute the loss after every 100th interval
    newLoss = []
    for i in range(10000):
        cls = cls.partial_fit(X, y, classes=np.unique(y))
        if i % 50 == 0:
            ypred = cls.predict_proba(X)
            newLoss.append(log_loss(y, ypred))

    return newLoss


l_rates = [1e-9, 1e-5, 1e-2,1e-1]
loss_lists = [train(X, y, i) for i in l_rates]

# regular Classifier


def classifier(X, y, l_rate):
    cls = SGDClassifier(max_iter=10000, tol=None, loss='log',
                        penalty=None, learning_rate='constant', eta0=l_rate)
    cls.fit(X, y)
    val = cls.score(X, y)
    return val * 100


# Picking the highest score to determine the learning rate
Score = []
for i in l_rates:
    Score.append(classifier(X, y, i))
best_rate = l_rates[Score.index(max(Score))]

# Plotting the Training Curves
fig = plt.figure()
for i in range(len(loss_lists)):
    plt.plot(np.arange(0, 10000, 50),
             loss_lists[i], label='l_rate={}'.format(l_rates[i]))
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(loc='best')
plt.title("Training Accuracy of {}% with a learning rate of {} ".format(
    max(Score), best_rate))
plt.show()

nepoch = 10000
rate = best_rate


def Para(X, y, rate, nepoch, reg):
    Losses = []
    cls = SGDClassifier(loss='log', penalty=None, alpha=reg,
                        max_iter=nepoch, tol=None, learning_rate='constant', eta0=rate)
    for epoch in range(nepoch):
        cls = cls.partial_fit(X, y, classes=np.unique(y))
        if epoch % 50 == 0:
            yPred = cls.predict_proba(X)
            Losses.append(log_loss(y, yPred))
    return Losses


reg_paras = [1e-10, 1e-25, 1e-40,1e-55]
loss_lists = []
for reg in reg_paras:
    a = Para(X, y, rate, nepoch, i)
    loss_lists.append(a)

# Picking the highest score to determine the regularization para
Score = []
for reg in reg_paras:
    cls = SGDClassifier(loss='log', penalty=None, alpha=reg,
                        max_iter=nepoch, tol=None, learning_rate='constant', eta0=rate)
    cls.fit(X, y)
    val = cls.score(X, y)
    Score.append(val)
i = Score.index(max(Score))
trainScore = max(Score)
best_reg = reg_paras[i]

# Display Traing Curves with regularization
fig = plt.figure()
for i in range(len(loss_lists)):
    plt.plot(np.arange(0, 10000, 50),
             loss_lists[i], label='eta0={}'.format(reg_paras[i]))
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(loc='best')
plt.title("Training Accuracy score of {}% with a learning rate = {} and \u03BB ={} ".format(
    max(Score) * 100, best_rate, best_reg))
plt.show()


# B. Visualizing the Decison Boundary with the best learning rate
cls = SGDClassifier(loss='log', penalty=None, alpha=best_reg,
                    max_iter=nepoch, tol=None, learning_rate='constant', eta0=best_rate)
cls.fit(X, y)
b0, b1, b2 = cls.intercept_, cls.coef_[0][0], cls.coef_[0][1]
x1 = np.linspace(2, 20, 30)
x2 = -b0 / b2 - b1 / b2 * x1

plt.scatter(X[y == 1, 0], X[y == 1, 1], marker='+', c='r', label='Hot Topic')
plt.scatter(X[y == 0, 0], X[y == 0, 1], marker='.', c='b', label='#ofDay')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='best')
plt.plot(x1, x2, color="g", linestyle="--", marker=None)
plt.title('Decision Boundary with \u03BB ={} & learning rate ={} '.format(
    best_reg, best_rate))
plt.show()

######################################    PART TWO. ######################################
############################   Logisttic Regression-Incremental Learning  ################
print("Parameters gathered from Training the data are:\nTraining Score ={}\nLearning Rate ={} \nRegularization Parameter(\u03BB) ={}".format(
    trainScore, best_rate, best_reg))


def getdata(i):
    data = np.loadtxt(i, delimiter=',')
    feature = data[:, :-1]
    label = data[:, -1]
    return feature, label


# K-paramter processing
# Bad model for k =10,15,20,25,30,35,40,45,50,60
for document in files[1:]:
    X, y = getdata(document)
    k = 100
    for i in range(k):
        cls = cls.partial_fit(X, y, classes=np.unique(y))
        cls.fit(X, y)
    pnt = cls.score(X, y)
    # Calculation of SDG
    b0, b1, b2 = cls.intercept_, cls.coef_[0][0], cls.coef_[0][1]
    x1 = np.linspace(2, 20, 30)
    x2 = -b0 / b2 - b1 / b2 * x1

    # Visualize Data with Decision Boundary Line
    plt.figure()
    plt.scatter(X[y == 1, 0], X[y == 1, 1],
                marker='+', c='r', label='Hot Topic')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], marker='.', c='b', label='#ofDay')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend(loc='best')
    plt.plot(x1, x2, color="g", linestyle="--", marker=None)
    plt.title('Training Accuracy Score = {}% with l_rate = {},\u03BB = {}, k = {}'.format(
        pnt * 100, best_rate, best_reg, k))
    plt.show()
