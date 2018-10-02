import pandas as pd
import random

dict_of_letters = {"A":13,"B":3,"C":3,"D":6,"E":18,"F":3,"G":4,"H":3,"I":12,"J":2,"K":2,"L":5,"M":3,"N":8,"O":11,"P":3,"Q":2,"R":9,"S":6,"T":9,"U":6,"V":3,"W":3,"X":2,"Y":3,"Z":2}


def in_joined_hand(row, joined_hand):
    return row in joined_hand

def sort_string(row):
    return ''.join(sorted(row))


df = pd.read_csv('EOWL.csv',header=None).dropna()

df.columns = ['words']
df['sorted'] = df['words'].apply(sort_string)


hands = []

def play_hand():
    bag_of_letters = []

    for k, v in dict_of_letters.items():
        bag_of_letters += list((k*v).lower())
        
    random.shuffle(bag_of_letters)

    first_hand = sorted(bag_of_letters[:15])

    joined_hand = ''.join(first_hand)

    ##df['sorted-hash'] = df['sorted'].apply(hash)

    df['in-hand'] = df['sorted'].apply(in_joined_hand, args=(joined_hand,))

    df[df['in-hand']==True][['words','sorted']]

    return df[df['in-hand']==True]['words'].tolist()

for i in range(1000):
    hands += play_hand()

hands_df = pd.DataFrame({'WordsPlayed':hands})

grouped_df = hands_df.groupby('WordsPlayed')['WordsPlayed'].count().sort_values(ascending=False).to_frame()

grouped_df.columns = ['Count']

grouped_df = grouped_df.reset_index()

grouped_df['len'] = grouped_df['WordsPlayed'].str.len()

grouped_df[grouped_df['len']>=4]
