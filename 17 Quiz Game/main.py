from question_model import QuestionModel

q_num = 0
print("Welcome to Quiz Game!!!")
question_model = QuestionModel()

while True:
    current_q = question_model.next_question()

    # Check if there are any questions available. if not, end the quiz.
    if not current_q:
        print("Quiz is Over.")
        print(f"Your final score is: {question_model.get_score()}/{q_num}")
        print("Thanks for playing.")
        break
    q_num += 1

    # print the question.
    user_answer = input(f"Q{q_num}. {current_q.question} (True/False)\n")

    # print whether user answer is correct or not.
    is_right = question_model.check_answer(current_q, user_answer)
    if is_right:
        print("You got it right!")
    else:
        print("That's wrong.")
        is_right = not is_right

    print(f"Correct answer was: {is_right}")
    print(f"Your current score is: {question_model.get_score()}/{q_num}")
