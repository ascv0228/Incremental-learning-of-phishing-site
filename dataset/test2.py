import pandas as pd
import os, sys
p = os.path.abspath(os.path.dirname(sys.argv[0]))
def read_normal_domain():
    path = p + r"/top500Domains.csv"
    f1 = pd.read_csv(path)['Root Domain']
    a = f1.to_list()
    print(a)

read_normal_domain()