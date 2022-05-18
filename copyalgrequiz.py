# https://www.youtube.com/watch?v=yriw5Zh406s 9:54
# we are on line 33





#Functions of the quiz
#This function asks the questions and takes in the users input.
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
        
        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_guesses, guesses)


#Ths function checks if the user answred the question correctly
def check_answer(answer , guess):
    
    if answer == guess:
        print("correct!")
        return 1
    else:
        print("")
        return 0

#------------------------------
def display_score(correct_guesses, guesses):
    print("")
    print("resualts")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(questions.get(i), end=" ")
    print()

    score = int(correct_guesses/len(questions))*100
    print(""+str(score)+"%") 

#This function is responsiblie for asking if they would like to play again.
def play_again():
    
    responese = input("")
    responese = responese.upper()

    if responese == "YES":
        return True
    else:
        return False


#Dictionary that holds the questions and correct asnwers
questions = {
    "Where was Naruto Uzumaki born?: ": "A",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": "",
    ": ": ""
    
}

#list that holds all answer options to each question
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

while play_again():
    new_game

print("byeeeeeeeeeeee")