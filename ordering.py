# Ordering the sentences
# description: https://www.codewars.com/kata/your-order-please/python
def order(sentence):
  if not sentence: return ""
  words = sentence.split()
  dict_w = {}
  for i in words:
      dig = [d for d in list(i) if d.isdigit()] 
      dict_w[dig[0]]=i
  final = ''
  for i in sorted(dict_w):
    final += (dict_w[i])+' '  
  return final[:-1]