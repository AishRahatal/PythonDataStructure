
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Revrse a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=('Mango','Orange','Banana','Blueberry','Kiwi','Watermelon')
        print("basket (tuple): ",basket)
        print()
        print("Reverse Tuple : ")
        print(basket[::-1])
        print()
    except Exception as e:
        print("Error...",e)