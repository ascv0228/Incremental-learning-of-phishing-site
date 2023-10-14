import pandas as pd
import numpy as np
from random import sample 
import os, sys

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(path)
f1 = pd.read_csv(path + '/normal_database.csv')
f2 = pd.read_csv(path + '/phishing_database.csv')
dfx = {
    "normal" : f1,
    "phishing" : f2
}

col_names = ["Have_IP","Have_At","URL_Length","URL_Depth","Redirection","https_Domain","TinyURL","Prefix/Suffix","DNS_Record","Web_Traffic","Domain_Age","Domain_End","iFrame","Mouse_Over","Right_Click","Web_Forwards","char_number","char_word","char_symbol","Label"]
features = ['URL_Length', 'URL_Depth', 'Web_Traffic', 'Web_Forwards']
# with open("123.txt", 'w') as file:
#     for dfs in dfx:
#         for f in col_names:
#             min = np.min(dfx[dfs].loc[:,f])
#             max = np.max(dfx[dfs].loc[:,f])
#             print(dfs, ": ", f, "max", max, "min", min)
#             print(dfs, ": ", f, "max", max, "min", min, file=file)
#         print("===================================")

dfx = pd.concat([f1, f2], axis=0)
with open("123.txt", 'w') as file:
    for f in features:
        min = np.min(dfx.loc[:,f])
        max = np.max(dfx.loc[:,f])
        print(f, "max", max, "min", min, file=file)


# cols_data_4 = f1.loc[:,'Have_IP'] # 指定連續列，用列名
# print(cols_data_4)
# cols_data_5 = df.iloc[:,0:4] # 指定連續列，用數字