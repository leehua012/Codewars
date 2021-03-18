# Instructions
"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""

# Solutions
def descending_order(num):
    ''' 1: convert int to str
        2: use list comprehension to split number into single digits
        3: sort the list in reverse order
        4: join into single number again
        5: convert str into int
    '''
    return int("".join(sorted([i for i in str(num)],reverse=True)))
