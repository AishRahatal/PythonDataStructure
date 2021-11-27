'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Remove an element from dictionary 
'''
#########################################################################################
if __name__=='__main__':
    try:
        basket = {'mango':40, 'banana':10, 'cherry':20 , 'apple': 30}
        fruit={}
        fruit=basket.pop('mango')
        print()
        print("Dictionary after removing element : ",basket)
        print()
    except Exception as e:
        print("Error..",e) 

