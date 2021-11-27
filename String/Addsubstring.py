'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :  Cncatenate string
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        string=input("Enter a word or a sentence :")
        s="ing"
        s1="ly"
        if len(string)>=3 and s not in string:
            str1=string+s
            print(str1)
        elif len(string)>=3 and s in string: 
            str2=string+s1
            print(str2)
 
        else:
            print("Please give longer word")     
        print()
    except Exception as e:
        print("Error :",e)