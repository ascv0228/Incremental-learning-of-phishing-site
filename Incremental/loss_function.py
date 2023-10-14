from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from libfun import *

lossFunction = ['hinge','log_loss', 'modified_huber', 'squared_hinge', 'perceptron'
                ]

cnt = 20

x_train, y_train = getNumpyFromCsv('./dataset/trainData_2.csv')
x_test, y_test = getNumpyFromCsv('./dataset/testData_2.csv', train=False)
x_normal, y_normal = getNumpyFromCsv_all('./dataset/normal_image_2.csv', normal=True)
x_phishing, y_phishing = getNumpyFromCsv_all('./dataset/phishing_image_2.csv')
x_new, y_new = getNumpyFromCsv_all('./dataset/new_image_2.csv')
temp_dict = {'test':[], 'normal': [], 'phishing': []}
loss_dict = {}
for l in lossFunction:
    loss_dict[l] = {}
    for t in ['test', 'normal', 'phishing']:
        loss_dict[l][t] = []

print (loss_dict)
for l in lossFunction:
    print(l, "Start....")
    for _ in range(cnt):
        sgd = SGDClassifier(loss=l, max_iter=1000)
        sgd.fit(x_train, y_train)

        y_pred = sgd.predict(x_test)
        loss_dict[l]['test'].append(accuracy_score(y_test, y_pred))
        y_pred = sgd.predict(x_normal)
        loss_dict[l]['normal'].append(accuracy_score(y_normal, y_pred))
        y_pred = sgd.predict(x_phishing)
        loss_dict[l]['phishing'].append(accuracy_score(y_phishing, y_pred))
    print(l, "Finish")

x = range(1, cnt+1)
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for t in ['test', 'normal', 'phishing']:
    for i in range(len(lossFunction)):
        plt.plot(x, loss_dict[lossFunction[i]][t], color[i]) 

    plt.legend(lossFunction,loc=4)
    plt.title(
    t,
    )
    plt.show()

