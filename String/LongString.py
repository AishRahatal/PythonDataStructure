'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title : Find longest word in sentence
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        string ="Nature is the endless expanse of life forms beauty resources peace and nourishment"
        print("string : ",string)
        print()
        str=list(string.split(" "))
        sort=sorted(str, key=len)
        print("Long Word: ", sort[-1])
        print()    
    except Exception as e:
        print("Error...",e)
        
