'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Append a list to the second list.
'''
#########################################################################################

if __name__=='__main__':
    try:
        basket1=['Mango','Apple','Banana','Blueberry','Kiwi','Watermelon']
        basket2=["Apple", "Banana", "Cherry","Grapes"]
        print("-------------------------------------------------")
        print("baskets : \n")
        print("Basket1 (list) : ",basket1)
        print()
        print("Basket2 (list) : ",basket2)
        print()
        print(" Append basket1 and basket2 (lists) :\n")
        basket=basket1+basket2
        print("List : ", basket)
        print()  
         
    except Exception as e:
        print("Error...",e)
