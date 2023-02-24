#!/usr/bin/env python3
import html
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
         }

# question
question = trivia["question"]

# correct answer
correct_answer = html.unescape(trivia["correct_answer"])

# incorrect answer #1 
incorrect_1 = html.unescape(trivia["incorrect_answers"][0])

# incorrect answer #2
incorrect_2 = html.unescape(trivia["incorrect_answers"][1])

# incorrect answer #3
incorrect_3 = html.unescape(trivia["incorrect_answers"][2])


print(f"the question is: {question} \n")

print(f"A : {correct_answer} \n")

print(f"B : {incorrect_1} \n")

print(f"C : {incorrect_2} \n")

print(f"D : {incorrect_3} \n")

choice = input("Choose the correct answer: ").lower()

if choice == 'A'.lower():
    print("That's correct!")
else:
    print(f"Nice try, the answer was A: {correct_answer}")
