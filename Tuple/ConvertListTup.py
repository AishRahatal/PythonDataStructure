
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Convert a list to a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=['Mango','Kiwi','Banana','Blueberry','Orange','Berry']
        print("basket (list) : ",basket)
        print()
        print("basket (tuple): ",tuple(basket))
        
        print()
    except Exception as e:
        print("Error...",e)