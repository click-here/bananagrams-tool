The `Intersect Freq.csv` file was generated in an attempt to understand ways in which words might frequently intersect.
  The thought was to simplify the problem to a single intersection which would be the most common for a human (me!) to see.  If "e's" or any letter have a high intersect 'score' it would be inflated additionally were I not to remove duplicate letters within a word. For example consider the word "keep". I'm only investigating intersection at one word. So if I don't remove one of those "e's" from the word than "e" would be counted twice.  When comparing any 2 words that I'm considering intersection of I do not care how many e's there are since I can only intersect at one point. (for the scope of this investigation)
  
# Some Thoughts

Just looking at `Intersect Freq.csv` has me thinking of a few strategies that I'd like to test.  Since `e` has a high intersect frequency it might seem sensible to play words that contain e's first when starting from a blank slate. On the other hand, if you start with a `q` you may want to play those words first since you won't be limiting yourself to the scope of what's playable based on the first `e` word that you hypothetically played.

# Possible Approaches

1. When a game starts. Survey hand and find letters with lowest frequency. [`q`,`j`...]  From the playable set of words value words that contain high value intersect letters. [This might be something worth pre-processing]

2. 