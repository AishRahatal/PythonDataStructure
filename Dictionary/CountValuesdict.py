'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Count values of dictionary
'''
#########################################################################################
if __name__=='__main__':
    try:
        basket = {'mango':40, 'banana':10, 'cherry':20 , 'apple': 30}

        print("------------------")
        print("Dictionary  values: ")
        count=0
        for fruit in basket.values():
            count=count+1

        print("Count of values in dictionary :",count)
        print() 
    except Exception as e:
        print("Error..",e) 