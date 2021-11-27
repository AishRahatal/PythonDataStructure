'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :  Lower and Upper case in string
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        string=input("Enter a word or a sentence :")

        print("Lower case : ", string.lower())
        print("Upper case : ", string.upper())     
        print()
    except Exception as e:
        print("Error :",e)