'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : function that takes two lists and returns True if they have at
            least one common member.
'''
#########################################################################################

def CommonElement(basket1,basket2):
    for fruit1 in basket1:
        for fruit2 in basket2:
            if fruit1==fruit2:
                return True

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
        check=CommonElement(basket1,basket2)
        print(" basket1 and basket2 contain same element:")
        print(check)
          
    except Exception as e:
        print("Error...",e)
