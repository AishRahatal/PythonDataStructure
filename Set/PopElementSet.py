'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Remove element from set itself
'''
#########################################################################################

if __name__=='__main__':
    #Set() 
    try:
        basket={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        print("-------------------------------------------------")
        print("basket(set) before removing : ",basket,)
        print()
        
        #pop() to remove element to set it does not allow argument
        fruit=basket.pop()
        print("Removed fruit :",fruit)
        print("-----------------------------------------------")
        print("basket(set) after removing : ",basket)

        print("------------------------------------------------")
    except Exception as e:    
        print("Something went wrong :",e)