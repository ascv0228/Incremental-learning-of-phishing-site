import pandas as pd
import numpy as np
from random import sample 
import os, sys

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(path)
f1 = pd.read_csv(path + '/normal_database.csv')
f2 = pd.read_csv(path + '/phishing_database.csv')
df = pd.concat([f1, f2], axis=0)

col_names = ["Have_IP","Have_At","URL_Length","URL_Depth","Redirection","https_Domain","TinyURL","Prefix/Suffix","DNS_Record","Web_Traffic","Domain_Age","Domain_End","iFrame","Mouse_Over","Right_Click","Web_Forwards","char_number","char_word","char_symbol","Label"]
features = ['URL_Length', 'URL_Depth', 'Web_Traffic', 'Web_Forwards']
for f in features:
    min = np.min(df.loc[:,f])
    max = np.max(df.loc[:,f])
    print(f, "max", max, "min", min)
    if(max == min ):
        df[f] = 0
    else:
        df.loc[:,f] = (df.loc[:,f] - min) / (max - min)

df.to_csv(path + "/image.csv", index=False)
df[df['Label'] == 0].to_csv(path + "/normal_image.csv", index=False)
df[df['Label'] == 1].to_csv(path + "/phishing_image.csv", index=False)

# cols_data_4 = f1.loc[:,'Have_IP'] # 指定連續列，用列名
# print(cols_data_4)
# cols_data_5 = df.iloc[:,0:4] # 指定連續列，用數字