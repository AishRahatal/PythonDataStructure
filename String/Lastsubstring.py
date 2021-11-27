'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title : Get the last part of a string before a specified character.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        str1 = 'https://www.w3resource.com/python-exercises/string'
        print(str1.rsplit('/', 1)[0])
        print()
        print(str1.rsplit('-', 1)[0])
        print()
    except Exception as e:
        print("Error :",e)