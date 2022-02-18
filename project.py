print("Wellcome to my super mega quiz!")

playing = input("Do you wanna play my game? Please answer yes or not  ")

if playing.lower() != "yes":
    quit()

print("Okay! Let`s play my game!")
score = 0

answer = input("What Sasha say when he come home? Answer must be in English  ")
if answer == "Im tired":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What Bogdan do say in Apex? Answer must be in English  ")
if answer == "He is play well":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What Ilya like to eat? Answer must be in English  ")
if answer == "He likes pasta":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What Andrey say when he come back from the job? Answer must be in English  ")
if answer == "I wanna sleep":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What papricius say about chicken in Albert? Answer must be in English  ")
if answer == "You know what? Albert has a cheaper chicken":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(" You got  " + str(score) + " Questions correct ! ")
print(" You got " + str((score / 5) * 100) + "%.")
