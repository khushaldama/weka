import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
df = pd.read_csv('D:\\College\\COLLEGE\\MCA\\MCA SEM-3\\Data Analytics\\practical\\ap\\test.csv', names = ['products'], sep = ',')

print(df.head())
print(df.shape)
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)

df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar[['antecedents','consequents','support', 'confidence']])