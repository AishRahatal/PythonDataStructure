'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : a list, sorted in increasing order by the last
        element in each tuple from a given list.
'''
#########################################################################################

if __name__=='__main__':
    try:
        list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        print("-----------------------------------------------------") 
        print("Before sort :",list)
        print()
        #lambada function to sort list
        list.sort(key = lambda x: x[-1])
        print(" Sorted List : ",list)
        print()
    except Exception as e:
        print("Error...",e)