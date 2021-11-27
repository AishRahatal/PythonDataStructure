'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Clear set using built in function
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        
        print("-------------------------------------------------")
        print("basket before clear : \n")
        print("Basket (set) : ",basket)
        print()        
        #Remove all elements from the fruits set
        basket.clear()
        print("After clear :\n")
        print("Basket (set) :",basket)

        print("-----------------------------------------------")
    except Exception as e:
        print("Something went wrong :",e)