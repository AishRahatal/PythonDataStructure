'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Create copy of list
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        fruits = ["cherry", "orange", "kiwi", "melon", "mango"] 
        numbers=[22, 4, 68, 9, 3]
        print("List1: ",fruits)
        print()
        print("List2 : ",numbers)
        print()
        temp1=fruits.copy()
        temp2=numbers.copy()
        print("copy of List1: ")
        print(temp1)
        print()
        print("copy of List2: ")
        print(temp2)
        print()    
    except Exception as e:
        print("Error...",e)