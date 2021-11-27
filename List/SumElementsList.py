'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Sum all the items in a list.
'''
#########################################################################################
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
        #sum() to all add items
        sum=sum(numbers) 
        print("Sum of all items of list :",sum)      
    except Exception as e:
        print("Error...",e)
        
