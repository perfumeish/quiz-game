from quiz_data import create_default_quizzes


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

            while True:
                user_input = input("정답 번호 (1~4): ").strip()

                try:
                    answer = int(user_input)
                except ValueError:
                    print("1~4 사이의 숫자를 입력하세요.")
                    continue

                if 1 <= answer <= 4:
                    break

                print("1~4 사이의 숫자를 입력하세요.")

            if quiz.check_answer(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        total = len(self.quizzes)
        score = round(correct_count / total * 100)

        print(f"\n결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")