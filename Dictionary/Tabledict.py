''''
@Author: Aishwarya
@Date: 2021-11-25 
@Title : Convert dictionary into table format
'''
#########################################################################################


if __name__=='__main__':
    try:    
    # Define the dictionary
        dic1 ={}

        # Insert data into dictionary
        dict1 = {1: ["Samuel", 21, 'Data Structures'],
            2: ["Richie", 20, 'Machine Learning'],
            3: ["Lauren", 21, 'OOPS with java'],
            }

        # Print the names of the columns.
        print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

        # print each data item.
        for key, value in dict1.items():
            name, age, course = value
            print ("{:<10} {:<10} {:<10}".format(name, age, course))
        print()
        lst = [{'Name':'Tim', 'Age':3}, {'Name':'Kate', 'Age':2}]
        print("Name\tAge")
        for i in lst:
            print("{}\t{}".format(i['Name'],i['Age']))    
    except Exception as e:
        print("Error..",e) 

