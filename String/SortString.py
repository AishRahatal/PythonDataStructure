'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title : Unique words in sorted form (alphanumerically)
'''
#########################################################################################
if __name__=='__main__':
    try:
        print("----------------------")
        string=input("Enter a words with comma :")
        words = [word for word in string.split(",")]
        sort= sorted(list(set(words)))
        print("Soted words:",sort)  
        print()
    except Exception as e:
        print("Error :",e)