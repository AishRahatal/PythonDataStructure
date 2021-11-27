'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : create dictionary from a string
'''
#########################################################################################
if __name__=='__main__':
    try:
        string = input("Enter a word :") 
        dict = {}
        for char in string:
            dict[char] = dict.get(char, 0)+1 
        print(dict)
    except Exception as e:
        print("Error..",e) 

