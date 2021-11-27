'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : To iterate over dictionaries using for loops.
'''
#########################################################################################

if __name__=='__main__':
    try:
        basket = {'mango':40, 'banana':10, 'cherry':20 , 'apple': 30}
        print("------------------")
        print("Dictionary Elements: ")
        #for loop to get keys without using .keys()
        for fruit in basket:
            print(fruit)
        print()
        print("------------------")
        print("Dictionary  keys: ")
        #for loop to get keys using .keys()
        for fruit in basket.keys():
            print(fruit)
        print()

        print("------------------")
        print("Dictionary  values: ")
        #for loop to get values using .values()
        for fruit in basket.values():
            print(fruit)
        print()
        print("------------------")
        print("Dictionary keys and values: ")
        #for loop to get keys and values using .items()
        for fruit ,quantity in basket.items():
            print(fruit,quantity)
        print()
    except Exception as e:
        print("Error..",e)    

