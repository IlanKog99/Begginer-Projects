# All-In-One Beginner Projects Collection

Welcome to my collection of Python beginner projects! This repository contains several small games and utilities that I created while learning Python. I've decided to refine, refactor, and combine them into a single application to showcase my growth as a programmer.

## What's Inside?

This collection includes:

- **Tic-Tac-Toe**: A classic game of X's and O's, against a friend or an AI that knows how to win and block
- **Rock-Paper-Scissors**: Play against a friend or challenge the computer
- **Number Guessing Game**: Try to guess the random number within a set number of attempts
- **Coin Flip**: A simple coin flipper that keeps count of heads and tails
- **Temperature Converter**: Convert between Celsius and Fahrenheit
- **Simple Calculator**: Perform basic arithmetic operations
- **Dice Roller**: Roll one or more dice with any number of sides

## About This Project

These were some of my first Python projects, and I wanted to preserve them while also demonstrating how my coding skills have improved. I've refactored the code to be cleaner while keeping it **beginner-friendly and easy to read**:

- Each project is its own class with a single `play()` method
- Shared input helpers (`ask_int`, `ask_float`, `ask_yes_no`) so every project validates input the same way
- Simple loops instead of menus calling each other
- Plain data structures (dictionaries and lists) instead of clever tricks
- Short comments that explain *why*, not just *what*

## How to Use

You need Python 3 installed. No extra packages are required.

```bash
python AIO_begginer_projects_refined.py
```

Pick a project from the menu by typing its number. Press `Ctrl+C` at any time to quit.

## Reading the Code

Everything lives in one file, split into clearly marked sections:

1. **Helper functions** at the top: small tools every project uses
2. **One class per project**, numbered to match the menu
3. **`GameSuite`** at the bottom: shows the menu and starts the chosen project

A good way to learn is to pick one project, read its `play()` method first, then look at the methods it calls.

## My Learning Journey

This collection represents my journey from writing my first "Hello World" to understanding object-oriented programming concepts. While the applications are simple, they demonstrate fundamental programming concepts like:

- Control flow and logic
- Function and class design
- Data validation
- User input processing
- Basic AI implementation

I hope this collection inspires other beginning programmers to keep refining their skills and to not be afraid of looking back at early code to see how far they've come!

## Feedback

If you have any suggestions or feedback on how I could improve these projects further, feel free to open an issue or submit a pull request. I'm always looking to learn and grow as a developer!

Happy coding! 😊 