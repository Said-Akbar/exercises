# String reversing the case and words order
# Description: https://www.codewars.com/kata/string-transformer/python
def string_transformer(s):
    if not s: return ""
    lists = s.replace(' ','_').split('_') # replace spaces with _ so that split makes one more element for extra spaces
    word =''
    list2=[]
    
    for i in lists: # reverse case for each string 
      for c in i:
        if c.isupper(): word += c.lower()
        elif c.islower(): word += c.upper()
      list2.append(word)
      word=''
      
    for i in list2[::-1]: # create the output
      word += i + ' '
    
    return word[:-1]