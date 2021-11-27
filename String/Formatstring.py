'''	
@Author: Aishwarya
@Date: 2021-11-27 
@Title : Display formatted text (width=50) as output.
'''
#########################################################################################
import textwrap
if __name__=='__main__':
    try:
        
        sample_text = '''Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasize scode readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.
            '''
        print()
        print(textwrap.fill(sample_text, width=50))
        print()

    except Exception as e:
        print("Error...",e)
        
