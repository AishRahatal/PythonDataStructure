'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Concatenate dictionary 
'''
#########################################################################################

if __name__=='__main__':

    try:
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50,6:60}
        #update() built in function to add an element to dictinary
        dic1.update(dic2)
        dic1.update(dic3)

        print()
        print("Updated dictionary :")
        print(dic1)
        print()
    except Exception as e:
        print("Error..",e)     