from questions import question_list
import random

prizes = ["10000", "20000", "30000", "40000", "50000", "100000", "2000000", "300000", "400000", "500000"]
i=0

print("\nWELCOME TO THE MILLIONAIRE GAME :)")
print("\nInstructions: Play the game or Type QUIT to exit the game anytime and keep the money you won\n")

for ques in question_list:
    print(ques["question"])
    print(ques["options"])

    q = str(input("\nEnter the correct answer or QUIT: ")).upper()

    if q=="QUIT":
        print(f"GAME OVER!!. \nPRIZE money you will get: {prizes[i]}")

    if(ques["answer"] == q):
        print("CORRECT ANSWER!!")
    else:
        print("\nWRONG ANSWER!!")
        print("BETTER LUCK NEXT TIME ):")
        break

    print(f"YOU WON :) {prizes[i]}\n")
    i+=1

if(i == len(question_list)):
    print(f"\nCongratulations! You Won{prizes[-1]}!!")