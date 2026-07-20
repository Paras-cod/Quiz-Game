class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0
    def has_still_ques(self):
        return self.question_no<len(self.question_list)


    def next_ques(self):
        current_question= self.question_list[self.question_no]

        ans=input(f'Q.{self.question_no+1}:{current_question.text}(True/False):')
        self.check_answer(ans, current_question.answer)

        self.question_no+=1
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You got it wrong!")
        print(f'The correct answer is: {correct_answer}')
        print(f'The score is {self.score}/{self.question_no+1}')


