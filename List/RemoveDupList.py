'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Remove duplicates from a list of lists.
'''
#########################################################################################
import itertools
if __name__=='__main__':
    try:
        list1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("-----------------------------")
        print("List: ", list1)
        print()
        list1.sort()
        temp = list(list1 for list1,_ in itertools.groupby(list1))
        print("After removing duplicate:")
        print("List :", temp)
        print()  
         
    except Exception as e:
        print("Error...",e)
