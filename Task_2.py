def get_word():
    return input("Введіть будь ласка довільне слово ->> ")

def find_max_repeat(word):
    max_repeat = 0
    char_max_repeat = ""
    current_count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            current_count += 1
        else:
            if current_count > max_repeat:
                max_repeat = current_count
                char_max_repeat = word[i - 1]
            current_count = 1

    if current_count > max_repeat:
        max_repeat = current_count
        char_max_repeat = word[-1]

    return max_repeat, char_max_repeat

def check_result():
    word = get_word()
    repeat, char = find_max_repeat(word)

    if len(word) < 2:
        print("Довільне слово повинно містити більше одного символу.")
    elif repeat > 1:
        print(f"Символ -> {char} повторюється -> {repeat} рази (ів).")
    else:
        print("Символи які повторюються відсутні.")

check_result()
