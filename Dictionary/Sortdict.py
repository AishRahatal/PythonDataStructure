'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Sort dictionary in ascending and descending order
'''
#########################################################################################
import operator
if __name__=='__main__':
    try: 
        dictionary = {1: 'z', 3: 'c', 4: 'v', 2: 'x', 0: 'g'}
        print("--------------------------------------------------")
        print('Dictionary : ',dictionary)
        print()
        sort_dict = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
        print("Ascending order by value : ",sort_dict)
        print()
        sort_dict = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
        print("Descending order by value : ",sort_dict)

    except Exception as e:
        print("Error..",e)     