'''
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Words which have more length than given list
'''
#########################################################################################

if __name__=='__main__':
    try:
        print("-----------------------------------------------------------")
        fruits = ["cherry", "orange", "Watermelon", "melon","Kiwi"] 
        print("List : ",fruits)
        #print(len(fruits))
        print()
        res=[]
        for x in fruits:
            if len(x)>len(fruits):
                #print(len(x))
                res.append(x)
        print("Words which have more length than given list: \n")
        print(res)
        print()    
    except Exception as e:
        print("Error...",e)