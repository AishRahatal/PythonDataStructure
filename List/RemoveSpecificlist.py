'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Print a specified element list after removing the 0th, 4th and
         5th elements.
'''
#########################################################################################
if __name__=='__main__':
    try:
        List =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        print("-------------------------------------------------")
        print("List : ",List)
        print()
        #pop() removes last element by default
        List.pop()# removes yellow
        List.pop(0)#removes red
        List.pop()#removes pink
        print("List after removing :")
        print("List : ",List)
        print()
            
    except Exception as e:
            print("Error...",e)