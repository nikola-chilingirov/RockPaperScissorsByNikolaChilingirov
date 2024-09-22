# The "Rock - Paper - Scissors" game, by Nikola_Chilingirov
 This is a simple console game "Rock Paper Scissors"
 
**Rock - Paper - Scissors** is played with three possible signals that represent a rock, paper, and scissors. Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players chose the same signal, it is considered a draw, and play resumes until there is a clear winner.
The player enters one of the following options:
- **'r' for rock**
- **'p' for paper**
- **'s' for scissors**

The computer choose a random option, then reveals the winner.

In code, there are nasted loops, with inner loop the program solve eventual problem with incorrect input data. Outer loop give an option to play again.

For colored output it is used **Colorama**. It is cross-platform colored terminal text. Cross-platform printing of colored text is done by using Colorama’s constant shorthand for ANSI escape sequences.
![image](https://github.com/user-attachments/assets/83b0be59-1591-4380-a5da-f1a31e777b6a)

With if-else statement are solve the issues about the choice of the player, the random choice of computer and which of the choices is winning. For the random choice of the computer it is used **"randint()"** method from build-in library **"random"**. **"randint"** accepts two parameters, both inclusive and returns a random number in this range.

[Source Code](https://github.com/nikola-chilingirov/RockPaperScissorsByNikolaChilingirov/blob/main/rock_paper_scissors.py) 

Screeshot

![image](https://github.com/user-attachments/assets/eaa66823-eb2f-46ec-8546-33f2631a46dc)

[Live Demo](https://replit.com/@nchilingirovz/RockPaperScissors#main.py)

