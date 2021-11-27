'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title :  Add element to set
'''
#########################################################################################

if __name__=='__main__':
    try:
        basket={'Mango','Apple','Banana','Blueberry'}
        print("-------------------------------------------------")
        print("basket(set) before adding : ",basket,)
        print()
        fruit=input("Add  a fruit to a basket:")
        #add() to add element to set
        basket.add(fruit)
        print("-----------------------------------------------")
        print("basket(set) after adding : ",basket)

        print("------------------------------------------------")
    except Exception as e:
        print("Please put correct fruit ...",e)