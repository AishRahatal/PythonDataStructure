'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Difference between two set using built in function
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket1={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        basket2={"Apple", "Banana", "Cherry","Grapes"}
        print("-------------------------------------------------")
        print("baskets before Difference : \n")
        print("Basket1 (set) : ",basket1)
        print()
        print("Basket2 (set) : ",basket2)
        print()
        
        #Difference() Return a set that contains the items that only exist in set 1, and not in set 2 
        Basket= basket1.difference(basket2)
        print("After Difference :\n")
        print("Basket (set) :",Basket)

        print("-----------------------------------------------")
    except Exception as e:
        print("Something went wrong :",e)