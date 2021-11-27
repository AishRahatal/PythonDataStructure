'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Iterate over set
'''
#########################################################################################

if __name__=='__main__':
    try:
        basket={'Mango','Apple','Banana','Blueberry','Kiwi','Watermelon'}
        print("-----------------------")
        print("Iterating over set using for loop :")
        for fruit in basket:
            print(fruit)
        print()
    except Exception as e:
        print("Something went wrong :",e)