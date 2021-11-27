'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :Count occurrences of a substring in a string.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        string ="Nature is the endless expanse of life forms beauty resources peace and nourishment"
        print("string : ",string)
        print()

        print("count occurrences of a substring in a string : ", string.count('is'))  
        print()
    except Exception as e:
        print("Error :",e)