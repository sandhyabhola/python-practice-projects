import random

print("Welcome to our game world!🎉")

##### hint section #####
#hint for level1 and level2
def hint_l1(x):
    return "[It is an even number]" if x % 2 == 0 else "[It is an odd number]"
#super hint for level2 
def hint_l2(x):
    if x % 2 == 0:
        if 1 <= x <= 20:
            return "[It is an even number ! Range : 1 to 20]"
        elif 30 <= x <= 50:
            return "[It is an even number ! Range : 30 to 50]"
        elif 20 < x < 30:
            return "[It is an even number ! Range : 15 to 35]"
    else:
        if 1 <= x <= 20:
            return "[It is an odd number ! Range : 1 to 20]"
        elif 30 <= x <= 50:
            return "[It is an odd number ! Range : 30 to 50]"
        elif 20 < x < 30:
            return "[It is an odd number ! Range : 15 to 35]"
# hint for level3
def hint_l3(x):
    if x % 2 == 0:
        if 1 <= x <= 40:
            return "[It is an even number ! Range : 1 to 40]"
        elif 60 <= x <= 100:
            return "[It is an even number ! Range : 60 to 100]"
        elif 40 < x < 60:
            return "[It is an even number ! Range : 30 to 70]"
    else:
        if 1 <= x <= 40:
            return "[It is an odd number ! Range : 1 to 40]"
        elif 60 <= x <= 100:
            return "[It is an odd number ! Range : 60 to 100]"
        elif 40 < x < 60:
            return "[It is an odd number ! Range : 30 to 70]"
#super_hint_level3
def superhint_l3(x):
    prime = True
    if x <= 1:
        prime = False
    else:
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break

    if prime:
        if x % 2 == 0:
            return "[It is a unique prime number ! Range : 1 to 40 ]"
        else:
            if 1 <= x <= 40:
                return "[It is an odd prime number ! Range : 1 to 40]"
            elif 60 <= x <= 100:
                return "[It is an odd prime number ! Range : 60 to 100]"
            elif 40 < x < 60:
                return "[It is an odd prime number ! Range : 30 to 70]"
    else:
        if x % 2 == 0:
            if 1 <= x <= 40:
                return "[It is a composite even number ! Range : 1 to 40]"
            elif 60 <= x <= 100:
                return "[It is a composite even number ! Range : 60 to 100]"
            elif 40 < x < 60:
                return "[It is a composite even number ! Range : 30 to 70]"
        else:
            if 1 <= x <= 40:
                return "[It is a composite odd number ! Range : 1 to 40]"
            elif 60 <= x <= 100:
                return "[It is a composite odd number ! Range : 60 to 100]"
            elif 40 < x < 60:
                return "[It is a composite odd number ! Range : 30 to 70]"

##### review section #####
#level-1 Review
def review_easy(x, y):
    if abs(x - y) <= 2:
        return "Your guess was very close!"
    elif abs(x - y) <= 4:
        return "Your guess was close!"
    elif abs(x - y) <= 6:
        return "Your guess was far from the target!"
    elif abs(x - y) <= 10:
        return "Your guess was very far from the target!"
    else:
        return "Your guess was extremely far from the target!"
#level-2 Review
def review_medium(x, y):
    if abs(x - y) <= 5:
        return "Your guess was very close!"
    elif abs(x - y) <= 10:
        return "Your guess was close!"
    elif abs(x - y) <= 15:
        return "Your guess was far from the target!"
    elif abs(x - y) <= 25:
        return "Your guess was very far from the target!"
    else:
        return "Your guess was extremely far from the target!"
#level-3 Review  
def review_hard(x, y):
    if abs(x - y) <= 10:
        return "Your guess was very close!"
    elif abs(x - y) <= 20:
        return "Your guess was close!"
    elif abs(x - y) <= 30:
        return "Your guess was far from the target!"
    elif abs(x - y) <= 50:
        return "Your guess was very far from the target!"
    else:
        return "Your guess was extremely far from the target!"

##### attempts #####

def attempts_left(total_attempt, current_attempt):
    remain_attempt = total_attempt - current_attempt
    if remain_attempt:
        return f"Challenges Remaining : {remain_attempt}"
    else:
        return "You lost all the challenges.\nBetter luck next time!😲"

##### rating #####

def rate(r):
    r1 = ["1", "2", "3", "4", "5"]
    if r in r1:
        return '⭐' * int(r)
    return

##### feedback #####

def feed1(f1):
    
    # length check
    if not (5 <= len(f1) <= 100):
        return False
    # must not be empty or just spaces
    if not f1.strip():
        return False
    # must contain at least one letter
    if not any(ch.isalpha() for ch in f1):
        return False
    # must not be only numbers
    if f1.isdigit():
        return False
    else:
        return True


##### bonus chance #####
#bonus_chance for medium level
def bonus_chance1(l1):
    d1 = {"1": "Rock", "2": "Paper", "3": "Scissor"}
    while True:
        c1 = random.choice(l1)
        c2 = input("ROCK PAPER SCISSOR (1/2/3): ")
        if c2 in l1:
            if (c1, c2) in [("1", "2"), ("2", "3"), ("3", "1")]:
                print(f"computer:{d1[c1]}  You:{d1[c2]}\nYou win!\nBonus Chance unlocked!")
                return True
            elif c1 == c2:
                print(f"Computer:{d1[c1]}  You:{d1[c2]}\nDraw! Try again.")
                continue
            else:
                print(f"computer:{d1[c1]}  You:{d1[c2]}\nComputer wins! Bonus lost.")
                return False
        else:
            print("Invalid Choice!")
