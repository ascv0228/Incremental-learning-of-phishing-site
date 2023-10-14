from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from libfun import *


x_train, y_train = getNumpyFromCsv('./dataset/trainData_2.csv')
x_test, y_test = getNumpyFromCsv('./dataset/testData_2.csv', train=False)
x_normal, y_normal = getNumpyFromCsv_all('./dataset/normal_image_2.csv', normal=True)
x_phishing, y_phishing = getNumpyFromCsv_all('./dataset/phishing_image_2.csv')
x_new, y_new = getNumpyFromCsv_all('./dataset/new_image_2.csv')
temp_dict = {'test':[], 'normal': [], 'phishing': [], 'new': []}

sgd = SGDClassifier(loss='log_loss', max_iter=1000)
sgd.fit(x_train, y_train)
#11111111111111111111111111111111111111111111#

# classes = np.unique(y_train)
# iter = 100
# model=sgd
# for _ in range(10):
#     for i in range(0, len(x_train), iter):
#         if i != 0:
#             model.partial_fit(x_train[i:i+iter], y_train[i:i+iter])
#         else:
#             i = iter//2
#             model.partial_fit(x_train[:i], y_train[:i], classes=classes)
#             model.partial_fit(x_train[i:iter], y_train[i:iter])
        
#         y_pred = model.predict(x_test)
#         temp_dict['test'].append(accuracy_score(y_test, y_pred))
        
#         y_pred = model.predict(x_normal)
#         temp_dict['normal'].append(accuracy_score(y_normal, y_pred))

#         y_pred = model.predict(x_phishing)
#         temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))
# else:
#     for k in temp_dict:
#         if len(temp_dict[k]) > 100:
#             temp_dict[k] = temp_dict[k][-100:]

# ac_list = [temp_dict['test'][-1], temp_dict['normal'][-1], temp_dict['phishing'][-1]]
#11111111111111111111111111111111111111111111#
#22222222222222222222222222222222222222222222#

# classes = np.unique(y_train)
# iter = 100
# count = 0
# accuracy_pre = 0
# model=sgd
# filename = "fulTrainPredCheck_5" + ".sav"
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
# filename = "fulTrainPredCheck_6" + ".sav"
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
#     print(f'accuracy: {accuracy_score(y_test, y_pred)}.')
#     y_pred = model.predict(x_normal)
#     temp_dict['normal'] += [accuracy_score(y_normal, y_pred)]*10
#     y_pred = model.predict(x_phishing)
#     temp_dict['phishing'] += [accuracy_score(y_phishing, y_pred)]*10
#33333333333333333333333333333333333333333333#
#77777777777777777777777777777777777777777777#

classes = np.unique(y_train)
trainData = [x_train, y_train]
iter = 50
count = 0
accuracy_pre = 0
ac_list = []
model=sgd
filename = "fulTrainPredCheck_7" + ".sav"
best_count = 0
for _ in range(1):
    for i in range(0, len(trainData[0]), iter):
        count+=1
        if i != 0:
            model.partial_fit(trainData[0][i:i+iter], trainData[1][i:i+iter])
        else:
            i = iter//2
            model.partial_fit(trainData[0][:i], trainData[1][:i], classes=classes)
            model.partial_fit(trainData[0][i:iter], trainData[1][i:iter])
        y_pred = model.predict(x_phishing)
        accuracy = accuracy_score(y_phishing, y_pred)

        y_pred = model.predict(x_test)
        temp_dict['test'].append(accuracy_score(y_test, y_pred))
        y_pred = model.predict(x_normal)
        temp_dict['normal'].append(accuracy_score(y_normal, y_pred))
        y_pred = model.predict(x_phishing)
        temp_dict['phishing'].append(accuracy_score(y_phishing, y_pred))
        y_pred = model.predict(x_new)
        temp_dict['new'].append(accuracy_score(y_new, y_pred))
        print(f'Train {count} accuracy: {accuracy}.')
        if accuracy_pre < accuracy and temp_dict['normal'][-1] > 0.75:
            accuracy_pre = accuracy
            best_count = count - 1
        saveModel(filename, model)
        print("Save ...")
        ac_list = [temp_dict['test'][-1], temp_dict['normal'][-1], temp_dict['phishing'][-1], temp_dict['new'][-1]]
        
else:
    model = loadModel(filename)
    
    y_pred = model.predict(x_test)
    temp_dict['test'] += [accuracy_score(y_test, y_pred)]*10
    y_pred = model.predict(x_normal)
    temp_dict['normal'] += [accuracy_score(y_normal, y_pred)]*10
    y_pred = model.predict(x_phishing)
    temp_dict['phishing'] += [accuracy_score(y_phishing, y_pred)]*10
    y_pred = model.predict(x_new)
    temp_dict['new'] += [accuracy_score(y_new, y_pred)]*10
    print(f'accuracy: {temp_dict["test"][-1]}.')

# for s in temp_dict:
#     temp_dict[s] = temp_dict[s][-100:]

print(temp_dict['test'][:-10])
print(temp_dict['normal'][:-10])
print(temp_dict['phishing'][:-10])
print(best_count +1 )
print(ac_list)
x = range(len(temp_dict['test'])-10)
plt.plot(x, temp_dict['test'][:-10], 'r') 
plt.plot(x, temp_dict['normal'][:-10], 'g') 
plt.plot(x, temp_dict['phishing'][:-10], 'b') 
plt.plot(x, temp_dict['new'][:-10], 'k') 

plt.legend([f'test-{"{:.{}f}".format(ac_list[0]*100, 2)}%',
            f'normal-{"{:.{}f}".format(ac_list[1]*100, 2)}%',
            f'phishing-{"{:.{}f}".format(ac_list[2]*100, 2)}%',
            f'new-{"{:.{}f}".format(ac_list[3]*100, 2)}%',
            ],loc=4)
plt.axvline(x=best_count, color='r', linestyle='--')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.show()