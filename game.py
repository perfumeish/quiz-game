import json
from pathlib import Path
from quiz_data import create_default_quizzes
from quiz import Quiz
from input_utils import read_text, read_number


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.state_path = Path(__file__).resolve().parent / "state.json"
        self.load_state()
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


        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        print(f"\n결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        if not self.save_state():
            print("이번 게임의 점수를 파일에 저장하지 못했습니다.")       
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
        if self.save_state():
            print("퀴즈가 추가되고 파일에 저장되었습니다.")
        else:
            print("퀴즈는 추가되었지만 파일에 저장하지 못했습니다.")
      

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")


        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")



    def show_score(self):
        if self.best_score is None:
            print("아직 완료한 게임이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점 (100점 만점)")

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        temp_path = self.state_path.with_name("state.json.tmp")

        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            temp_path.replace(self.state_path)

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")
            return False

        return True
    

    def load_state(self):
        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 데이터는 객체 형태여야 합니다.")

            quiz_data = data["quizzes"]
            best_score = data["best_score"]

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            quizzes = []

            for item in quiz_data:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 형식이 잘못되었습니다.")

                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not isinstance(question, str) or not question.strip():
                    raise ValueError("문제가 비어 있거나 잘못되었습니다.")

                if not isinstance(choices, list) or len(choices) != 4:
                    raise ValueError("선택지는 4개여야 합니다.")

                if any(
                    not isinstance(choice, str) or not choice.strip()
                    for choice in choices
                ):
                    raise ValueError("선택지 내용이 잘못되었습니다.")

                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답 번호가 잘못되었습니다.")

                quizzes.append(Quiz(question, choices, answer))

            if best_score is not None:
                if type(best_score) is not int or not 0 <= best_score <= 100:
                    raise ValueError("최고 점수가 잘못되었습니다.")

            self.quizzes = quizzes
            self.best_score = best_score
            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
        except (ValueError, KeyError, TypeError) as error:
            print(f"저장 데이터가 손상되어 기본 퀴즈로 시작합니다: {error}")
        except OSError as error:
            print(f"파일을 읽을 수 없어 기본 퀴즈로 시작합니다: {error}")