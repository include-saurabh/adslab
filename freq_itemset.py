# -*- coding: utf-8 -*-
"""Freq_Itemset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hi4sbgbWEHUYZomaK1mPLj9eguq8NXtH
"""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [['Milk','Onion', 'Bread','Eggs','Yoghurt'],
           ['Milk', 'Fish','Onion','Bread','Eggs','Yoghurt'],
           ['Milk', 'Apples', 'Kidney Beans’, ‘Eggs'],
           ['Milk', 'Sugar', 'Tea Leaves', 'Yoghurt'],
           ['Tea Leaves','Onion', 'Ice cream', 'Eggs'],
          ]
          
tr = TransactionEncoder()
tr_arr = tr.fit(dataset).transform(dataset)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
df

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.5, use_colnames = True)
frequent_itemsets

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [['Milk','Onion', 'Bread','Eggs','Yoghurt'],
           ['Milk', 'Fish','Onion','Bread','Eggs','Yoghurt'],
           ['Milk', 'Apples', 'Kidney Beans’, ‘Eggs'],
           ['Milk', 'Sugar', 'Tea Leaves', 'Yoghurt'],
           ['Tea Leaves','Onion', 'Ice cream', 'Eggs'],
          ]
          
tr = TransactionEncoder()
tr_arr = tr.fit(dataset).transform(dataset)
df = pd.DataFrame(tr_arr, columns=tr.columns_)
df

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.5, use_colnames = True)
frequent_itemsets

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
rules