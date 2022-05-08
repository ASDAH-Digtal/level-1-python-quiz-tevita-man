#introduce the quiz.
name = input("What is you name?")
print("Hello {}, this is a quiz! This quiz is a quiz on the anime, Naruto!".format(name))
print("There is one rule when it comes to this quiz. When answering, spell the answer as it is presented. So if the answer you want to put is cat and you put kat, it will be wrong. Lets begin")

total_score = 0
#start asking the questions of the quiz.
q1 = input("1. ")

if q1 == "" or q1 == "":
    print("Correct, you earned 10 points!")
    total_score += 10
elif q1 == "" or "":
    print("Sorry, that's incorrect, you lost 5 points")
elif q1 == "" or "":
    print("Sorry, that's incorrect, you lost 5 points")
elif q1 == "" or "":
    print("Sorry, that's incorrect, you lost 5 points")
else:
    print("That is not an option")
#infrom the partipant of their score and thank them for playing.
