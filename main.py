from game import QuizGame


def show_menu():
    print("\n=== 나만의 영화 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def main():
    game = QuizGame()

    try:
        while True:
            show_menu()
            choice = input("번호를 선택하세요: ").strip()

            if choice == "1":
                game.play()
            elif choice == "2":
                game.add_quiz()
            elif choice == "3":
                game.list_quizzes()
            elif choice == "4":
                game.show_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 번호를 입력하세요.")

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 종료합니다.")

    finally:
        if game.save_state():
            print("데이터를 저장했습니다.")
        else:
            print("데이터를 저장하지 못했습니다.")


if __name__ == "__main__":
    main()