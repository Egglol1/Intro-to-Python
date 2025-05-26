# Reflection Questions
  1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. 
  Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation: 

  - The script should ask the user where they want to travel. 
  -	The user’s input should be checked for 3 different travel destinations that you define. 
  -	If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
  -	If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”

  ```
  where_to_go = input('Where do you want to travel?')
  where_to_go.capitalize()
  destinations = ['Berlin', 'London', 'Washington']
  if where_to_go in destinations:
    print('Enjoy your stay in ' + where_to_go + '!')
  else:
    print('Oops, that destination isn\'t available.')
  ```

  2.	Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.

  The logical operators in Python are 'and', 'or', 'in', and 'not'. 'and' checks if two conditions are both true and returns a boolean based on that comparison. 
  'or' checks if one of two conditions is true, and if either of them are, it returns a boolean True. 
  'in' checks if a value is contained within a data type such as a list, tuple, or dictionary and returns True if it is.
  'not' is added before any other logical operator and switches the True and False values. For example, 1 + 1 = 2 would return True, but 1 + 1 not = 2 would return False.

  3.	What are functions in Python? When and why are they useful?

  A function is a set of instructions that manipulate code in a certain way. Like how upper() changes a string to be all uppercase letters. 
  They are useful because they vastly shorten the amount of code that needs to be written in a single line or file, which makes development easier. 

  4.	In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course.  
  In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

  So far, the lessons we've been having seem a little more geared towards the second achievement instead of the current recipe app. 
  I am happy to have a refresher on the Python basics, since I hadn't used it in years until now.
