'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title :  Create Tuple having with different data type
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("----------------------------------")
        n = int(input("Enter number of elements : "))
        t=[]
        for i in range(n):
            print("Enter ",i+1," element")
            d=input()
            #append() to add element to list
            t.append(d)
        a = tuple(t)         
        print()
        print("tuple : ")
        print(a)     
        print()
             
    except Exception as e:
        print("Error...",e)