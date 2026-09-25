"""
All-In-One Beginner Projects
============================

A collection of small games and tools in one file:

    1. Tic-Tac-Toe
    2. Rock-Paper-Scissors
    3. Number Guessing Game
    4. Coin Flip
    5. Temperature Converter
    6. Simple Calculator
    7. Dice Roller

Run it with:  python AIO_begginer_projects_refined.py

Every project is its own class with a play() method.
The GameSuite class at the bottom shows a menu and calls play() on the chosen project.
"""

import os
import random
import time


# ---------------------- HELPER FUNCTIONS ----------------------
# Small functions that several projects use.

def clear_screen():
    """Clear the terminal ("cls" on Windows, "clear" everywhere else)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Wait until the user presses Enter."""
    input("\nPress Enter to continue...")


def ask_yes_no(question):
    """Keep asking until the user answers yes or no. Returns True for yes."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'yes' or 'no'.")


def ask_int(question, min_value=None, max_value=None):
    """Keep asking until the user types a whole number inside the allowed range."""
    while True:
        try:
            number = int(input(question))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if min_value is not None and number < min_value:
            print(f"The number must be at least {min_value}.")
        elif max_value is not None and number > max_value:
            print(f"The number must be at most {max_value}.")
        else:
            return number


def ask_float(question):
    """Keep asking until the user types a number (decimals allowed)."""
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Please enter a number.")


def format_number(number):
    """Show 4.0 as 4 and round long decimals, e.g. 0.30000000000000004 -> 0.3."""
    number = round(number, 10)
    if number == int(number):
        return str(int(number))
    return str(number)


# ---------------------- 1. TIC-TAC-TOE ----------------------

class TicTacToe:
    # Every group of 3 squares that wins the game (squares are numbered 1-9).
    WINNING_LINES = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7),             # diagonals
    ]

    def reset(self):
        """Start a fresh game."""
        # The board is a dictionary: square number -> what's in it ("1".."9", "X" or "O").
        self.board = {square: str(square) for square in range(1, 10)}
        self.current_player = "X"

    def print_board(self):
        b = self.board
        print(f"\n {b[1]} | {b[2]} | {b[3]}")
        print("---+---+---")
        print(f" {b[4]} | {b[5]} | {b[6]}")
        print("---+---+---")
        print(f" {b[7]} | {b[8]} | {b[9]}\n")

    def free_squares(self):
        """Return a list of the squares nobody has taken yet."""
        return [square for square in self.board if self.board[square] not in ("X", "O")]

    def get_winner(self):
        """Return "X" or "O" if someone won, otherwise None."""
        for a, b, c in self.WINNING_LINES:
            if self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def human_move(self):
        while True:
            square = ask_int(f"Player {self.current_player}, choose a square (1-9): ", 1, 9)
            if square in self.free_squares():
                return square
            print("That square is already taken. Try another one.")

    def ai_move(self):
        """
        A simple AI:
        1. If it can win right now, it does.
        2. If the human could win on their next move, it blocks them.
        3. Otherwise it picks a random free square.
        """
        opponent = "X" if self.current_player == "O" else "O"

        for player in (self.current_player, opponent):
            for square in self.free_squares():
                self.board[square] = player            # try the move...
                wins = self.get_winner() == player
                self.board[square] = str(square)       # ...then undo it
                if wins:
                    return square

        return random.choice(self.free_squares())

    def play(self):
        clear_screen()
        print("Tic-Tac-Toe")
        against_ai = ask_yes_no("Do you want to play against the AI?")

        while True:
            self.reset()

            # One loop turn = one move. Stop when someone wins or the board is full.
            while True:
                clear_screen()
                self.print_board()

                if against_ai and self.current_player == "O":
                    square = self.ai_move()
                else:
                    square = self.human_move()
                self.board[square] = self.current_player

                winner = self.get_winner()
                if winner or not self.free_squares():
                    break

                # Switch turns
                self.current_player = "O" if self.current_player == "X" else "X"

            clear_screen()
            self.print_board()
            if winner:
                print(f"Player {winner} wins!")
            else:
                print("It's a tie!")

            if not ask_yes_no("\nWould you like to play again?"):
                break


# ---------------------- 2. ROCK-PAPER-SCISSORS ----------------------

class RockPaperScissors:
    CHOICES = ["rock", "paper", "scissors"]

    # What each choice beats: rock beats scissors, and so on.
    BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    def __init__(self):
        self.two_players = False
        self.ask_names = True
        self.set_default_names()

    def set_default_names(self):
        self.player1 = "Player 1"
        self.player2 = "Player 2" if self.two_players else "The Bot"
        self.names_entered = False
        self.reset_scores()

    def reset_scores(self):
        self.score1 = 0
        self.score2 = 0

    def ask_choice(self, player_name):
        """Ask a player for rock, paper or scissors. Accepts 1/2/3, r/p/s or the full word."""
        shortcuts = {"1": "rock", "r": "rock",
                     "2": "paper", "p": "paper",
                     "3": "scissors", "s": "scissors"}
        while True:
            answer = input(f"{player_name}, choose 1. Rock  2. Paper  3. Scissors: ").strip().lower()
            answer = shortcuts.get(answer, answer)
            if answer in self.CHOICES:
                return answer
            print("Invalid choice. Please try again.")

    def enter_names(self):
        clear_screen()
        self.player1 = input("Player 1, enter your name: ").strip() or "Player 1"
        if self.two_players:
            self.player2 = input("Player 2, enter your name: ").strip() or "Player 2"
            print(f"\nHello {self.player1} and {self.player2}!")
        else:
            print(f"\nHello {self.player1}! You'll be playing against {self.player2}.")
        self.names_entered = True
        self.reset_scores()
        pause()

    def play_round(self):
        clear_screen()
        choice1 = self.ask_choice(self.player1)

        if self.two_players:
            clear_screen()  # hide player 1's choice from player 2
            choice2 = self.ask_choice(self.player2)
        else:
            choice2 = random.choice(self.CHOICES)

        clear_screen()
        print(f"{self.player1} chose {choice1}.")
        print(f"{self.player2} chose {choice2}.\n")

        if choice1 == choice2:
            print("It's a tie!")
        elif self.BEATS[choice1] == choice2:
            print(f"{self.player1} wins!")
            self.score1 += 1
        else:
            print(f"{self.player2} wins!")
            self.score2 += 1

        self.print_scores()

    def print_scores(self):
        print(f"\nScore: {self.player1} {self.score1} - {self.score2} {self.player2}")

    def settings(self):
        while True:
            clear_screen()
            print("Settings")
            print(f"1. Ask for names:  {'On' if self.ask_names else 'Off'}")
            print(f"2. Two players:    {'On' if self.two_players else 'Off'}")
            print("3. Reset to default settings")
            print("4. Back")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.ask_names = not self.ask_names
                self.set_default_names()
            elif choice == "2":
                self.two_players = not self.two_players
                self.set_default_names()
            elif choice == "3":
                self.two_players = False
                self.ask_names = True
                self.set_default_names()
            elif choice == "4":
                return

    def play(self):
        while True:
            clear_screen()
            print("Rock, Paper, Scissors!")
            print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")
            print("1. Play")
            print("2. Settings")
            print("3. Back to Main Menu")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                if self.ask_names and not self.names_entered:
                    self.enter_names()
                while True:
                    self.play_round()
                    if not ask_yes_no("\nPlay another round?"):
                        break
            elif choice == "2":
                self.settings()
            elif choice == "3":
                return


# ---------------------- 3. NUMBER GUESSING GAME ----------------------

class NumberGuessingGame:
    def play(self):
        clear_screen()
        print("Number Guessing Game")

        while True:
            lowest = ask_int("\nEnter the lowest number of the range: ")
            highest = ask_int("Enter the highest number of the range: ", min_value=lowest)
            max_attempts = ask_int("How many attempts would you like? ", min_value=1)

            secret = random.randint(lowest, highest)
            guesses = []
            print(f"\nI'm thinking of a number between {lowest} and {highest}.")
            print(f"You have {max_attempts} attempts to guess it.")

            while len(guesses) < max_attempts:
                guess = ask_int(f"\nAttempt {len(guesses) + 1}: ", lowest, highest)
                guesses.append(guess)

                if guess == secret:
                    break
                elif guess < secret:
                    print("Too low!")
                else:
                    print("Too high!")

            won = guesses[-1] == secret
            if won:
                tries = "try" if len(guesses) == 1 else "tries"
                print(f"\nCorrect! You guessed it in {len(guesses)} {tries}.")
            else:
                print(f"\nYou've run out of attempts! The number was {secret}.")

            print("\nGame Summary")
            print(f"- Secret number: {secret}")
            print(f"- Your guesses:  {guesses}")
            print(f"- Even guesses:  {[g for g in guesses if g % 2 == 0]}")
            print(f"- Odd guesses:   {[g for g in guesses if g % 2 != 0]}")

            if not ask_yes_no("\nDo you want to play again?"):
                break


# ---------------------- 4. COIN FLIP ----------------------

class CoinFlip:
    def play(self):
        clear_screen()
        print("Coin Flip")
        heads = 0
        tails = 0

        while True:
            input("\nPress Enter to flip a coin...")
            print("Flipping...")
            time.sleep(0.5)  # a short pause for suspense

            result = random.choice(["Heads", "Tails"])
            if result == "Heads":
                heads += 1
            else:
                tails += 1

            print(f"The coin landed on {result}!")
            print(f"So far: {heads} heads, {tails} tails.")

            if not ask_yes_no("\nDo you want to flip again?"):
                break


# ---------------------- 5. TEMPERATURE CONVERTER ----------------------

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def play(self):
        clear_screen()
        print("Temperature Converter")

        while True:
            print("\n1. Celsius -> Fahrenheit")
            print("2. Fahrenheit -> Celsius")
            direction = ask_int("Choose 1 or 2: ", 1, 2)
            temperature = ask_float("Enter the temperature: ")

            if direction == 1:
                result = self.celsius_to_fahrenheit(temperature)
                print(f"{format_number(temperature)}°C = {result:.1f}°F")
            else:
                result = self.fahrenheit_to_celsius(temperature)
                print(f"{format_number(temperature)}°F = {result:.1f}°C")

            if not ask_yes_no("\nDo you want to convert another temperature?"):
                break


# ---------------------- 6. SIMPLE CALCULATOR ----------------------

class SimpleCalculator:
    def calculate(self, a, operator, b):
        """Return the result, or None if the calculation is impossible (dividing by zero)."""
        if operator == "+":
            return a + b
        if operator == "-":
            return a - b
        if operator == "*":
            return a * b
        if operator == "/":
            if b == 0:
                return None
            return a / b

    def play(self):
        clear_screen()
        print("Simple Calculator")

        while True:
            a = ask_float("\nEnter the first number: ")

            operator = input("Enter an operator (+, -, *, /): ").strip()
            while operator not in ("+", "-", "*", "/"):
                operator = input("Please enter +, -, * or /: ").strip()

            b = ask_float("Enter the second number: ")

            result = self.calculate(a, operator, b)
            if result is None:
                print("Error: you can't divide by zero.")
            else:
                print(f"{format_number(a)} {operator} {format_number(b)} = {format_number(result)}")

            if not ask_yes_no("\nDo you want to do another calculation?"):
                break


# ---------------------- 7. DICE ROLLER ----------------------

class DiceRoller:
    def play(self):
        clear_screen()
        print("Dice Roller")

        while True:
            sides = ask_int("\nHow many sides does each die have? ", min_value=2)
            count = ask_int("How many dice do you want to roll? ", min_value=1)

            rolls = [random.randint(1, sides) for _ in range(count)]

            if count == 1:
                print(f"You rolled a {rolls[0]}!")
            else:
                print(f"You rolled: {rolls}")
                print(f"Total: {sum(rolls)}")

            if not ask_yes_no("\nDo you want to roll again?"):
                break


# ---------------------- MAIN MENU ----------------------

class GameSuite:
    def __init__(self):
        # Menu number -> (name, project object)
        self.projects = {
            "1": ("Tic-Tac-Toe", TicTacToe()),
            "2": ("Rock-Paper-Scissors", RockPaperScissors()),
            "3": ("Number Guessing Game", NumberGuessingGame()),
            "4": ("Coin Flip", CoinFlip()),
            "5": ("Temperature Converter", TemperatureConverter()),
            "6": ("Simple Calculator", SimpleCalculator()),
            "7": ("Dice Roller", DiceRoller()),
        }
        self.quit_option = str(len(self.projects) + 1)

    def show_menu(self):
        clear_screen()
        print("Welcome to the All-In-One Game Suite!\n")
        for number, (name, _) in self.projects.items():
            print(f"{number}. {name}")
        print(f"{self.quit_option}. Quit")
        return input("\nEnter your choice: ").strip()

    def run(self):
        while True:
            choice = self.show_menu()

            if choice in self.projects:
                _, project = self.projects[choice]
                project.play()
            elif choice == self.quit_option:
                clear_screen()
                print("Thank you for playing. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
                pause()


if __name__ == "__main__":
    try:
        GameSuite().run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C (or Ctrl+D) quits the program without an ugly error message.
        print("\n\nGoodbye!")
