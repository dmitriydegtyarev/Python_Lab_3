def get_sentence():
    return input("Введіть будь ласка речення ->> ")

def replace_sentence():
    sentence = get_sentence().split()

    if len(sentence) < 2:
        print("В реченні повинно бути не менше 2-х слів.")
    else:
        sentence[0], sentence[-1] = sentence[-1], sentence[0]
        print(f"Змінене речення ->>> {' '.join(sentence)}")

replace_sentence()