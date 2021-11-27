'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Intersect two set 
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket1={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        basket2={"Apple", "Banana", "Cherry","Grapes"}
        print("-------------------------------------------------")
        print("baskets before intersection : \n")
        print("Basket1 (set) : ",basket1)
        print()
        print("Basket2 (set) : ",basket2)
        print()
        
        #intersection() returns common element of two sets 
        fruits= basket1.intersection(basket2)
        print("Common fruits in both baskets :",fruits)
        print("-----------------------------------------------")
    except  Exception as e:
        print("Something went wrong :",e)