'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title :  Calculate the length of a string.
'''
#########################################################################################
if __name__=='__main__':
    try:
        string=input("Enter a word or a sentence :")
        length=len(string)
        print("----------------------")
        print("Length of '"+string+"' : ",length)
        print()
    except Exception as e:
        print("Error :",e)
