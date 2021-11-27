'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Two lists are circularly identical..
'''
#########################################################################################
import numpy
def circular(list1,list2):
    for i in range(len(list1)):
        if list1 == list(numpy.roll(list2, i)): # shift b circularly by i
            return True
    return False
        

if __name__=='__main__':
    try:
        list1=[1, 1, 1, 0, 0]
        list2=[1, 1, 0, 0, 1]
        print("-------------------------------------------------")
        print("List : \n")
        print("list1 (list) : ",list1)
        print()
        print("list2 (list) : ",list2)
        print()
        print("Two lists are circularly identical :")
        f=circular(list1,list2)
        print(f) 
        print()        
    except Exception as e:
        print("Error...",e)
