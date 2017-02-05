import unittest
import re

## SI 206 - W17 - HW3
## COMMENT WITH:
## Your section day/time:
## Any names of people you worked with on this assignment:

#####################


## PART 1: 300 points

## Use regular expressions to define a function called parse_counted_words which should accept a string, find strings of the form: <count> <word>  e.g. 101 Dalmations, inside it, and should return either the LAST correctly matching number-word combo in the string as a tuple, e.g. ('13', "pineapples"), if there are any such sub-strings, or None, if there are not.
## The number in the <count> should be one or more digits only. The word should be made up of an optional non-alphabetic character followed by any number of alphabetic characters, upper or lower case.
## HINT:  \b matches the beginning or end of a word
## HINT:  you can use the Python re .findall method to get multiple matches in a string
#parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') should return ('1', 'papaya')
# parse_counted_words('101 dalmations!') should return ('101', 'dalmations') ...

## Write code to define your parse_counted_words function here.      x = re.search('[0-9]+ ^\w*$', turtle)


import re
def parse_counted_words(turtle):
    x = re.findall(r'\b([0-9]+)\s(.[A-Za-z]+)', turtle)
    if x:
        print(x[-1])
        return x[-1]


## PART 2: 200 points

## We have provided a text file computer_paths.txt. It's not incredibly long -- you can scan through it, but do NOT hard code your answers! Each line contains 1 filesystem path.

## (a) Write Python code to determine how many of these paths identify FILES, not directories. Save that number in the variable file_paths_num.
ocean = open('computer_paths.txt')
numlist = []
for fish in ocean: 
    x1 = re.findall(r'\S+\.\S+', fish)
    if x1:
        numlist.append(x1)
file_paths_num = 0
for files in numlist: 
    file_paths_num += 1




## (b) Write Python code to determine how many of these paths are FULL paths, not relative paths. Save that number in the variable full_paths_num.
ocean = open('computer_paths.txt')
numlist2 = []
for fish in ocean: 
    x3 = re.findall(r'^/Users\S+', fish)
    x2 = re.findall(r'^~\S+', fish)
    if x3: 
        numlist2.append(x3)
    if x2:
        numlist2.append(x2)
full_paths_num = 0
for files in numlist2:
    full_paths_num += 1


## (c) Write Python code to determine how many of these paths describe a Python file saved inside a folder called SI206. Save that number in the variable python_course_paths.
ocean = open('computer_paths.txt')
numlist3 = []
for fish in ocean: 
    x4 = re.findall(r'\S+SI206\S+.py', fish)
    x5 = re.findall(r'SI206\S+.py', fish) 
    if x4: 
        numlist3.append(x4)
    elif x5:
        numlist3.append(x5)
python_course_paths = 0
for files in numlist3:
    python_course_paths += 1
## (d) Write Python code to determine how many of these paths describe a Microsoft file (a file that EITHER ends with .docx OR .xlsx, but nothing else counts) where the file name ends in a digit. Save that total in the variable microsoft_files_num.

ocean = open('computer_paths.txt')
numlist4 = []
for fish in ocean: 
    x6 = re.findall(r'\S+[0-9]\.xlsx', fish)
    x7 = re.findall(r'\S+[0-9]\.docx', fish) 
    if x6:
        numlist4.append(x6)
    elif x7:
        numlist4.append(x7)
microsoft_files_num = 0
for files in numlist4:
    microsoft_files_num += 1



## We have provided unit tests in this file. To earn the full 500 points, you'll need to pass all of the tests and will need to have followed the instructions.
## Each class of the tests represents one "part" of the homework, and the points for each part are divided approx. equally between each of the tests.

####### UNIT TESTING BELOW; DO NOT CHANGE ANY TESTING CODE #######

class Part1_HW3(unittest.TestCase):
    def test_pcw_1(self):
        self.assertEqual(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.'),('1','papaya'))
    def test_pcw_2(self):
        self.assertEqual(parse_counted_words('101 dalmations!'),('101','dalmations'))
    def test_pcw_3(self):
        self.assertEqual(parse_counted_words('snow white and the 7 #littledwarves'),('7','#littledwarves'))
    def test_pcw_4(self):
        self.assertEqual(parse_counted_words('goldilocks and the 3 little pigs'),('3','little'))
    def test_pcw_5(self): 
        self.assertEqual(parse_counted_words('678 1234567 890  '),None)
    def test_pcw_6(self):
        self.assertEqual(parse_counted_words("hellllo 5000"), None)
    def test_pcw_7(self):
        self.assertEqual(parse_counted_words("!!!! 6"), None)
    def test_pcw_8(self):
        self.assertEqual(parse_counted_words("!!!!! 72 and 76 calendars"),('76',"calendars"))

class Part2_HW3(unittest.TestCase):
    def test_cpaths_1(self):
        self.assertEqual(file_paths_num,16)
    def test_cpaths_2(self):
        self.assertEqual(full_paths_num,16)
    def test_cpaths_3(self):
        self.assertEqual(python_course_paths,3)
    def test_cpaths_4(self):
        self.assertEqual(microsoft_files_num,3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

