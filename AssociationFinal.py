import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
ds = pd.read_csv("A:\CMPICA\CertificationProgram\\store_data.csv",header = None)

#print(ds)
records = []
for i in range(0, 5):
    records.append([str(ds.values[i,j]) for j in range(0, 5)])
#print(records)

association_rules = apriori(records)
association_results = list(association_rules)

for item in association_results:
    
    pair = item[0] 
    items = [x for x in pair]
    print(pair)
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("=====================================")

    

   
