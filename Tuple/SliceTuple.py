
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Slice a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=('Mango','Orange','Banana','Blueberry','Kiwi','Watermelon')
        print("basket (tuple): ",basket)
        print()
        print("basket After slicing : ")
        print(basket[:3])
        print(basket[:-4])
        print(basket[1:5])
        print()
    except Exception as e:
        print("Error...",e)