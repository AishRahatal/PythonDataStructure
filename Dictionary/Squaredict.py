'''	
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Generate dictionary in the form (x, x*x)
'''
#########################################################################################

if __name__=='__main__':
    try:
        d=dict()
        for i in range(1,6):
            d[i]=pow(i,2)
        print(d) 
    except Exception as e:
        print("Error..",e)     