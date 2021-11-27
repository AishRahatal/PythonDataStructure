'''	
@Author: Aishwarya
@Date: 2021-11-26 
@Title : Count of words with first and last character are same in a list.
'''
#########################################################################################

if __name__=='__main__':
    try:
        list=['abc', 'xyz', 'aba', '1221','111','ana','ssb']
        c=0
        for s in list:
            if len(s)>1 and s[0]==s[-1]:
                c=c+1
        print("-----------------------------------------------------")        
        print("count of words with first and last character are same : ",c)
        print()
    except Exception as e:
        print("Error...",e)
