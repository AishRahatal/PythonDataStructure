'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :  Reverse String
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        string=input("Enter a word or a sentence :")
        print("Reverse : ", string[::-1]) 
        print()
    except Exception as e:
        print("Error :",e)