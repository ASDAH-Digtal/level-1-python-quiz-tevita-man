#introduce the quiz.
name = input("What is you name?")
print("Hello {}, this is a quiz! This quiz is a quiz on the anime, Naruto!".format(name))
print("There is one rule when it comes to this quiz. When answering, spell the answer as it is presented. So if the answer you want to put is cat and you put kat, it will be wrong. Lets begin")

total_score = 0
#start asking the questions of the quiz.
q1 = input("1. Question 1: Where was Naruto Uzumaki born? \n1. The Land of Lightning/Kumogakure \n2. The Land of Water/Kirigakure \n3. The Land of Wind/Sunagakure \n4. The Land of Fire/Konohagakure. ")

if q1 == "The Land of Fire." or q1 == "Konohagakure." or q1 == "4":
    print("Correct, you earned 10 points!")
    total_score += 10
elif q1 == "The Land of Lightning" or q1 == "Kumogakure" or q1 == "1":
    print("Sorry, that's incorrect, you lost 5 points")
elif q1 == "The Land of Water" or q1 == "Kirigakure" or q1 == "2":
    print("Sorry, that's incorrect, you lost 5 points")
elif q1 == "The Land of Wind" or q1 == "Sunagakure" or q1 == "3":
    print("Sorry, that's incorrect, you lost 5 points")
else:
    print("That is not an option")


#infrom the partipant of their score and thank them for playing.
