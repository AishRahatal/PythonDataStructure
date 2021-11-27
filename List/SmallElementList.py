'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : multtiply all the items in a list.
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
        numbers=[22, 4, 68, 9, 3]
        print("List : ",fruit)
        print()
        print("List: ",numbers)
        print()
        print("Small element of list: ", (min(fruit)))
        print()
        print("Small element of list: ", (min(numbers)))
        print()    
    except Exception as e:
        print("Error...",e)
        
