'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Count of how many dictionaries have success as True
'''
#########################################################################################

if __name__=='__main__':
    try:    

        dic= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, 
            {'id': 3, 'success': True, 'name': 'Alex'}]
            #sum() for getting count
        sum_id=sum(d['id'] for d in dic)
        sum_success=sum(d['success'] for d in dic)

        print("Count of id :",sum_id)
        print("Count of success :",sum_success)
    except Exception as e:
        print("Error..",e)
    