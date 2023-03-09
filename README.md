# Python-Practise-Tasks

Program 1: square roots

This program computes the square root of each non-negative number in a given list using the compute_square_roots function. 
If a negative number is encountered, it returns None. The program provides two sample input lists, values1 and values2, for testing the function. 
It includes a test function, test_compute_square_roots, that verifies the correctness of the output.

Program 2: find words in brackets

This program searches for words enclosed in parentheses in a given list called text. 
It uses a loop and a enumerate function to iterate through each character in the text and keep track of open and closing parentheses. 
The words inside the parentheses are added to the words_in_brackets list. The final output is a list of words found within parentheses in the input text.

Program 3: sort in numerical order

This program sorts three strings containing numbers written as words (string1, string2, and string3) in numerical order. 
It defines a dictionary called number_mapping that maps each word to its numeric value and a function called words_to_numbers 
that returns a list of the corresponding numeric values for a given string of words. 
The program then sorts each string of words using the sorted function based on the corresponding numeric values of the words and prints 
the sorted strings to the console.

Program 4: geometry

This program defines two classes, Rectangle and Circle, that determine whether a given point is inside a rectangle or circle, respectively. 
Both classes have an is_inside function that takes two input parameters, x and y, representing the coordinates of the point to be tested. 
The functions use the distance formula between two points to determine whether the given point is inside the shape or not. 
The program does not include any sample inputs or tests.

Program 5: classes - 2D geometric shapes

This program is a collection of classes that represent 2D geometric shapes, including Point, Segment, Circle, and Rectangle.
Each class contains methods to move and scale the shapes. Additionally, there is a Group class that is a collection of shapes 
and has methods to move all the shapes in the collection by the same vector and scale them by the same factor.
The program provides an implementation of each class, including the Group class, but does not include any sample inputs or tests.
