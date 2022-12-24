# word counter 
def word_counter(s):
    count={}
    for chr in s:
        count[chr]=s.count(chr)
    return count
print(word_counter("prakash"))