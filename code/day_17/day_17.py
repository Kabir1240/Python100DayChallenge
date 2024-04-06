from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""
Main file for quiz gam
"""

# adds questions and their answers as Question objects to question bank
question_bank = []
for item in question_data:
    new_question = Question(text=item["question"], answer=item["correct_answer"])
    question_bank.append(new_question)

# Makes new QuizBrain and gives it the Question objects list
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    # ask user questions
    quiz.next_question()
# end game
quiz.quiz_complete()
