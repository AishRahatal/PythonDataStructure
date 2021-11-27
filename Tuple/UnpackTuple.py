
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title :  Unpack a tuple in several variables.
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("----------------------------------")
        fruit=("Orange","C-viatamin",10)
        print("tuple: ",fruit)
        (fruits,viatamin,quantity)=fruit
        print()
        print("Unpacked tuple into variable:")
        print("fruits :",fruits)
        print("viatamin: ",viatamin)
        print("quantity: ",quantity)
        print()
             
    except Exception as e:
        print("Error...",e)