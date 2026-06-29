from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    question_text = question["text"]  #takes in the tect part of the dictionary
    question_answer = question["answer"]
    
    new_question = Question(question_text,question_answer) #creates a new_quesiton using the class in question_modeule

    question_bank.append(new_question) #adds new question to the question bank

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print(f"Score: {quiz.score}")

 