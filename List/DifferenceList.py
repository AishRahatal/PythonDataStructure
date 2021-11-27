'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Difference between the two lists.
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
        print(" Difference basket1 and basket2 (lists) :\n")
        temp=[]
        basket=basket1+basket2
        for i in basket:
            if i not in basket1 or i not in basket2:
                temp.append(i)
        print(temp)
        print()     
    except Exception as e:
        print("Error...",e)
