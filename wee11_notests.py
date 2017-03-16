import unittest

# Lets build on what we did last week in discussion section :-)
starter = [1, 3, 6, 11, 5, 8, 7, 2, 9]

# ---- Task 1a ----
# Write a funtion squareFunc takes a number as a paramter and returns the square of the number
# ----- Your Code Starts Here -----


# ---- Task 1b -----
# Map function takes 2 parameters - a function object, and a sequence
# i.e. it is invoked like this -> map(aFunction, aSequence)
# Use squareFunc as first parameter in map function, and the list starter as second parameter
# Store the result returned by map function in a variable square_fn
# ----- Your Code Starts Here -----
square_fn =


# ---- Task 1c ----
# Write a lambda function that does the same thing as squareFunc
# and use the lambda function in place of squareFunc.
# Store the result returned by map function in a variable square_la
# ----- Your Code Starts Here -----
square_la =


# ---- Task 1d ----
# Cast square_la to a list square_lst
# ----- Your Code Starts Here -----
square_lst = []


# ---- Task 2a ----
# Since map function works on sequences, lets try it on a string.
# First, write a function flippingCase which takes a character
# and returns it in uppercase if the character is lowercase
# else returns it in lowercase if the character is uppercase
# Hint : You can use str.isUpper(), str.isLower(), str.upper(), str.lower() if needed
# ----- Your Code Starts Here -----


# ---- Task 2b ----
# Use the function flippingCase and the string 'I Am Camel Case' as parameters for map function
# Store the result in variable confusedCase
# ----- Your Code Starts Here -----
confusedCase =


# ---- Task 2c ----
# Cast confusedCase to a list confusedList
# ----- Your Code Starts Here -----
confusedList = []


# ---- Task 2d ----
# Write a lambda function that does the exact thing as flippingCase, and use it in the map function
# Store the result in confusedCaseAgain
# HINT : Think about how you had written if in list comprehensions
# ----- Your Code Starts Here -----
confusedCaseAgain =


# ---- Task 2e ----
# Cast confusedCaseAgain to a list confusedListAgain
# ----- Your Code Starts Here -----
confusedListAgain = []

# ---- Task 3a ----
# Time to do some filtering!
# Filter function takes same parameters as map function - a function object and a sequence
# First write a function lowercaseOnly that returns a character only if it is lowercase, else returns None
# ----- Your Code Starts Here -----


# ---- Task 3b ----
# Use function lowercaseOnly and confusedListAgain as parameters of filter function
# and filter all lowercase letters
# Store the result in lowercase_filter.
# ----- Your Code Starts Here -----


# ---- Task 3c ----
# Cast lowercase_filter to lowercase_list
# ----- Your Code Starts Here -----
lowercase_list =


# ---- Task 3d ----
# Use lambda function to do the exact same thing as lowercaseOnly
# Use this function as a parameter in filter function
# Now instead of storing the result of filter function in a variable, cast it to list directly
# Assign the final list to variable lowercase_list_la
# ----- Your Code Starts Here -----
lowercase_list_la = []
