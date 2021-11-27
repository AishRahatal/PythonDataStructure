
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Find the repeated items of a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=('Mango','Kiwi','Banana','Blueberry','Kiwi','Blueberry')
        print("basket: ",basket)
        print()
        #count() Returns the number of times a specified value occurs in a tuple
        print("There 'Kiwi' in basket are :",basket.count('Kiwi'))
        print("There 'Mango' in basket are :",basket.count('Mango'))
        print()
    except Exception as e:
        print("Error...",e)