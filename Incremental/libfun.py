
import pickle
import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

DomainList = {}

def getNumpyFromCsv(filename, train=True):
    f1 = pd.read_csv(filename)
    DomainList["train" if train else "test"] = f1.iloc[:, 0]
    f1 = f1.iloc[:, 1:]
    a = f1.to_numpy()
    # DomainList.append(list(zip(a[:, 0], a[:, -1])))
    return a[:, :-1], a[:, -1]

def getNumpyFromCsv_all(filename, normal=True):
    f1 = pd.read_csv(filename)
    DomainList["normal" if normal else "phishing"] = f1.iloc[:, 0]
    f1 = f1.iloc[:, 1:]
    a = f1.to_numpy()
    # DomainList.append(list(zip(a[:, 0], a[:, -1])))
    return a[:, :-1], a[:, -1]

def saveModel(filename, model):# save the model to disk
    pickle.dump(model, open(filename, 'wb'))

def loadModel(filename):
    return pickle.load(open(filename, 'rb'))

def fulTrain(model, x_train, y_train, iter=100):
    classes = np.unique(y_train)
    
    for i in range(0, len(x_train), iter):
        if i != 0:
            model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
        else:
            i = iter//2
            model.partial_fit(x_train[:i], y_train[:i], classes=classes)
            model.partial_fit(x_train[i:iter], y_train[i:iter])


def fulTrainPredCheck(model, x_train, y_train, x_test, y_test, iter=100, reTrain=False):
    classes = np.unique(y_train)
    count = 0
    accuracy_pre = 0
    filename = "fulTrainPredCheck" + ".sav"
    reTrainList =[]
    for i in range(0, len(x_train), iter):
        count+=1
        if i != 0:
            model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
        else:
            i = iter//2
            model.partial_fit(x_train[:i], y_train[:i], classes=classes)
            model.partial_fit(x_train[i:iter], y_train[i:iter])

        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Train {count} accuracy: {accuracy}.')
        if accuracy_pre < accuracy:
            accuracy_pre = accuracy
            saveModel(filename, model)
            print("Save ...")
        else:
            if reTrain:
                reTrainList.append((x_train[i:i+iter], y_train[i:i+iter]))
            model = loadModel(filename)
            print("Load ...")
    else:
        if reTrain:
            for i in range(0, len(reTrainList)):
                count+=1
                model.partial_fit(*reTrainList[i])

                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                print(f'Train {count} accuracy: {accuracy}.')
                # if accuracy_pre < accuracy:
                #     accuracy_pre = accuracy
                #     saveModel(filename, model)
                #     print("Save ...")
                # else:
                #     model = loadModel(filename)
                #     print("Load ...")
                accuracy_pre = accuracy
                saveModel(filename, model)
                print("Save ...")
        output_diff("pre_check.txt", y_test, y_pred)
    print(f"Final Accuracy: {accuracy_pre}")
    return model

def fulTrainPred(model, x_train, y_train, x_test, y_test, iter=100):
    classes = np.unique(y_train)
    count = 0
    accuracy = 0
    filename = "fulTrainPred" + ".sav"
    for i in range(0, len(x_train), iter):
        count+=1
        if i != 0:
            model.partial_fit(x_train[i:i+100], y_train[i:i+100])
        else:
            i = iter//2
            model.partial_fit(x_train[:i], y_train[:i], classes=classes)
            model.partial_fit(x_train[i:100], y_train[i:100])

        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Train {count} accuracy: {accuracy}.')
    else:
        output_diff("pre.txt", y_test, y_pred)
        saveModel(filename, model)

    print(f"Final Accuracy: {accuracy}")
    return model

def output_diff(filename, y_test, y_pred, train=False):
    print(len(y_test), len(y_pred), len(DomainList["train" if train else "test"]))
    with open(filename, 'w') as f:
        for index, (first, second) in enumerate(zip(y_test, y_pred)):
            if int(first) != int(second):
                print(index, DomainList["train" if train else "test"][index], first, second, file=f)

def plt_line(x, y):
    pass
