# *Find-Winner-on-a-Tic-Tac-Toe-Game*
##  *The Problem  ⛓*      
  Tic-tac-toe is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

  -  Players take turns placing characters into empty squares `' '`.
  
  -  The first player `A` always places `'X'` characters, while the second player `B`  always places `'O'`  characters.
  
  -  `'X'` and `'O'` characters are always placed into empty squares, never on filled ones.
  
  -  The game ends when there are three of the same (non-empty) character filling any `row`, `column`, or `diagonal`.
   
  -  The game also ends if all squares are non-empty.
    
  -  No more moves can be played if the game is over.

  -  Given a 2D integer array moves where `moves[i] = [rowi, coli]`  indicates that the ith move will be played on `grid[rowi][coli]`. return the winner of the game if it exists `(A or B)`. In case the game ends   in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

- You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

#  *Approach ⛓️‍💥*


### *After all this Rules what is the `Tic-Tac-Toe` Game Actually you know it* 


<img width="891" height="353" alt="image" src="https://github.com/user-attachments/assets/7b35bef4-1ac2-4b03-b6b3-aab8af20749f" />

 ## *To solve the problem we should know all the wining Cases*  

<img width="784" height="711" alt="image" src="https://github.com/user-attachments/assets/cca584e1-b04c-48d2-af3d-e6b967ad6857" />   

####  *The Winning Posisions*   
```py
winning_positions = [
            {tuple([0, 0]), tuple([0, 1]), tuple([0, 2])},
            {tuple([1, 0]), tuple([1, 1]), tuple([1, 2])},
            {tuple([2, 0]), tuple([2, 1]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 0]), tuple([2, 0])},
            {tuple([0, 1]), tuple([1, 1]), tuple([2, 1])},
            {tuple([0, 2]), tuple([1, 2]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 1]), tuple([2, 2])},
            {tuple([0, 2]), tuple([1, 1]), tuple([2, 0])}
        ]    
```
 
### *Hint 1*   
  - All  The Positions of the Player 2 is `Odd` Number (impaire 1,3,5,7)
  - All  the Positions of the player 1 is `Even` Number (paire 0,2,4,6,8)
   


##  *Example 🧪*   

   #### `moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]`

### *Player 1️⃣ User of `X`*   
    {(0, 0), (0, 1), (1, 2), (2, 0), (2, 2)}   
### *Player 2️⃣ User of `O`*   
    {(0, 2), (1, 0), (1, 1), (2, 1)}   

##  *I use Thia Part of Code :*   

```py
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]] 
winning_positions = [
            {tuple([0, 0]), tuple([0, 1]), tuple([0, 2])},
            {tuple([1, 0]), tuple([1, 1]), tuple([1, 2])},
            {tuple([2, 0]), tuple([2, 1]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 0]), tuple([2, 0])},
            {tuple([0, 1]), tuple([1, 1]), tuple([2, 1])},
            {tuple([0, 2]), tuple([1, 2]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 1]), tuple([2, 2])},
            {tuple([0, 2]), tuple([1, 1]), tuple([2, 0])}
        ]      
player1_moves =  set()  
player2_moves =  set()   
for i , move in enumerate (moves) :    
        if i % 2 == 0 :   
                player1_moves.add(tuple(move))  
        else :   
                player2_moves.add(tuple(move))    

print(player1_moves)
print(player2_moves) 
``` 

##  *After we Know all the Positions of any  Player we need to check whos win 🤔*   

- We gonna use `issubset()`  we virifie with if we have a `left` expresion  in the right `Position`
  
    - `{1, 2}.issubset({1, 2, 3})`  -> `True`
    - `{1, 4}.issubset({1, 2, 3})`  -> `False`
 

###  *So the Last Thing Is Easy*   

#### *If we find a `Winning_position` in `Player1_moves` we return  `"A"`*
#### *If we find a `Winning_position` in `Player2_moves` we return  `"B"`*      


##  *Examples 🧪*   


<img width="1096" height="698" alt="image" src="https://github.com/user-attachments/assets/bd6ecbb2-b6cf-466f-a6ff-f09d0e05a418" />

  
##  *The Translation to Code ⚔️*       


```py
for win in  winning_positions :   
  if win.issubset(player1_moves) :   
      return "A"   
  if win.issubset(player2_moves) :   
       return  "B"  
```


###  *we See the Cases when `A` Win or `B` win*   

  -  The `Draw`  case
  -  the `Pending` case

#### *Draw 🤝*   
  - when  we Virifie The Player1_moves and Player2_moves and no one Win
  - To be specific  when the `moves.length == 9 ` and `no winner` .

###  *Pending ➿*  
  - When we have `moves.length < 9 `  and `no winner`


##  *The Translation to Code ⚔️*       


```py
if len(moves) == 9 :   
  return "Draw"   
else :   
  "Panding"
```

## *Time and Space Complexity ⏳&☄️*   
  ### *Time complexity ⏳*  : $$O(1)$$   
  ### *Space complexity ☄️*  : $$O(1)$$  


## *The Translation of all the part  to the final  Code ⚔️*   



```py
def TicTacGame(moves):
    winning_positions = [
            {tuple([0, 0]), tuple([0, 1]), tuple([0, 2])},
            {tuple([1, 0]), tuple([1, 1]), tuple([1, 2])},
            {tuple([2, 0]), tuple([2, 1]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 0]), tuple([2, 0])},
            {tuple([0, 1]), tuple([1, 1]), tuple([2, 1])},
            {tuple([0, 2]), tuple([1, 2]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 1]), tuple([2, 2])},
            {tuple([0, 2]), tuple([1, 1]), tuple([2, 0])}
        ]      
    player1_moves =  set()  
    player2_moves =  set()   

    for i , move in enumerate (moves) :    
        if i % 2 == 0 :   
                player1_moves.add(tuple(move))  
        else :   
                player2_moves.add(tuple(move))    
    for win in  winning_positions :   
           if win.issubset(player1_moves) :   
                  return "A"   
           if win.issubset(player2_moves) :   
                  return  "B"   
    if len(moves) == 9 :   
           return "Draw"   
    else :   
           "Panding"  
```


### *So we done have a good day 💭*   




<img width="500" height="350" alt="Hope you enjoyed this part  See what's next!" src="https://github.com/user-attachments/assets/3537732f-f282-4492-9765-32900b6aa085" />

