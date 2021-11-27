''''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Generate all permutations of a list in Python.
'''
#########################################################################################
import itertools


if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        letters = ['a','b','c'] 
        print("List : ",letters)
        print()
        permut=itertools.permutations(letters)
        permutList=list(permut)
        print("Permutations :")
        print(permutList)
        print()    
    except Exception as e:
        print("Error...",e)