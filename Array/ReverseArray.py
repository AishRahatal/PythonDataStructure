'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Reverse Array
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
            arr.append(element)
        print("-------------------")
        #[::1]Start at the beginning, end when it ends, in steps of 1 
        print(" Array : ",arr[::1],sep="\n")
        print()
        #[::1]Start at the end, stop when it ends, in steps of 1 
        print("Rverese array: ",arr[::-1],sep="\n")
    except Exception as e:
        print("Error..",e)     