#bonus_chance for Hard level
def bonus_chance2(l1):
    d1 = {"1": "Snake", "2": "Water", "3": "Gun"}
    while True:
        c1 = random.choice(l1)
        c2 = input("Snake Water Gun (1/2/3): ")
        if c2 in l1:
            if (c1, c2) in [("1", "3"), ("2", "1"), ("3", "2")]:
                print(f"computer:{d1[c1]}  You:{d1[c2]}\nYou win!\nBonus Chance unlocked!")
                return True
            elif c1 == c2:
                print(f"Computer:{d1[c1]}  You:{d1[c2]}\nDraw! Try again.")
                continue
            else:
                print(f"computer:{d1[c1]}  You:{d1[c2]}\nComputer wins! Bonus lost.")
                return False
        else:
            print("Invalid Choice!")
#Ask play again Input valid check
def ask_replay(message="Do you want to play another round? (yes/no): "):
    while True:
        again = input(message).strip().lower()
        if again in ["yes", "no"]:
            return again
        else:
            print("Please enter valid response (yes/no).")


# --- (keep all your hint, review, attempts, rating, feedback, bonus functions as they are) ---

def main_game(level_name, limit, hint_function, review_function, medal_message, start_message="You have 3 Challenges to win the game.🤞"):
    MAX_ATTEMPTS = 3
    print(f"Welcome to level {level_name}!")
    print(start_message)
    for i in range(1, MAX_ATTEMPTS+1):
        while True:
            try:
                n1 = random.randint(1, limit)
                
                print(f"Hint: {hint_function(n1)}")
                n2 = int(input(f"Guess the number (between 1,{limit}):"))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if n2 <= 0 or n2 > limit:
                print("Number out of range!")
                continue
            break

        if n1 == n2:
            print("\033[92m")
            print(medal_message)
            print("\033[0m")
            return True
        else:
            print("You lost this round 😔")
            print(f"Review: {review_function(n2, n1)}")
            print(attempts_left(MAX_ATTEMPTS , i))
    return False

# --- Game Flow ---
# --- Progressive Mode Only ---
while True:

    # Easy Level
    easy_result = main_game("1", 20, hint_l1, review_easy, "Congratulation! You win The Easy level🥉")
    if not easy_result:
        again = ask_replay("You lost Easy Level. Do you want to play again? (yes/no): ")
        if again == "yes":
            continue
        else:
            break

    # Medium Level
    medium_result = main_game("2", 50, hint_l1, review_medium, "Congratulation! You win The Medium level🥈")
    if not medium_result:
        print("Bonus Chance: Rock Paper Scissor")
        bonus_result1 = bonus_chance1(["1", "2", "3"])
        if bonus_result1:
            # Bonus Medium Level must be won before Hard Level
            bonus_level2 = main_game("2 Bonus", 50, hint_l2, review_medium, "🥈Congratulation! You win the Bonus Medium level!")
            if bonus_level2:
                hard_result = main_game("3", 100, hint_l3, review_hard, "Congratulation! You win The Hard level🥇")
            else:
                again = ask_replay("You lost Bonus Round For Medium Level.Do you want to Play again? (yes/no): ")
                if again == "yes":
                    continue
                else:
                    break
        else:
            again = ask_replay("You lost Medium Level Bonus Chance.Do you want to Play again? (yes/no): ")
            if again == "yes":
                continue
            else:
                break
    else:
        hard_result = main_game("3", 100, hint_l3, review_hard, "Congratulation! You win The Hard level🥇")

    # Hard Level
    if not hard_result:
        print("Bonus Chance: Snake Water Gun")
        bonus_result2 = bonus_chance2(["1", "2", "3"])
        if bonus_result2:
            # Bonus Hard Level must be won before Reward
            bonus_level3 = main_game("3 Bonus", 100, superhint_l3, review_hard, "🥇Congratulation! You win the Bonus Hard level!")
            if bonus_level3:
                print("\033[92m")
                print("🏆 GOLD MEDAL AWARDED 🎉")
                print("\033[0m")
                break
            else:
                again = ask_replay("You lost Bonus Round For Hard Level.Do you want to Play again? (yes/no): ")
                if again == "yes":
                    continue
                else:
                    break
        else:
            again = ask_replay("You lost Hard  Level Bonus Chance.Do you want to Play again? (yes/no): ")
            if again == "yes":
                continue
            else:
                break
    else:
        print("\033[92m")
        print("🏆 GOLD MEDAL AWARDED 🎉")
        print("\033[0m")
        break


# --- Rating Section ---
while True:
    review = input("How much ratings do you want to give (1-5): ")
    if review in ["1", "2", "3", "4", "5"]:
        print(f"Ratings: {rate(review)}")
        print("Thank you for your valuable response!")
        break
    else:
        print("Please enter a valid response!")

# --- Feedback Section ---
while True:
    feedback = input("Enter feedback: ")
    if feed1(feedback):
        print(f"Feedback: {feedback}")
        print("Thank you for your feedback.\nWe will improve using your valuable response!")
        break
    else:
        print("Enter valid feedback (5–100 characters).")













        #this is our phase1 project for learning purpose
