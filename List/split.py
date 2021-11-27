'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : split a list based on first character of word.
'''
#########################################################################################
from itertools import groupby
from operator import itemgetter
if __name__=='__main__':
    try:
        basket=['Mango','Apple','Banana','Blueberry','Kiwi','Watermelon']
        print("-----------------------------------")
        for letter, words in groupby(sorted(basket), key=itemgetter(0)):
            print (letter)
            for word in words:
                print(word)
                print("---------------")
        print()  
         
    except Exception as e:
        print("Error...",e)
