# 🎮 Number Guessing Game (Progressive Mode)

A console-based number guessing game written in Python. The player moves through three levels in order (Easy, Medium and Hard) and can earn bonus chances by winning a mini-game.

This is a **practice project** built while learning Python. It is a simplified version of the game with a single, fixed progression and no level selection menu.

---

## Features

- Three levels played in order: Easy, then Medium, then Hard
- Hint system that gets more detailed at higher levels
- Review messages that tell you how close your guess was
- Bonus chances through Rock Paper Scissors and Snake Water Gun
- Super hints in bonus rounds (range hints and prime/composite hints)
- Input validation and error handling
- Replay option after losing, with a message that says where you lost
- Star rating and feedback section at the end

---

## Levels

| Level  | Number Range | Challenges | Hint                                    |
|--------|--------------|------------|-----------------------------------------|
| Easy   | 1 to 20      | 3          | Even or odd                             |
| Medium | 1 to 50      | 3          | Even or odd                             |
| Hard   | 1 to 100     | 3          | Even or odd + range                     |

Each challenge uses a fresh random number. Winning any one of the 3 challenges wins the level.

---

## How the Game Flows

1. **Easy:** win to move on to Medium. If you lose, you can replay from the start.
2. **Medium:** win to move on to Hard. If you lose, you get a bonus chance.
3. **Medium bonus:** win Rock Paper Scissors to unlock a Bonus Medium round with a range hint. Win it to continue to Hard.
4. **Hard:** win to get the Gold Medal. If you lose, you get a bonus chance.
5. **Hard bonus:** win Snake Water Gun to unlock a Bonus Hard round with a super hint (prime or composite, even or odd, plus range). Win it to get the Gold Medal.

Whenever you lose a round or a bonus, the game asks whether you want to play again. At the end you rate the game from 1 to 5 stars and leave short feedback (5 to 100 characters).

---

## Concepts Practiced

- Variables, data types and operators
- Conditional statements and loops
- Functions and return values
- Lists, dictionaries and strings
- `random` module
- Exception handling (`try` / `except`)
- User input validation
- Managing program flow across multiple levels

---

## How to Run

Requirements: Python 3.x (no extra libraries needed).

```bash
python real_game.py
```

The game uses emojis and colored terminal text, so use a terminal that supports UTF-8.

---

## Project Structure

```
real_game.py   # complete game in a single file
```

Inside the file the code is split into functions for:

- Hints (`hint_l1`, `hint_l2`, `hint_l3`, `superhint_l3`)
- Reviews (`review_easy`, `review_medium`, `review_hard`)
- Bonus mini-games (`bonus_chance1`, `bonus_chance2`)
- Attempts, rating and feedback validation
- The main game loop (`main_game`)

---

## Difference from `game_1.py`

`game_1.py` lets the player choose the starting level. This version always starts at Easy and follows one progression path, which keeps the game flow simpler and cleaner.

---

## Notes

This is a learning project from my Python practice phase. The code is intentionally simple and function-based.