from libfun import *
from sklearn.metrics import accuracy_score
from keras.models import Sequential, load_model


x_test, y_test = getNumpyFromCsv('./dataset/new_image.csv', train=False)

def incremental(x_test, y_test):
    model_name = "fulTrainPredCheck_7" + ".sav"
    model = loadModel(model_name)

    y_pred = model.predict(x_test)
    print(f"train accuracy = {accuracy_score(y_test, y_pred)}")

def testFunc(XArray, YArray, median = 0.6):
    regressor = load_model('./LSTM/model/location.keras')
    y_pred = regressor.predict(XArray)
    y_pred = np.array(list(map(lambda x: 1 if x > median else 0, y_pred.flatten())))
    accuracy = accuracy_score(YArray, y_pred)
    print(f"train accuracy = {accuracy}")

testFunc(x_test, y_test, 0.5)