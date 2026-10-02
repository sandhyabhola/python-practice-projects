# 🧠 Quiz World (Console Quiz Game)

A console-based multiple-choice quiz game written in Python. The player creates a User ID, chooses a category and then clears three levels (Easy, Medium and Hard) by scoring well enough at each one.

This is a **practice project** built while learning Python. It uses only core Python concepts and the standard library.

---

## Features

- Three categories: Python, Mathematics and AIML
- Three levels per category: Easy, Medium and Hard
- 10 multiple-choice questions per level (A/B/C/D)
- Question order is randomized every time you play
- User ID creation with validation
- Input validation for options, replay and review
- Score board after every level
- Answer review with correct answers and explanations
- Final report with total score, percentage, Pass/Fail result and grade
- Replay option after losing a level
- Star rating and feedback section at the end

---

## How the Game Works

1. Enter a User ID (3 to 15 characters, must contain at least one letter, cannot be only numbers).
2. Choose a category: Python, Mathematics or AIML.
3. Play the levels in order: **Easy, then Medium, then Hard**.
4. After each level you see a score board and can choose to review your answers with explanations.
5. You need **80% or more** to qualify and move to the next level.
6. If you fail a level, you can choose to play again (the category restarts from Easy).
7. After the game, rate it from 1 to 5 stars and leave short feedback (5 to 100 characters).

---

## Scoring

| Item                     | Value        |
|--------------------------|--------------|
| Questions per level      | 10           |
| Points per correct answer| 5            |
| Maximum score per level  | 50           |
| Pass mark                | 80% (40/50)  |

### Grades

| Percentage | Grade    |
|------------|----------|
| 90 to 100  | Grade A+ |
| 80 to 89   | Grade A  |
| 70 to 79   | Grade B+ |
| 60 to 69   | Grade B  |
| 50 to 59   | Grade C  |
| Below 50   | Grade D  |

The final report shows total questions, correct and wrong answers, total score, percentage, Pass/Fail result and grade.

---

## Concepts Practiced

- Variables, data types and operators
- Conditional statements and loops
- Functions and return values
- Lists and dictionaries (nested)
- Importing from another file (modules)
- `random` module (`random.sample`)
- Global variables
- User input validation
- Organizing code into separate files

---

## How to Run

Requirements: Python 3.x (no extra libraries needed).

Keep both files in the same folder, then run:

```bash
python main.py
```

The game uses emojis in the final report, so use a terminal that supports UTF-8.

---

## Project Structure

```
quiz-world/
├── main.py                 # game logic, scoring, reports
└── quiz_question_bank.py   # all questions (Python, Math, AI_ML)
```

### main.py

Contains the functions for:

- Option, replay, review and User ID validation
- Score board (`score_system`)
- Grade and Pass/Fail logic (`grade`, `result`)
- Final report (`final_report`)
- Answer review (`display_review`)
- Running one level (`main_game`) and a full category (`play_category`)
- Rating and feedback

### quiz_question_bank.py

Stores the questions as Python dictionaries, grouped by category and level. Each question looks like this:

```python
{
    "Q": "Which function is used to display output in Python?",
    "options": {"A": "display()", "B": "show()", "C": "print()", "D": "output()"},
    "Answer": "C",
    "Explanation": "The print() function is used to display output on the screen."
}
```

To add questions, append more dictionaries in the same format to the right list.

---

## Notes

This is a learning project from my Python practice phase. The code is intentionally simple and function-based.