
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title :  Create the colon of a tuple.
'''
#########################################################################################
from copy import deepcopy
if __name__=='__main__':
    try:
        print("----------------------------------")
        fruit=('Mango','Apple',[],'Banana')
        print("tuple: ",fruit)
        print()
        #create copy using deepcopy()
        fruit_clone=deepcopy(fruit)
        fruit_clone[2].append('Berry')
        print("Updated tuple clone:")
        print(fruit_clone)
        print("original tuple:")
        print(fruit)
        print()
             
    except Exception as e:
        print("Error...",e)