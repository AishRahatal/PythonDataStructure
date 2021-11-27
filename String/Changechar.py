'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :  Change character of string at second occurenece
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        str=input("Enter a word or a sentence :")
        char = str[0]  
        length = len(str)  
        str = str.replace(char, '$')  
        str = char + str[1:]  
        print(str)        
        print()
    except Exception as e:
        print("Error :",e)