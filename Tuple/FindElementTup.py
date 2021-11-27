
'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Check whether an element exists within a tuple.
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------------------")
        basket=('Mango','Kiwi','Banana','Blueberry','Kiwi','Blueberry')
        print("basket: ",basket)
        print()
       
        print("there are 'Kiwi'   in basket  :",'Kiwi'in basket)
        print("there are 'Mango'  in basket  :",'Mango' in basket)
        print("there are 'Orange' in basket  :",'Orange' in basket)

        print()
    except Exception as e:
        print("Error...",e)