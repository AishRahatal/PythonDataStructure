'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Multiple keys exists in a dictionary
'''
#########################################################################################
if __name__=='__main__':
    try:
        basket = {
        'Mango': 10,
        'Blueberry': 20,
        'Kiwi': 3,
        'Banana': 4
                }
        #using function all( ) to check multiple keys
        if all (k in basket for k in ("Mango","Blueberry","Kiwi","Banana")):
                print ("They're there!")
    except Exception as e:
        print("Error..",e)             