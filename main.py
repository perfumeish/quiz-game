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

    while True:
        show_menu()
        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            game.play()
        elif choice == "2":
            print("퀴즈 추가를 준비 중입니다.")
        elif choice == "3":
            print("퀴즈 목록을 준비 중입니다.")
        elif choice == "4":
            print("점수 확인을 준비 중입니다.")
        elif choice == "5":
            print("게임을 종료합니다.")
            break
        else:
            print("1~5 사이의 번호를 입력하세요.")


if __name__ == "__main__":
    main()