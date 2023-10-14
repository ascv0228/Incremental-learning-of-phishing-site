import pandas as pd
import os, sys
from sklearn.utils import shuffle

def createCombine(df1, df2, n):
    A = pd.DataFrame.sample(df1, n).reset_index(drop=True)
    B = pd.DataFrame.sample(df2, n).reset_index(drop=True)
    return pd.concat([A, B], axis=0)

def createTrainTestData(df1, df2, n):
    A = pd.DataFrame.sample(df1, 2*n).reset_index(drop=True)
    B = pd.DataFrame.sample(df2, 2*n).reset_index(drop=True)
    a1, a2 = A.iloc[:n, :], A.iloc[n:, :]
    b1, b2 = B.iloc[:n, :], B.iloc[n:, :]
    return shuffle(pd.concat([a1, b1], axis=0)), shuffle(pd.concat([a2, b2], axis=0))


path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(path)
# f1 = pd.read_csv(path + '/normal_database.csv')
# f2 = pd.read_csv(path + '/phishing_database.csv')
f1 = pd.read_csv(path + '/normal_image.csv')
f2 = pd.read_csv(path + '/phishing_image.csv')
# print(f1)
trainData, testData = createTrainTestData(f1, f2, 5000)
trainData.to_csv(path + '/' + "trainData.csv", encoding='utf-8', index=False)
testData.to_csv(path + '/' + "testData.csv", encoding='utf-8', index=False)
