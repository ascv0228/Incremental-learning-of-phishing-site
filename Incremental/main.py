from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from libfun import *


x_train, y_train = getNumpyFromCsv('./dataset/trainData.csv')
x_test, y_test = getNumpyFromCsv('./dataset/testData.csv', train=False)

sgd = SGDClassifier(loss='log_loss')
#11111111111111111111111111111111111111111111#

classes = np.unique(y_train)
x_normal, y_normal = getNumpyFromCsv_all('./dataset/normal_image.csv', normal=True)
x_phishing, y_phishing = getNumpyFromCsv_all('./dataset/phishing_image.csv')
temp_dict = {'test':[], 'normal': [], 'phishing': []}
iter = 100
for i in range(0, len(x_train), iter):
    if i != 0:
        sgd.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
    else:
        i = iter//2
        sgd.partial_fit(x_train[:i], y_train[:i], classes=classes)
        sgd.partial_fit(x_train[i:iter], y_train[i:iter])
    
    y_pred = sgd.predict(x_test)
    temp_dict['test'].append(accuracy_score(y_test, y_pred))
    
    y_pred = sgd.predict(x_normal)
    temp_dict['normal'].append(accuracy_score(y_normal, y_pred))

    y_pred = sgd.predict(x_phishing)
    temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))

x = range(len(temp_dict['test']))
plt.plot(x, temp_dict['test'], 'r') 
plt.plot(x, temp_dict['normal'], 'g') 
plt.plot(x, temp_dict['phishing'], 'b') 
plt.show()


# fulTrain(sgd, x_train, y_train)
# y_pred = sgd.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Test accuracy: {accuracy}')
####################################################
# print("Train 1")
# fulTrainPred(SGDClassifier(loss='log_loss'), x_train, y_train, x_test, y_test)

# print("\n\n=====================\n\n")
# print("Train 2")
# fulTrainPredCheck(SGDClassifier(loss='log_loss'), x_train, y_train, x_test, y_test)


# print("\n\n=====================\n\n")
# print("Train 3")
# sgd = SGDClassifier(loss='log_loss')
# sgd.fit(x_train, y_train)
# # model = fulTrainPredCheck(sgd, x_train, y_train, x_train, y_train, reTrain=True)
# model = fulTrainPred(sgd, x_train, y_train, x_test, y_test)
# model = sgd
# y_pred = model.predict(x_train)
# accuracy = accuracy_score(y_train, y_pred)
# print(f'Train accuracy: {accuracy}.')
# output_diff("train_diff.txt", y_train, y_pred)
# print("\n\n=====================\n\n")
# # model.fit(x_train, y_train)
# # y_pred = model.predict(x_test)
# # accuracy = accuracy_score(y_test, y_pred)
# # print(f'Train accuracy: {accuracy}.')

# f1 = pd.read_csv('./dataset/trainData.csv')

# ===================
# model = loadModel("fulTrainPred.sav")
# my_list = [[0,0,0.06315789473684211,0,0,0,0,0,0,1.0,1,1,1,1,1,0.058823529411764705,0.5,0.3125,0.1875]]
# a = np.array(my_list, dtype='float32')
# print(model.predict(a))

