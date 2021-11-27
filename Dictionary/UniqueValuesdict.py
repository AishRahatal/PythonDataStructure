'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : print unique values from dictionary 
'''
#########################################################################################
if __name__=='__main__':
    try:
        dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, 	{"V":"S009"},{"VIII":"S007"}]
        print("----------------------------")
        print("Original List: ",dic)
        print()
        u_value = set( val for dic in dic for val in dic.values())
        print("Unique Values: ",u_value)
        print()
    except Exception as e:
        print("Error..",e) 
