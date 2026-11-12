from quiz_data import create_default_quizzes
from quiz import Quiz
from input_utils import read_text, read_number


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {number}]")
            quiz.display()

            answer = read_number("정답 번호 (1~4): ", 1, 4)

            if quiz.check_answer(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        total = len(self.quizzes)
        score = round(correct_count / total * 100)

        print(f"\n결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

    def add_quiz(self):
        print("\n새로운 영화 퀴즈를 추가합니다.")

        question = read_text("문제: ")

        choices = []
        for number in range(1, 5):
            choice = read_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = read_number("정답 번호 (1~4): ", 1, 4)

        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)

        print("퀴즈가 추가되었습니다.")