'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Remove duplicate from list
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("----------------------------------")
        n = int(input("Enter number of elements : "))
        temp=[]
        for i in range(n):
            print("Enter ",i+1," number")
            d=input()
            #append() to add element to temp
            temp.append(d)
            
        print()
        print("Items in temp : ")
        print(temp)     
        print()
        #removing duplicate items using set()
        r=list(set(temp))
        print("After removing duplicates :",r)      
    except Exception as e:
        print("Error...",e)