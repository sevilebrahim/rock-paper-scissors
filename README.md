# Rock Paper Scissors 🎮

A small Python game based on the classic Rock, Paper, Scissors.

The idea is simple: the player chooses one of three options — rock, paper, or scissors — while the computer makes its choice randomly. Each round is compared, and a point is given to the winner.

The game currently runs for four rounds, and at the end, the scores are compared to determine the overall winner.

### How to Play

Start the program and enter:

```text
rock
paper
scissors
```

The computer will randomly choose one of the three options, and the result of the round will be displayed immediately.

For example:

```text
Choose rock, paper, or scissors: rock
Computer: scissors
You win this round!
----------------
```

After all four rounds, the final scores are shown and the game announces whether you won, lost, or ended in a draw.

### What I Practiced

This project helped me practice some of the basic but important parts of Python, including random values, user input, conditions, loops, variables, and keeping track of scores.

One of the main parts of the project is using `random.choice()` to let the computer make a different choice during each round.

### Run the Game

Make sure Python is installed, then run:

```bash
python rock_paper_scissors.py
```

No external libraries are required because the project only uses Python's built-in `random` module.

### Future Ideas

The game could be expanded later with more rounds, a best-of-three mode, input validation, or a replay option.

This is a simple project, but it was a useful way to practice Python fundamentals by turning them into something interactive and playable.
