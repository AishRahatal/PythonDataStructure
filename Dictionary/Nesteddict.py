'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Creating nested dictionary 
'''
#########################################################################################

if __name__=='__main__':
    try:
        list = ['a', 'b', 'c', 'd']
        dict = temp = {}
        #creating nested dictionary
        for name in list:
            temp[name] = {}
            temp = temp[name]
        print()
        print("Nested dictionary :")
        print(dict)
    except Exception as e:
        print("Error..",e) 