
# Intro to Python Chapter #1

# Lines that begin with # are comments -- they explain code but are not executed

# Basic Math at the repl 
# You cans start repl on command line or in VS-Code - shift -comand on mac then (Python_start repl)
# 1. what is the result of: 2 + 3 * 5

# play around with different math functions at repl

2 + 3 * 5

# Nothing happens if run as a file 
# run with shift-enter with curser at end of line works in interactive shell
# You need a print() function to make it show up

print(2+3*5)

# You can use a variable 

n = 2 + 3 * 5 

print(n)

# 2. assign 2,3 and 5 each to different variables then add/multiply them together in the print() function

# 3. same as 2 but assign the answer to a variable and print that

# 4. Change precedence to get 25, assign result to n2 and print answer (boring 15)

# 5. Add n to n2, assign it to ans and print ans - hint you should get 42


# 6. find the type for 2  -hint type(2)

type(2)

# 7. Find type for 2.5

type(2.5)

# 8. Find type for 2 + 2.5

2 + 2.5
type(2+2.5)

# Strings  -- Double quotes

"Campbell"

# concatenating Strings

"Campbell" + " " + "Law" + " " + "School"

# assign string to variable

l = "law"


# 9. print() Campbell Law School
#  a) All three words as a single string
#  b) use concatenated strings in a print statement print("Campbell" + ...)
#  c) assign to a variable and print the variable


# 10. What happens when you print() "Law" + 2019  (How can you fix it?)



# 11. What about "Campbell" * 3 ?


# Variables:
#  1) Can only be one word
#  2) Can't begin with number
#  3) Hyphens not allowed 
#  4) Can't be reserved words
#  5) Can't be special character like $ of '

# 12. which ones of the following are valid:

# school = "campbell Law"
# 2L = "Bob"
# law-school = "Campbell"
# total_$um = 100
# not = "no"

# 13. Write "Your First Program" page 21 in text (Hint - You can copy it)



# 14. What happens with print("I am " + 25 + " years old") - Can you fix it


# 15. Which of the following are True
   a). 25 == '25'
   b). 25 == 25.00
   c). 25 == 0025.00
   d). 25 == int("25")