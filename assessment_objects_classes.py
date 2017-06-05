"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction: 
    The act of hiding the interal fuctionality of methods and attributes of a class and calling only the signature
    of a method. 

   Encapsulation: 
    Encapsulations organizes all attributes and methods into one class. Abstraction is achieved though encapsulation.  

   Polymorphism:
    Polymorphism means "many forms" is able to handle different forms of inputs to return a predictable output. 
    This is acheived through inheritance from parent to child classes.

2. What is a class?
    It is an object that contains methods and attributes that pertains to the class. 

3. What is an instance attribute?
    Once we instatiate an instance, or create an object with a particular class then we can add 
    attributes to just that object, or "post its", that supercedes our class attributes. 

4. What is a method?
    Similar to a function, but only used in classes. Methods interact with "self", or the instance of
    the object. 

5. What is an instance in object orientation?
    An instance is the existence of the object. In our case, the object is a class, so we are creating
    the object, but it is a different version from other instances.  

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    A class attribute is an attribute associated both with the class and with instances. 
    An instance attribute is only associated with the instance. You would use a 
    class attribute to start off with when you make a class. With instance attributes, you can
    make changes for just that specific instance.

    For example, if you create a class, "Plate" with parameters of "main_dish", "side_dish". You can
    create class attributes which will start off with the first arguments you give it, such as,
    "steak" and "potatoes" for the instance "dinner".

    However, if you want to create an instance of "lunch", and you don't want "steak and potatoes".
    Then you can change the instance attributes of "lunch" to "sandwich" and "salad".


"""


# Parts 2 through 5:
# Create your classes and class methods

# created a class Student that store first_name, last_name, and address as data
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

# created a class Question that stores a question and the answer as data
class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        '''prints the question and asks the user for the answer. returns if the answer was correct'''

        print self.question 
        user_answer = raw_input("answer >>" )

        if user_answer == self.correct_answer:
            return True
        else:
            return False

# created a class Exam that stores the exam name as data.
# the questions are stored in a list so we can add multiple instances of Question
class Exam(object):
    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question):
        '''this method allows us to add our question instances to our exam class'''
        self.questions.append(question)

    def administer(self):
        '''ask the user each question on the exam and score their results'''
        self.score = 0
        self.number_of_questions = len(self.questions)

        # I need a for loop to iterate through each question in our list of questions
        for each_question in self.questions:

            # "correct" stores True if the user got the answer right
            correct = each_question.ask_and_evaluate()

            # each correct answer gets 1 added to the current score
            if correct:
                self.score = self.score + 1

        # calculate the percentage of the score correct based on the number of questions asked
        return float(self.score) / float(self.number_of_questions) * 100

# created the class StudentExam which stores the student and the exam as data
class StudentExam(object):
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = 0

    def take_test(self):
        '''calls the administer method which runs the list of questions and captures the score'''
        self.score = self.exam.administer()
        print "Your score is " + str(self.score)


def example():
    '''this function instantiates examples of the classes above and runs an exam for a student'''
    exam = Exam("SAT") 
    
    question_1 = Question("what color is the sky?", "blue")
    question_2 = Question("what color is a sea lion?", "brown")
    question_3 = Question("what color does red and blue mixed make?", "purple")
    
    exam.add_question(question_1)
    exam.add_question(question_2)
    exam.add_question(question_3)

    nura = Student("nura", "renke", "123 street")

    student_exam = StudentExam(nura, exam)

    student_exam.take_test()

# created a class Quiz which inherits from Exam
class Quiz(Exam):

    def administer(self):
        '''same administration as class Exam, but delivers a pass (1) or fail grade (0) '''
        percentage_score = super(Quiz, self).administer()
        if percentage_score >= 50.0:
            return 1
        else:
            return 0

# created a StudentQuiz which inherits from StudentExam
class StudentQuiz(StudentExam):

    def take_test(self):
        '''runs the same administer method from StudentExam Class to capture the score'''
        self.score = self.exam.administer()

        # different between Student Quiz and Student Exam is the pass or fail grade
        if self.score == 1:
            print "You passed"
        else:
            print "You failed"

def example_quiz():
    '''This function prints out an example of the instanitation of each instance from class Quiz'''
    quiz = Quiz("SAT") 
    
    question_1 = Question("what color is the sky?", "blue")
    question_2 = Question("what color is a sea lion?", "brown")
    question_3 = Question("what color does red and blue mixed make?", "purple")
    
    quiz.add_question(question_1)
    quiz.add_question(question_2)
    quiz.add_question(question_3)

    nura = Student("nura", "renke", "123 street")

    student_quiz = StudentQuiz(nura, quiz)

    student_quiz.take_test()
