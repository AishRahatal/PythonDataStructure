'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Remove element from set 
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        print("-------------------------------------------------")
        print("basket(set) before removing : ",basket,)
        print()
        fruit=input("Remove  a fruit from basket:")
        #remove() to remove given element 
        basket.remove(fruit)
        print("Removed fruit :",fruit)
        print("-----------------------------------------------")
        print("basket(set) after removing : ",basket)

        print("------------------------------------------------")
    except:
        print("Please remove correct fruit")