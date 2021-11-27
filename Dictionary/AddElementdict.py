'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Add an element to dictionary 
'''
#########################################################################################

if __name__=='__main__':
    try:
    
        fruit = {'mango':40, 'banana':10, 'cherry':20}
        newfruit={'apple':30}
        #update() built in function to add an element to dictinary
        fruit.update(newfruit)
        print()
        print("Updated dictionary :")
        print(fruit)
    except Exception as e:
        print("Error..",e)    