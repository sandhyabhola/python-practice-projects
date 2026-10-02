import random
from quiz_question_bank import Python,Math,AI_ML
Python=Python
Math=Math
AIML=AI_ML


#-------option validation----------
def option_validation(option="User_Answer: "):
    while True:
        op=input(option).strip().upper()
        if op in ["A","B","C","D"]:
            return op
        else:
            print("Please enter a valid option (A/B/C/D).")


#----------score_system----------
def score_system(category_name,level_name,Total_score,score,score_per_point,percentage,correct=0,wrong=0):
    print("=" * 60)
    print("        Score Board")
    print("="*60)
    print(f"User ID: {user_id}")
    # print(f"Category : {category_name}")
    print(f"Difficulty : {level_name}")

    print("-"*60)
    print(f"Score: {score}/{Total_score}")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"percentage:{round(percentage,0)}%")
    

#Answer Review Input valid Check
def answer_review(message="Do You want to se your answers? (yes/no):"):
    while True:
        review=input(message).strip().lower()
        if review in ["yes","no"]:
            return review
        else:
            print("Enter a valid response!")



#Ask play again Input valid Check
def ask_replay(message="Do you want to play another round? (yes/no):"):
    while True:
        again=input(message).strip().lower()
        if again in ["yes","no"]:
            return again
        else:
            print("Please enter valid response (yes/no).")

#----------user_id validation-----
def user_id_validation(user_id):
    
    if not (3<=len(user_id)<=15):
        return False
    if not user_id.strip():
        return False
    if not any(ch.isalpha() for ch in user_id):
        return False
    if user_id.isdigit():
        return False
    else:
        return True

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


#grade system according their percentage score
def grade(score_percent):
    if 90<=score_percent<=100:
        return"Grade A+"
    elif 80<=score_percent<90:
        return "Grade A"
    elif 70<=score_percent<80:
        return "Grade B+"
    elif 60<=score_percent<70:
        return "Grade B"
    elif 50<=score_percent<60:
        return "Grade C"
    else:
        return "Grade D"
#final report pass/fail system
def result(score_p):
    if score_p>=80:
        return "Pass"
    else:
        return "Fail"


#---------Final report---------
def final_report(category_tag,level_name):
    final_percentage=round((final_score/final_total_score)*100,2)

    print("="* 60)
    print("Final Report")
    print("="* 60)
    print(f"User ID: {user_id}")
    print(f"Category: {category_tag}")
    print(f"Difficulty: {level_name}")
    
    print("-"*60)
    print(f"Total_questions:{final_total_questions}")
    print(f"Correct Answers:{final_correct_answer}")
    print(f"Wrong Answer:{final_wrong_answer}")
    print(f"Total Score: {final_total_score}")
    print("-"*60)
    print(f"🏆 Score :{final_score}/{final_total_score}")
    print(f"📈 Percentage:{round(final_percentage,0)}%")
    print(f"🎖️ Result :{result(final_percentage)}")
    print(f"⭐ Grade :{grade(final_percentage)}")
    print("="* 60)
    print("Thank you For playing!")
    print("="* 60)

#-------Review Section-----
def display_review(level_result):
    review=answer_review()
    if review=="yes":
        
        for reviews in level_result["review"]:
            user_answer=reviews['Your_Answer']
            correct_answer=reviews['Correct_Answer']
            print(f"Q: {reviews['Q']}")
            print(f"Your Answer: {user_answer}")
            print(f"Correct Answer: {correct_answer}")
            if user_answer==correct_answer:
                
                print("✅ correct")
            else:
                print("❌ Incorrect")
                
            print(f"Explanation:{reviews['Explanation']}")
            print("="*60)
           
