from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

Question_Bank=[]
for question in question_data:
  question_text=question["question"]
  question_answer=question["correct_answer"]
  new_ques=Questions(question_text,question_answer)
  Question_Bank.append(new_ques)
quiz=QuizBrain(Question_Bank)

while quiz.has_still_ques():
    quiz.next_ques()
print("You completed the quiz")
print(f'The final score is: {quiz.score}/{quiz.question_no}')