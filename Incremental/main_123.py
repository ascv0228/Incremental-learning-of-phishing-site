from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from libfun import *


x_train, y_train = getNumpyFromCsv('./dataset/trainData.csv')
x_test, y_test = getNumpyFromCsv('./dataset/testData.csv', train=False)
x_normal, y_normal = getNumpyFromCsv_all('./dataset/normal_image.csv', normal=True)
x_phishing, y_phishing = getNumpyFromCsv_all('./dataset/phishing_image.csv')
temp_dict = {'test':[], 'normal': [], 'phishing': []}

sgd = SGDClassifier(loss='log_loss')
#11111111111111111111111111111111111111111111#

classes = np.unique(y_train)
iter = 100
model=sgd
for _ in range(15):
    for i in range(0, len(x_train), iter):
        if i != 0:
            model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
        else:
            i = iter//2
            model.partial_fit(x_train[:i], y_train[:i], classes=classes)
            model.partial_fit(x_train[i:iter], y_train[i:iter])
        
        y_pred = model.predict(x_test)
        temp_dict['test'].append(accuracy_score(y_test, y_pred))
        
        y_pred = model.predict(x_normal)
        temp_dict['normal'].append(accuracy_score(y_normal, y_pred))

        y_pred = model.predict(x_phishing)
        temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))


#11111111111111111111111111111111111111111111#
#22222222222222222222222222222222222222222222#

# classes = np.unique(y_train)
# iter = 100
# count = 0
# accuracy_pre = 0
# model=sgd
# filename = "fulTrainPredCheck_2" + ".sav"
# for i in range(0, len(x_train), iter):
#     count+=1
#     if i != 0:
#         model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
#     else:
#         i = iter//2
#         model.partial_fit(x_train[:i], y_train[:i], classes=classes)
#         model.partial_fit(x_train[i:iter], y_train[i:iter])
#     y_pred = model.predict(x_test)
#     accuracy = accuracy_score(y_test, y_pred)

#     print(f'Train {count} accuracy: {accuracy}.')
#     if accuracy_pre < accuracy:
#         accuracy_pre = accuracy
#         saveModel(filename, model)
#         print("Save ...")
#     else:
#         model = loadModel(filename)
#         print("Load ...")
        
#     y_pred = model.predict(x_test)
#     temp_dict['test'].append(accuracy_score(y_test, y_pred))
#     y_pred = model.predict(x_normal)
#     temp_dict['normal'].append(accuracy_score(y_normal, y_pred))
#     y_pred = model.predict(x_phishing)
#     temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))


#22222222222222222222222222222222222222222222#
#33333333333333333333333333333333333333333333#

# classes = np.unique(y_train)
# iter = 100
# count = 0
# accuracy_pre = 0
# model=sgd
# filename = "fulTrainPredCheck_3" + ".sav"
# for i in range(0, len(x_train), iter):
#     count+=1
#     if i != 0:
#         model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
#     else:
#         i = iter//2
#         model.partial_fit(x_train[:i], y_train[:i], classes=classes)
#         model.partial_fit(x_train[i:iter], y_train[i:iter])
#     y_pred = model.predict(x_test)
#     accuracy = accuracy_score(y_test, y_pred)

#     print(f'Train {count} accuracy: {accuracy}.')
#     if accuracy_pre < accuracy:
#         accuracy_pre = accuracy
#         saveModel(filename, model)
#         print("Save ...")
        
#     y_pred = model.predict(x_test)
#     temp_dict['test'].append(accuracy_score(y_test, y_pred))
#     y_pred = model.predict(x_normal)
#     temp_dict['normal'].append(accuracy_score(y_normal, y_pred))
#     y_pred = model.predict(x_phishing)
#     temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))
# else:
#     model = loadModel(filename)
    
#     y_pred = model.predict(x_test)
#     temp_dict['test'] += [accuracy_score(y_test, y_pred)]*10
#     y_pred = model.predict(x_normal)
#     temp_dict['normal'] += [accuracy_score(y_normal, y_pred)]*10
#     y_pred = model.predict(x_phishing)
#     temp_dict['phishing'] += [accuracy_score(y_phishing, y_pred)]*10

#33333333333333333333333333333333333333333333#


for s in temp_dict:
    temp_dict[s] = temp_dict[s][-100:]



x = range(len(temp_dict['test']))
plt.plot(x, temp_dict['test'], 'r') 
plt.plot(x, temp_dict['normal'], 'g') 
plt.plot(x, temp_dict['phishing'], 'b') 
plt.legend(['test','normal','phishing'],loc=4)
plt.show()