#Global variables for final report initialization
final_total_questions=0
final_correct_answer=0
final_wrong_answer=0
final_score=0
final_total_score=0

    
#----------Main Game-------------
def main_game(category_data,level_name,Total_questions=10,score_per_point=5,pass_percent=80):
    

    global final_correct_answer
    global final_wrong_answer
    global final_score
    global final_total_score
    global final_total_questions



    correct=0 #local
    wrong=0 # local
    review_section=[]
    
    
    questions_list=category_data[level_name]
    selected_questions=random.sample(questions_list,Total_questions)
    
    for questions in selected_questions:
        print(f"Q: {questions['Q']}")
        option=questions['options']
        ans=questions['Answer']
        Answer_value=option[ans]

        key=list(option.keys())
        value=list(option.values())
        new_option=dict(zip(key,value))
        for keys,values in new_option.items():
            print(f"{keys}. {values}")
        
        user=option_validation("Select your Answer (A/B/C/D):")
        print("-"*60)
        if new_option[user]==Answer_value:
            correct+=1
            final_correct_answer+=1
        else:
            wrong+=1
            final_wrong_answer+=1

        review_section.append({"Q":questions['Q'],
                               "Your_Answer":new_option[user],
                               "Correct_Answer":Answer_value,
                               "Explanation":questions['Explanation']
                               })
    
    
    #-------Score calculation for per level---------
    Total_Score=Total_questions*score_per_point
    score=correct*score_per_point
    percentage=(score/Total_Score)*100
    

    #----Score calculation for final report (multiple level)-------
    final_total_questions+=Total_questions
    final_total_score+=Total_Score
    final_score+=score
    
    #--------Level score display------
    score_system(category_data,level_name,Total_Score,score,score_per_point,percentage,correct,wrong)
    
    if percentage>=pass_percent:
        print(f"Successfully completed {level_name} Level.")
        print(f"Status: Qualified")
    else:
        print(f"You loose the {level_name} Level.")
        print(f"Status: DisQualified")
    print("=" *20)

    

    #--- Return stats for final_report ---
    return {
    "level": level_name,
    "score": score,
    "percentage": percentage,
    "passed": percentage >= pass_percent,
    "review": review_section
}
#------------Game Folw For All category------------

def play_category(category_name,category_tag):
    while True:
        #------------easy level------------
        print("="*60)
        print(f"            {category_tag} Easy Section")
        print("="*60)
        easy_result=main_game(category_name,"Easy")
        display_review(easy_result)
        if not easy_result["passed"]:
            again = ask_replay(f"You lost Easy Level in {category_tag}.\nDo you want to play again? (yes/no): ")
            if again == "yes":
                continue
            else:
                break
        #------------Medium Level------------
        print("="*60)
        print(f"           {category_tag} Medium Section")
        print("="*60)
        medium_result=main_game(category_name,"Medium")
        display_review(medium_result)
        print()
        # final_report(category_tag,"Medium")
        if not medium_result["passed"]:
            final_report(category_tag,"Medium")
            again = ask_replay(f"You lost Medium Level in {category_tag}.\nDo you want to play again? (yes/no): ")
            if again == "yes":
                continue
            else:
                break
        
        #------------Hard Level------------
        print("="*60)
        print(f"              {category_tag} Hard Section")
        print("="*60)
        hard_result=main_game(category_name,"Hard")
        display_review(hard_result)
        print()
        final_report(category_tag,"Hard")
        if not hard_result["passed"]:
            again = ask_replay(f"You lost Hard Level in {category_tag}.\nDo you want to play again? (yes/no): ")
            if again == "yes":
                continue
            else:
                break
        print(f"Congratulations! You completed all {category_tag} levels.")
        break

#---------welcome message---------
print("Welcome to Quiz World!")

#-------User ID-------
while True:
    user_id=input("Create User ID:")
    if user_id_validation(user_id):
        break
    else:
        print("This ID is invalid. Enter a valid ID.")

print("="*30)
print(f"User ID:{user_id}")
print("="*30)
#-----Game flow Category wise----------

while True:
    print("Select your category to start the quiz.")
    print("1.Python\n2.Mathematics\n3.AIML")
    category_choice=input("Select Category (1/2/3):")
    if category_choice in ["1","2","3"]:
        if category_choice=="1":
            print(f"Topic confirmed: Python .\nLet’s begin our Python quiz!")
            play_category(Python,"Python")
            break
        elif category_choice=="2":
            print(f"Topic confirmed: Mathematics .\nLet’s begin our Mathematics quiz!")
            play_category(Math,"Math")
            break
        elif category_choice=="3":
            print(f"Topic confirmed: AIML \nLet’s begin our AIML quiz!")
            play_category(AIML,"AIML")
            break
        else:
            break
    else:
        print("Please Select a valid category!")


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


#---------complete------------------