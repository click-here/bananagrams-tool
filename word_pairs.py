import pandas as pd
import random
import string

def in_joined_hand(row, joined_hand):
    return row in joined_hand

def sort_string(row):
    return ''.join(sorted(row))

def rem_let(row, joined_hand):
    return ''.join(set(row) - set(joined_hand))


dict_of_letters = {"A":13,"B":3,"C":3,"D":6,"E":18,"F":3,"G":4,"H":3,"I":12,"J":2,"K":2,"L":5,"M":3,"N":8,"O":11,"P":3,"Q":2,"R":9,"S":6,"T":9,"U":6,"V":3,"W":3,"X":2,"Y":3,"Z":2}

df = pd.read_csv('EOWL.csv',header=None).dropna()
df.columns = ['words']
df['sorted'] = df['words'].apply(sort_string)


joined_hand = 'hstieeeifuxarai'

def get_possible_words_from_letters(letters):
    remove_these_letter = ''.join(set(string.ascii_lowercase) - set(letters))

    df['in-hand'] = df['sorted'].apply(rem_let, args=(remove_these_letter,)).apply(sort_string)

    df[df['in-hand'] == df['sorted']][['words','sorted']]

    all_possible_words = df[df['in-hand']==df['sorted']]['words'].tolist()

    return all_possible_words


all_possible_words = get_possible_words_from_letters(joined_hand)

df = pd.DataFrame({'words':all_possible_words})

test_word = 'wired'

four_letters_and_up = [x for x in all_possible_words if len(x)>3]

t = []
for test_word in four_letters_and_up:
    for w in four_letters_and_up:
        if len(test_word) > len(w):
            r = set(test_word) - set(w)
        else:
            r = set(w)- set(test_word)
        max_len = max(len(set(w)),len(set(test_word)))
        if len(r) == max_len - 1:
            t.append([w, test_word])

        
df = pd.DataFrame(t[1:],columns=['w1','w2'])

df['joined_len'] = df['w1'].str.len() + df['w2'].str.len()

df_wordpairs = df.sort_values(by='joined_len',ascending=False)
