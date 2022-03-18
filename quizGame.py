def main():
    questions = {
    "What is the black man's name": ["Dawit", "Cory", "Tony", "Sam", "a"],
    "Blue is a color": ["True", "False", "a"],
    "What color is Tony's work desk?": ["White", "Black", "Baige", "Green", "Red", "a"],
    "Dawit's favourite hobby!": ["Gaming", "Sleeping", "Working", "b"],
    "1 + 1 = 5": ["True", "False", "b"]
    }
    questions_right = 0
    count = 1
    run = True
    lstOfChoices = []
    print(f"Welcome to the Quiz Game of {len(questions)} questions")
    while run and count-1 != len(questions):
        print(f"Question {count} >>> {list(questions.keys())[count-1]}")
        lstOfAnswersForQuestion = list(questions.values())[count-1]
        for val, choices in enumerate(lstOfAnswersForQuestion):
            if val != len(lstOfAnswersForQuestion) - 1:
                print(f"{chr(97+val)}) {choices}")
                lstOfChoices.append(chr(97+val))
        while True:
            user_input = input("Type your letter letter choice or -1 to quit: ")
            user_input = user_input.lower()
            if user_input == "-1":
                run = False
                break
            elif len(user_input) == 1 and user_input in lstOfChoices:
                break
            print("invalid input")
        if user_input == lstOfAnswersForQuestion[-1]:
            questions_right += 1
        count += 1

    if run:
        print(f"Number of rights is {questions_right}")

main()