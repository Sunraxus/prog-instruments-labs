import random
import pyfiglet
from rich.console import Console
from rich.text import Text

# Create a console object for rich text
console = Console()

class ImpossibleGame:
    def __init__(self):
        self.moves_left = 7  # Reduced moves for more difficulty
        self.puzzle_stage = 1

    def start_game(self):
        # ASCII banner for game title
        banner = pyfiglet.figlet_format("Impossible Game")
        console.print(f"[bold cyan]{banner}[/bold cyan]")
        
        console.print("Only [bold red]1%[/bold red] of players can win. You have [bold yellow]7 moves[/bold yellow] to complete the game.", style="bold magenta")
        console.print("[bold blue]Solve the puzzles, but beware: a single wrong move can end your journey.[/bold blue]")
        self.play_game()

    def play_game(self):
        while self.moves_left > 0:
            if self.puzzle_stage == 1:
                if self.puzzle_one():
                    self.puzzle_stage = 2
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 2:
                if self.puzzle_two():
                    self.puzzle_stage = 3
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 3:
                if self.puzzle_three():
                    self.puzzle_stage = 4
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 4:
                if self.puzzle_four():
                    self.win_game()
                    return
                else:
                    self.game_over()
                    return
        console.print("[bold red]Out of moves! Game over.[/bold red]")
    
    def puzzle_one(self):
        console.print("\n--- [bold yellow]Puzzle 1: The Number Sequence[/bold yellow] ---")
        console.print("[bold green]Find the number that completes this sequence: 2, 4, 8, 16, ?[/bold green]")
        try:
            answer = int(input("Your answer: "))
            if answer == 32:
                console.print("[bold green]Correct! Moving to the next puzzle.[/bold green]")
                self.moves_left -= 1
                return True
            else:
                console.print("[bold red]Incorrect! You lose a move.[/bold red]")
                self.moves_left -= 2
                return False
        except ValueError:
            console.print("[bold red]Invalid input. You lose a move.[/bold red]")
            self.moves_left -= 2
            return False

    def puzzle_two(self):
        console.print("\n--- [bold yellow]Puzzle 2: The Reverse Word[/bold yellow] ---")
        word = "python"
        console.print(f"[bold green]What is the reverse of '{word}'?[/bold green]")
        answer = input("Your answer: ")
        if answer.lower() == word[::-1]:
            console.print("[bold green]Correct! Moving to the next puzzle.[/bold green]")
            self.moves_left -= 1
            return True
        else:
            console.print("[bold red]Incorrect! You lose a move.[/bold red]")
            self.moves_left -= 2
            return False

    def puzzle_three(self):
        console.print("\n--- [bold yellow]Puzzle 3: Math Challenge[/bold yellow] ---")
        console.print("[bold green]Solve this math problem: What is the sum of all numbers from 1 to 10?[/bold green]")
        try:
            answer = int(input("Your answer: "))
            if answer == 55:  # 1+2+3...+10 = 55
                console.print("[bold green]Correct! Moving to the final puzzle.[/bold green]")
                self.moves_left -= 1
                return True
            else:
                console.print("[bold red]Incorrect! You lose a move.[/bold red]")
                self.moves_left -= 2
                return False
        except ValueError:
            console.print("[bold red]Invalid input. You lose a move.[/bold red]")
            self.moves_left -= 2
            return False

    def puzzle_four(self):
        console.print("\n--- [bold yellow]Puzzle 4: The Final Door[/bold yellow] ---")
        console.print("[bold green]You are faced with two doors: One leads to victory, the other to defeat.[/bold green]")
        console.print("[bold green]Choose wisely![/bold green]")
        choice = input("Choose door 1 or door 2: ")
        correct_door = random.choice(['1', '2'])  # Randomly decides the winning door
        if choice == correct_door:
            console.print("[bold green]You chose the right door![/bold green]")
            self.moves_left -= 1
            return True
        else:
            console.print("[bold red]Wrong door! You lose the game.[/bold red]")
            self.moves_left -= 2
            return False

    def game_over(self):
        console.print("\n[bold red]Game Over. Better luck next time![/bold red]")
    
    def win_game(self):
        console.print("\n[bold gold]Congratulations! You have won the Impossible Game![/bold gold]")
        console.print("[bold gold]You are part of the elite 1% who can solve these challenges.[/bold gold]")

def play_again():
    while True:
        play = input("\nWould you like to play again? (yes/no): ").lower()
        if play in ('yes', 'y'):
            return True
        elif play in ('no', 'n'):
            return False
        else:
            console.print("[bold red]Invalid input. Please answer 'yes' or 'no'.[/bold red]")

# Game loop to allow continuous play
while True:
    game = ImpossibleGame()
    game.start_game()
    
    if not play_again():
        console.print("[bold cyan]Thanks for playing! Goodbye.[/bold cyan]")
        break