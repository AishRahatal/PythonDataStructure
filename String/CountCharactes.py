'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title : Count the number of characters
'''
#########################################################################################
if __name__=='__main__':
    try:
        string=input("Enter a word or a sentence :")
         
        print("----------------------")
        temp={}
        for letter in string:
            if letter in temp:
                temp[letter]+=1
                
            else:
                temp[letter]=1
        print("Count of character string :",temp)
        print()
    except Exception as e:
        print("Error :",e)
