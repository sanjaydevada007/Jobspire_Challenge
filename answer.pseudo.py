#imort randint to generate random number between 6 and 15
from random import randint
a=raw_input() #ttake input given string

#function to concate the string and random number and to print result
def Naming(s):
    x = str(randint(6,15))
    ans= s+' '+ x
    print ans
    

Naming(a) #function calling
    
