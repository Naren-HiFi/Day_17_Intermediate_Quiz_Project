from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)



'''
My Innovative code
 
en_of_objects = len(question_data)

question_bank = []

for question in range(0,len_of_objects):
    entry = question_data[question]
    text = entry["text"]
    answer = entry["answer"]
    question_object = Question(text,answer)
    question_bank.append(question_object)

print(question_bank)


'''

