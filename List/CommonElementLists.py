'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : to find common items from two lists.
'''
#########################################################################################

def CommonElement(basket1,basket2):
    b=[]
    for fruit1 in basket1:
        for fruit2 in basket2:
            if fruit1==fruit2:
                b.append(fruit1)
    print("basket1 and basket2 contain same element:\n")
    print(b)
    print()            
                

if __name__=='__main__':
    try:
        basket1=['Mango','Apple','Banana','Blueberry','Kiwi','Watermelon']
        basket2=["Apple", "Banana", "Cherry","Grapes","Mango"]
        print("-------------------------------------------------")
        print("baskets : \n")
        print("Basket1 (list) : ",basket1)
        print()
        print("Basket2 (list) : ",basket2)
        print()
        CommonElement(basket1,basket2)     
    except Exception as e:
        print("Error...",e)
