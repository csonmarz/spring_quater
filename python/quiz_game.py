print("Welcome to my computer game quiz!")

playing = input("Do you want to play? ")

text = ""

if playing != "yes": 
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "cenrral processing unit":
    print('Correct!')
    score += 1
    score = score + 1 
else:
    print("incorrect")

answer = input(" What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
    score = score + 1 
else:
    print("Incorrect!")

answer = input(" What does RAM stand for?")
if answer.lower() == "random acess memory":
    print('Correct!')
    score += 1
    score = score + 1 
else:
    print("Incorrect!")

answer = input(" What does PSU stand for?")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
    score = score + 1 
else:
    print("Incorrect!")

print(" You got " + str(score) + " questions correct!")
print(" You got " + str((score / 4) * 100) + "%")

