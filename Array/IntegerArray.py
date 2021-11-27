'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Display Integer Array
'''
#########################################################################################
if __name__=='__main__':
    try:
        a=[]  
        # initialize the number of rows
        for i in range(5):
            a+= [0]
        print ("Enter 5 elements in array: ")
        for i in range(5):
            print ("Enter",i+1," element: ")
            a[i]=int(input())
        print("-----------------------")   
        print ("Elements in array : ")
        for i in a:
            print(i)   
        print("-----------------------") 
        print ("Accessing individual element through indexes: ") 
        print(a[0])
        print(a[1])
        print(a[2])
        print(a[3])
        print(a[4])
    except Exception as e:
        print("Error..",e) 