'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : multtiply all the items in a list.
'''
#########################################################################################
import math
if __name__=='__main__':
    try:
        print("----------------------------------")
        n = int(input("Enter number of elements : "))
        numbers=[]
        for i in range(n):
            print("Enter ",i+1," number")
            d=int(input())
            #append() to add element to list
            numbers.append(d)
            
        print()
        print("Numbers in list : ")
        print(numbers)     
        print()
        #prod() for multilication of items of list
        mult= math.prod(numbers)
       
        print("Multiplication of all items of list :",mult)      
    except Exception as e:
        print("Error...",e)
        
