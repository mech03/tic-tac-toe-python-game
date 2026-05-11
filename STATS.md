# Game Statistics

This file describes all the statistics that are tracked during the game and where to find them in the code.

---

## What is tracked

| Statistic | Variable | Description |
|---|---|---|
| Player 1 Wins | `player1_wins` | Total number of games Player 1 has won |
| Player 2 Wins | `player2_wins` | Total number of games Player 2 (or Computer) has won |
| Draws | `draws` | Total number of games that ended in a draw |
| Player 1 Streak | `player1_streak` | How many games in a row Player 1 has won |
| Player 2 Streak | `player2_streak` | How many games in a row Player 2 has won |

---

## How they work

All five variables are **global counters** — they are defined at the top of the file, outside all functions, so every function can read and update them.

```python
player1_wins   = 0
player2_wins   = 0
draws          = 0
player1_streak = 0
player2_streak = 0
```

They are updated inside `play_game()` after every game:
- When someone wins → their wins and streak go up by 1, the other player's streak resets to 0
- When it's a draw → draws goes up by 1, both streaks reset to 0

---

## When they are displayed

Stats are printed after every game using the `print_stats()` function, and again at the end when the player chooses not to play again.

Example output:
```
--- Stats ---
Amechi wins: 3  (streak: 2)
Computer wins: 1  (streak: 0)
Draws: 1
```

---

## Where to find it in the code

| Function | Location | What it does with stats |
|---|---|---|
| `play_game()` | `Tic Tac Toe.py` line 74 | Updates all counters after each game |
| `print_stats()` | `Tic Tac Toe.py` line 47 | Displays all stats to the player |

---

## Note on persistence

Stats are tracked **within a single session** only. Once the program ends the counters reset back to zero. To save stats permanently between sessions a file or database would be needed — this was beyond the scope of this project.
