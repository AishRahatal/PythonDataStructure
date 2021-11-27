'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Create frozen set
'''
#########################################################################################
#frozen set is a immutable
if __name__=='__main__':
    try:
        basket1=frozenset([ 'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'])
        basket2=frozenset(["Apple", "Banana", "Cherry","Grapes"])
        #use intersection(). Return similar element. 
        print("------------------------------------------------")
        print("Intersection :",basket1.intersection(basket2))
        print()
        #use difference(). Return a new set with elements in the set that are not in the others.
        print("Difference :",basket1.difference(basket2))
        print()  
        #symmetric difference() Return a set that contains all items from both sets, 
        # except items that are present in both sets
        print("Symmetric Difference :",basket1.symmetric_difference(basket2))        
        print()
        #Union() returns common all items from both sets, duplicates are excluded
        print("Union :",basket1.union(basket2))
        print()
    except Exception as e:
        print("Error..",e)

