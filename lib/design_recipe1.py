#Reading Time: Function Design Recipe

"""""


As a user
So that I can manage my time
I want to see an estimate of reading time for a text,
assuming that I can read 200 words a minute.

"""

#2. Design the Function Signature
"""""
Include: 
-The name of the function.
-What parameters it takes, their names and data types.
-What it returns and the data type of that value.
"""
#Function Name: Python
def estimate_reading_time(text):
    #parameters:text:a stringrepresenting human readable text
    #return: a float: representing a reading time

#3 Create Examples as Tests
#Make a lis of examples of the method will take and return 

#python 


"""""
Given a text of 200 words
it will return a reading time of 1
"""

estimate_reading_time("....200....")
#=> 1.0


"""""
Given a text of 400 words
it will return a reading time of 1
"""

estimate_reading_time("....400....")
#=> 1.0




"""""
Given a text of 300 words
it will return a reading time of 1.5
"""
estimate_reading_time("....300....")
#=> 1.5



"""""
Given an empty text
it will return an error
"""

estimate_reading_time("")
#Raises error:"Cant estimate reading time for an empty text"