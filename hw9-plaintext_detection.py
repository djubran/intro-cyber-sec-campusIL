""""

Implement heuristic plaintext detection using frequency analysis:

Implement a function is_english that:

Receives a string
Makes sure it consists of only ASCII characters (using the provided is_ascii() function)
Counts the 3 most frequent letters in it
Makes sure they're one of the 6 most frequent letters in English (e, t, a, o, i, n)

""""
from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if not is_ascii(s):
        return False
    s_lower=s.lower()
    # loop for all characters and remove non alphabet chars
    for x in s:
        if not x.isalpha():
            s = s.replace(x,'')
    s_lower=s.lower()
    histogram=[0]*27
    s_list=list(s_lower)
    for char in s_list:
        histogram[ord(char)-ord('a')]=histogram[ord(char)-ord('a')]+1
        
    #find biggest 3 and set them to negative number so we avoid them later
    biggest=max(histogram)
    biggest_index=histogram.index(biggest)
    histogram[biggest_index]=-1
    bigger=max(histogram)
    bigger_index=histogram.index(bigger)
    histogram[bigger_index]=-1
    big=max(histogram)
    big_index=histogram.index(big)
    histogram[big_index]=-1
  
    x=chr(big_index+97)
    y=chr(bigger_index+97)
    z=chr(biggest_index+97)
    most_common=set([x,y,z])
    return most_common.issubset(set(['e', 't', 'a', 'o', 'i', 'n']))
            
