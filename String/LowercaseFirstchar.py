'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title :lowercase first n characters in a string
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        string ="Nature is the endless expanse of life forms beauty resources peace and nourishment"
        print("string : ",string)
        print()
        s=string[0].lower()+string[1:]
        print("string : ",s)
        print()    
    except Exception as e:
        print("Error...",e)
        
