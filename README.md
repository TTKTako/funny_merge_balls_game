# Welcome to Funny Merge Balls
> **Genre**: Puzzle\
> **description**: Drop those colorful balls and watch them merge to be the bigger one, but beware of overfilling the ball!

<br>

## How to install?

**Require Library**:
- turtle
- pandas
- csv
- pygame
- random
- copy
Library install method.
```bash
pip install PythonTurtle pandas pygame
```

**Install Game**:
```bash
git clone https://github.com/TTKTako/funny_merge_balls_game.git
```

<br>

## Demo & Tutorial
- https://youtu.be/AZZqHOkub4E

<br>

## How to play?

**First Step**:
- run the file name: '<font color="#fab727">Run_Game.py</font>'.

**Second Step**:
- Enter your <font color="#fb683b">username</font> in terminal for <font color="#fe8e8e">saving</font> your high score data and click '<font color="#fab727">Start</font>'.

**Third Step**:
- press <font color="#fb683b">spacebar</font> on your keyboard to drop balls. Merge the same ball to get the score and bigger ball.

**Fourth Step**:
- Have fun with a game. :>

<br>

## Feature methods

**Save data**:
- use **csv** to read and write file.

**Display scoreboard**:
- use **Pandas** to get top 5 and display in order.

**Display game**:
- use **turtle** to generate UIs and gameplay.

**Playsound**:
- use **pygame** to access sound path and play it.

<br>

## UML
![UML plan](https://github.com/TTKTako/funny_merge_balls_game/blob/main/project_UML.png)

<br>

## Bugs
- **Lag**: This happened from the physics module because the script will repeatedly calculate so the ball will be dynamic to move to the left, right, or merge. [Test by spam dropping balls.]
- **Collision**: Sometimes balls will stack over and over. This happened from the hitbox that calculates from the turtle position and radius. Since the amount of time that I have is not enough to fix. [test by normally playing.]

<br>

## Coding detail & Prefer score
**Code**:
- First of all, I didn't use any code from the professor, so I recreated every system by myself, such as inelastic collision, generating application backgrounds, and more.
- How did I create physics? I made the physics of balls to be 2 main parts, First, the gravitational; I add acceleration to balls and check that if they touch with other balls or the border, then stop. Second, inelastic; I start checking if the balls touch something, then calculate the distance between the 2 center points of the balls. If the distance is negative, then go to the left; if the distance is positive, then go to the right; if the distance is 0, then randomly go to the left or right.

```math
 \bigtriangleup x = x_{collideball} - x_{checkball}
```

<br>

```math
 direction(x) \left\{\begin{matrix} x \pm 1    ;    \bigtriangleup x = 0
 \\ x - 1    ;    \bigtriangleup x > 0
 \\ x + 1    ;    \bigtriangleup x < 0
\end{matrix}\right.
```

- How did I loop the dropper without effect any other script: of course there is a function that we can call from turtle which is

```py
import turtle
turtle.Screen().ontimer(func(), 100)
```

**Prefer Score**:
- My preferred score is <font color="#fab727">**100**</font> because I need to rewrite and calculate all new physics systems and adapt a number of features from the base code to be more efficient and stable.

<br>
---


**Image Source**:
- https://dk.pinterest.com/
- https://www.flaticon.com/

**Sound effect Source**:
- https://mixkit.co/