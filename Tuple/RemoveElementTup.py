
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Remove an item from a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=('Mango','Orange','Banana','Blueberry','Kiwi')

        print("basket (tuple): ",basket)
        list=list(basket)
        list.remove('Blueberry')
        print()
        basket=tuple(list)
        print("basket After removing: ",basket)
        print()
    except Exception as e:
        print("Error...",e)