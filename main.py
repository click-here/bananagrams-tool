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

bag_of_letters = []

for k, v in dict_of_letters.items():
    bag_of_letters += list((k*v).lower())
    
random.shuffle(bag_of_letters)

first_hand = sorted(bag_of_letters[:15])

joined_hand = ''.join(first_hand)

def get_possible_words_from_letters(letters):
    remove_these_letter = ''.join(set(string.ascii_lowercase) - set(letters))

    df['in-hand'] = df['sorted'].apply(rem_let, args=(remove_these_letter,)).apply(sort_string)

    df[df['in-hand'] == df['sorted']][['words','sorted']]

    all_possible_words = df[df['in-hand']==df['sorted']]['words'].tolist()

    return all_possible_words


all_possible_words = get_possible_words_from_letters(joined_hand)

for word in all_possible_words[:500]:
    print(word)
    remaining_letters = [x for x in joined_hand if x not in word]
    remaining_words = get_possible_words_from_letters(remaining_letters)
    for word2 in remaining_words:
        remaining_letters2 = [x for x in remaining_letters if x not in word2]
        lastwords = get_possible_words_from_letters(remaining_letters2)
        if lastwords == []:
            pass
        else:
            lastword = lastwords[0]
            last_letters = [x for x in remaining_letters2 if x not in lastword]
            print(word, word2, lastword,last_letters)

    
