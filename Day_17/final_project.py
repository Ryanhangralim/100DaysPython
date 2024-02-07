from question_model import Question
from data import question_data

#initialize question bank
question_bank = []

#loops through questions and add it to the question bank
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)
