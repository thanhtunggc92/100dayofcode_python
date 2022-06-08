from data import question_data

from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for item in question_data:
    questions_text= item['text']
    questions_answer=item['answer']
    new_q= Question(q_text=questions_text,q_answer=questions_answer)
    question_bank.append(new_q)
quiz_brain=QuizBrain(question_bank)

while quiz_brain.is_still_remaining():
    quiz_brain.next_question()

print("You complete all the questions:")
print(f"Your final score is: {quiz_brain.score}/{len(question_bank)} ")