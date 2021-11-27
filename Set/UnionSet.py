'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Union of  two set 
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket1={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        basket2={"Apple", "Banana", "Cherry","Grapes"}
        print("-------------------------------------------------")
        print("baskets before Union : \n")
        print("Basket1 (set) : ",basket1)
        print()
        print("Basket2 (set) : ",basket2)
        print()
        
        #Union() returns common all items from both sets, duplicates are excluded 
        Basket= basket1.union(basket2)
        print("After Union :\n")
        print("Basket (set) :",Basket)

        print("-----------------------------------------------")
    except Exception as e:
        print("Something went wrong :",e)