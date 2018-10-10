import pandas as pd
import random
import string
from collections import Counter

def f7(seq): # https://www.peterbe.com/plog/uniqifiers-benchmark
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


dict_of_letters = {"A":13,"B":3,"C":3,"D":6,"E":18,"F":3,"G":4,"H":3,"I":12,"J":2,"K":2,"L":5,"M":3,"N":8,"O":11,"P":3,"Q":2,"R":9,"S":6,"T":9,"U":6,"V":3,"W":3,"X":2,"Y":3,"Z":2}

df = pd.read_csv('EOWL.csv',header=None).dropna()
df.columns = ['words']

wl = df.words.tolist()

wlu = []
for w in wl:
    wlu.append(''.join(f7(w)))


wls = ''.join(wlu)
cnt = Counter()
for l in wls:
    cnt[l] += 1

d={}
for key, value in cnt.items():
    d[key] = value


df2 = pd.DataFrame(list(d.items()),columns=['letter','count'])

df2 = df2.sort_values(by='count',ascending=False)

df2.to_csv('Intersect Freq.csv',index=False)
