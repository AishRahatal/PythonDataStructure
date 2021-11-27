'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Symmetric Difference of set 
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket1={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        basket2={"Apple", "Banana", "Cherry","Grapes"}
        print("-------------------------------------------------")
        print("baskets before Symmetric Difference : \n")
        print("Basket1 (set) : ",basket1)
        print()
        print("Basket2 (set) : ",basket2)
        print()
        
        #symmetric difference() Return a set that contains all items from both sets, 
        # except items that are present in both sets
        Basket= basket1.symmetric_difference(basket2)
        print("After Symmetric Difference :\n")
        print("Basket (set) :",Basket)

        print("-----------------------------------------------")
    except Exception as e:
        print("Something went wrong :",e)