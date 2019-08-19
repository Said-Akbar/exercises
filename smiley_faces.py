# COUNT THE SMILEY FACES.
# description: https://www.codewars.com/kata/count-the-smiley-faces/python
import pandas as pd
def count_smileys(arr):
    arr = pd.Series(arr)
    x=arr.str.contains("[:;][-~]?[)D]") # regex expression to check the smiley
    return sum(x)