score = 0


#Questions
Q1 = "What is the capital of France?"
Q2 = "What is 5+5?"
Q3 = "What is capital of Thailand?"
Q4 = "What is capital of Myanmar?"
Q5 = "Whaat is capital of India?"

#Answers
A1 = "Paris"
A2 = "10"
A3 = "Bangkok"
A4 = "Nay pyi taw"
A5 = "New delhi"

print("==== pYTHON QUIZ ====")
print(Q1)
answer = input("Enter your answer: ").capitalize()
if answer == A1:
    print("Correct!")
    score += 1
else:
    print("incorrect!")

print(Q2)
answer = input("Enter your answer: ")
if answer == A2:
    print("Correct!")
    score += 1
else:
    print("incorrect!")

print(Q3)
answer = input("Enter your answer: ").capitalize()

if answer == A3:
    print("Correct!")
    score += 1
else:
    print("incorrect!")


print(Q4)
answer = input("Enter your answer: ").capitalize()
if answer == A4:
    print("Correct!")
    score += 1
else:
    print("incorrect!")

print(Q5)
answer = input("Enter your answer: ").capitalize()
if answer == A5:
    print("Correct!")
    score += 1
else:
    print("incorrect!")

print("==== RESULT ====")

if score == 5 :
    print(f"Score: {score}/5")
    print('Excellent!')
elif score >= 3 :
    print(f"Score: {score}/5")
    print('Good job!')
else :
     print(f"Score: {score}/5")
     print('try again!')