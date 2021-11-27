'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Get count of specific element of Array
'''
#########################################################################################

if __name__=='__main__':
    try:
        size=int(input("Enter size of an array: "))
        arr=[]
        print("Enter elements: ")
        for i in range(size):
            print("Enter  " ,i+1, " elements: ")
            element=input()
            #append() will add element to array
            arr.append(element)
        print("-------------------")
        #[::1]Start at the beginning, end when it ends, in steps of 1 
        print(" Array : ",arr[::1],sep="\n")
        element=input("Enter element to get count: ")
        print("-------------------")
        #count() will give occcurence of element
        print("The occurenece of ",element," = ",arr.count(element))
    except Exception as e:
        print("Error..",e)     