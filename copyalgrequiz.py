# https://www.youtube.com/watch?v=yriw5Zh406s 9:54
# we are on line 33





#Functions of the quiz
def new_game():
    
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("").strip().lower()
        guesses.append(guess)
        
        check_answer(questions.get(key),guess)
        questions_num += 1

#------------------------------
def check_answer(answer , guess):
    
    if answer == guess:
        print("correct!")
        return 1
    else:
        print()

#------------------------------
def display_score():
    pass
#------------------------------
def play_again():
    pass

#Dictionary that holds the questions and asnwers
questions = {
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",
    ":" "": "",  
}

# 2list that holds all answer options to answer question
options = [ [""""""""],
            [""""""""], 
            [""""""""],
            [""""""""],
            [""""""""],
            [""""""""],
            [""""""""],
            [""""""""],
            [""""""""],
            [""""""""],
]

new_game()