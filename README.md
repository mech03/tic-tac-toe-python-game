# Tic-Tac-Toe 🎮

A two-player Tic-Tac-Toe game built in Python as my first project on the Rockborne Data Engineering course.
You can play against a friend or go up against the computer!

---

## Project Folder Structure

```
04 Python-2/
│
├── Tic Tac Toe.py        ← the game code
├── README.md             ← this file
└── STATS.md              ← details on all statistics tracked in the game
```

---

## How to Run

Open `Tic Tac Toe.py` in VS Code (or any Python editor) and run it.
No extra libraries needed apart from `random` which comes built into Python.

---

## How to Play

When you run the game it will ask you to pick a mode:
- **1** — Two players (you and a friend take turns)
- **2** — vs Computer (you play against a random computer)

Each player then enters their name. Player 1 is always **X** and Player 2 (or Computer) is always **O**.

The board is numbered 1 to 9 like this:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

On your turn just type the number of the spot you want to place your marker.
First to get **3 in a row** — across, down or diagonal — wins.
If all 9 spots are filled with no winner it's a **draw**.

---

## Statistics

The game tracks the following stats across all rounds in a session:
- Wins per player
- Draws
- Win streaks

Stats are displayed after every game and at the end of the session.

Full details on all statistics, variable names and where they live in the code can be found in **[STATS.md](STATS.md)**.

---

## Features

- Two game modes — play with a friend or vs the Computer
- Input validation — handles letters, symbols, numbers out of range and spots already taken
- Win streaks — tracks how many games in a row each player has won
- Stats after every game — wins, draws and streaks displayed
- Play again option — keep playing without restarting the program

---

## What I Used

Everything in this project was built using what I learned on the course:

- **Lists** — the board is a list of 9 spaces
- **Functions** — the code is split into functions to keep it clean and readable
- **Global variables** — counters for wins, draws and streaks that every function can access
- **While loops** — to keep the game going and to validate inputs
- **If/else** — to check winners, draws and switch players
- **Try/except** — to catch any bad inputs without crashing the game
- **For loops** — to check all 8 winning lines and find empty spots for the computer

---

## GitHub

This project was uploaded manually to GitHub due to authentication issues with the GitHub CLI.
Commit history can be viewed directly in the repository.

---