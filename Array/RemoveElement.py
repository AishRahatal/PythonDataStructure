'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Remove first element of Array
'''
#########################################################################################

if __name__=='__main__':
    #Taking user input
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
        element=input("Enter element to remove: ")
        # remove() will remove first occurence of element
        arr.remove(element)
        print("-------------------")
        print(" Array after removing element  : ",arr[::1],sep="\n")
    except Exception as e:
        print("Error..",e) 