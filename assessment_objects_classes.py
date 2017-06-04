"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction: 
   You don't need to know about interal fuctionality of the method; just the signature. 

   Encapsulation: 
   All attibutes and methods encapsulated into one object, so that you can call their methods on other objects.

   Polyomorphism:
    Which is uniformity and predictablity. This is acheived through inheritance from parent to child classes.

2. What is a class?
    An object that holds methods, attributes, and instances.

3. What is an instance attribute?
    When we instatiate an instance, then add attributes to just that instance. (Or it's the post it)

4. What is a method?
    Similar to a function, but only used in classes.

5. What is an instance in object orientation?
    It is the "instance" of the object. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is an attribute associated with the class and can be used to associate
   with instances. An instance attribute is only associated with the instance.


"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class Exam(object):
    def __init__(self, exam_name, questions):
        self.exam_name = exam_name
        self.questions = []
