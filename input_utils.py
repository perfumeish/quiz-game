def read_text(prompt):
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print("빈 입력입니다. 내용을 입력하세요.")


def read_number(prompt, minimum, maximum):
    while True:
        text = read_text(prompt)

        try:
            number = int(text)
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")