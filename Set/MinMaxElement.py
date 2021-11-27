'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Find maximum and the minimum value in a set
'''
#########################################################################################

if __name__=='__main__':
    try:
        n=int(input('Enter n: '))
        s=set()
        print("----------------------------------------")
        #user input into set using map() and split()
        for i in range(n):
            s= s | set(map(str,input(f'Enter {i+1}rd set: ').split()))
        print("------------------------------")
        print("Set :",s)
        print()
        print("Max element in set :", (max(s)))
        print()
        print("Min element in set :" ,(min(s)))


    except:
        print("Please enter correct")
