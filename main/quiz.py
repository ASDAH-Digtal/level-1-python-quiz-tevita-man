#introduce the quiz.
name = input("What is you name?")
print("Hello {}, this is a quiz! This quiz is a quiz on the anime, Naruto!".format(name))
print("Before we being, lets go over a few housekeeping rules if you will. \n Number 1: When asnwering a question, answer with either the option or option number. \n Number 2: Dont cheat, that ruins the quiz. \n That is all, Lets begin")

total_score = 0
total_correct = 0

#start asking the questions for the quiz.
q1 = input("Question 1: Where was Naruto Uzumaki born? \n1. The Land of Lightning/Kumogakure \n2. The Land of Water/Kirigakure \n3. The Land of Wind/Sunagakure \n4. The Land of Fire/Konohagakure. ").lower().strip()


if q1 == "thelandoffire" or q1 == "konohagakure" or q1 == "4":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q1 == "thelandoflightning" or q1 == "kumogakure" or q1 == "1":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q1 == "thelandofwater" or q1 == "kirigakure" or q1 == "2":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q1 == "thelandofwind" or q1 == "sunagakure" or q1 == "3":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5
        
print("You current score is {}.".format(total_score))

q2 = input("Question 2: How old is Naruto in the very first episode? \n1. 13 \n2. 14 \n3. 12 \n4. 11").strip()

if q2 == "3" or q2 == "12":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q2 == "1" or q2 == "13":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q2 == "2" or q2 == "14":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q2 == "4" or q2 == "11":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q3 = input("Question 3: How tall is Naruto before the time skip (cm)? \n1. 146 \n2. 147 \n3. 148 \n4. 149").strip()

if q3 == "1" or q3 == "146":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q3 == "2" or q3 == "147" :
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q3 == "3" or q3 == "148":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q3 == "4" or q3 == "149":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q4 = input("Question 4: Who is Naruto’s rival? \n1. Sasuke \n2. Shikamaru \n3. Sakura \n4. Chogi").lower().strip()

if q4 == "1" or q4 == "sasuke":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q4 == "2" or q4 == "shikamaru":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q4 == "3" or q4 == "sakura":
    print("Sorry, but you are retarded, you lost 5 points")
    total_score -= 5
elif q4 == "4" or q4 == "chogi":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q5 = input("Question 5: What is the name of the beast inside of Naruto? \n1. Kuruma \n2. Shukaku \n3. Gyuki \n4. Isobu").lower().strip()

if q5 == "1" or q5 == "kuruma":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q5 == "2" or q5 == "shukaku":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q5 == "3" or q5 == "gyuki":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q5 == "4" or q5 == "isobu":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q6 = input("Question 6: Naruto favorite food/food store? \n1. Lightning burger \n2. Ichu raku ramen \n3. Anata ga kore o erabunara anata no baka \n4. Onigiri").lower().strip()

if q6 == "2" or q6 == "ichurakuramen":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q6 == "1" or q6 == "lightningburger":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q6 == "3" or q6 == "anatagakoreoerabunaraanatanobaka":
    print("Sorry, Anata ga kore o erandanara anata no orokana, you lost 5 points")
    total_score -= 5
elif q6 == "4" or q6 == "onigiri":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q7 = input("Question 7: What is the name of the book that Naruto gives to Kakashi \n1. Icha Icha Paradise \n2. Icha Icha Tactics \n3. Icha Icha Innocence \n4. Icha Icha Violence").lower().strip()

if q7 == "2" or q7 == "ichaichatactics":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q7 == "1" or q7 == "ichaichaparadise":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q7 == "3" or q7 == "ichaichainnocence":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q7 == "4" or q7 == "ichaichaviolence":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q8 = input("Question 8: What is the real name of the villain known as Tobi? \n1. Itachi uchiha \n2. Madara Uchiha \n3. Shisui Uchiha \n4. Obito Uchiha")

if q8 == "4" or q8 == "obitouchiha":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q8 == "1" or q8 == "itachiuchiha":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q8 == "2" or q8 == "madarauchiha":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q8 == "3" or q8 == "shisuiuchiha":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q9 = input("Question 9: What is the name of the Jutsu Naruto creates? \n1. Rasen Shuriken \n2. Gum gum gatling gun \n3. Shadow clone jutsu \n4. Spirit Bomb")

if q9 == "1" or q9 == "rasenshuriken":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q9 == "2" or q9 == "gumgumgatlinggun":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q9 == "3" or q9 == "shadowclonejutsu":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q9 == "4" or q9 == "spiritbomb":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

print("You current score is {}.".format(total_score))

q10 = input("Question 10: The Second hokage? \n1. Tobirama Senju \n2. Hashirama Senju \n3. Minato Namikaze \n4. Rasa")

if q10 == "1" or q10 == "tobiramasenju":
    print("Correct, you earned 10 points!")
    total_score += 10
    total_correct += 1
elif q10 == "2" or q10 == "hashiramasenju":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q10 == "3" or q10 == "minatonamikaze":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
elif q10 == "4" or q10 == "rasa":
    print("Sorry, that's incorrect, you lost 5 points")
    total_score -= 5
else:
    print("That is not an option")
    total_score -= 5

#infrom the partipant of their score and thank them for playing.
print("Thank you {} for play! Out of 100 points, you scored..... \n ***Drumrole*** \n{}!!! You also got a total of {} question right out of 10 \n Thank yoiu for playing!!!".format(name, total_score, total_correct))
