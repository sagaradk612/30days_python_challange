quiz_data=[
    {
        "Question" : "What is the capital of France?" ,
        "Answer" : "PARIS"} ,
    {
        "Question" : "What is 5+5?" ,
        "Answer" : "10" } ,
    {
        "Question" : "What is capital of Thailand?" ,
        "Answer" : "BANGKOK" } ,
    {
        "Question" : "What is capital of Myanmar?" ,
        "Answer" : "NAYPYITAW" } ,
    {
        "Question" : "What is capital of India?",
        "Answer" : "NEWDELHI" }
        ]

score = 0

print("==== PYTHON QUIZ ====")
for item in quiz_data:
    print(item["Question"])
    answer = input("Enter your answer: ").replace(" ", "").upper()
    if answer == item["Answer"] :
        print("Correct!")
        score += 1
    else:
         print("incorrect!")


print("==== RESULT ====")


total_questions = len(quiz_data)
if score == total_questions :
    print(f"Score: {score}/{total_questions}")
    print('Excellent!')
elif score >= total_questions * 0.6 :
    print(f"Score: {score}/{total_questions}")
    print('Good job!')
else :
     print(f"Score: {score}/{total_questions}")
     print('try again!')
