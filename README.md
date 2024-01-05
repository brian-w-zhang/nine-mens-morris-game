Nine Men’s Morris

_Part A Plan_

![](https://lh7-us.googleusercontent.com/CXQENniOgDxiIGEwVoO6oX6_zNWBpscfNqP5M4rIA81mai6hUgUf1OYNrMca7FOHHmPL9PHn90VtQIV_7qP8GzSZ9ogZ2sb8AO0XVBI151UuBuBOUt6Yl4kuj1ZjtB4uce9i9Rp-Ld8HRnz2qsK6anM)

**Brian Zhang**

01.12.2022

ICS3UP


# PROGRAM DESCRIPTION:![](https://lh7-us.googleusercontent.com/Zvjie1GwDlKbWKXAoJxoSs_LaVMnx8smPuzBKCdzFgWCyLVudTfZ864Rwam50ePynwaef2gjHb4nxHaPNleAOGR27V-nbeI32v34TxE_K5vQ2QsyMbN_-vmIFvS3TrYT5x9-Otr4OgG-DL7VtV2kmUs)

Equipment:

Nine Men’s Morris is played between two players on a board as seen in the image on the right. Each of the 24 points represent a place where a piece can be played. 

There are 9 white pieces and 9 white black pieces that accompany the board. These pieces (or “men”) are flat cylinders, which closely resemble checkers pieces.

Objective:

The objective of the game is to form consecutive lines of 3, kind of like Tic-Tac-Toe. These vertical or horizontal lines of 3 in a row are called “mills”. Every time a player forms a mill, an opposing piece is removed. A player wins when they reduce the number of the opponent’s pieces to two, so that they can no longer form mills. 

Play:

Players determine who gets the white pieces and goes first. In the first phase of the game, players take turns placing one of their nine pieces on any vacant point until all pieces have been played.

In the second phase, players alternate moving any one of their pieces to an unoccupied adjacent point. Pieces cannot jump over each other until a player has 3 pieces left. 

If a player forms a mill during any phase, they get to remove any one of their opponent’s pieces that is not currently a part of a mill, unless no other pieces are available. Pieces are only captured when a mill has just been formed. Moving a piece back and forth to continuously break and reform a mill is a common strategy. A captured piece cannot be replayed, and remains out of the game.

Once a player only has 3 pieces remaining, that player’s pieces gain the ability to “jump”. This means that their pieces are not limited to traveling to vacant adjacent points, and can “jump” to any unoccupied point on the board.

In addition to winning when the opponent is reduced to 2 pieces, a player can also win if all of the opponent’s pieces are trapped and unable to move.


# ISPO PLAN

|                                                                                                                                |                                                                                                                                                                                                                                  |                                                                                                                                                                             |                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ## INPUT                                                                                                                       | ## STORAGE                                                                                                                                                                                                                       | ## PROCESS                                                                                                                                                                  | ## OUTPUT                                                                                                               |
| Locations of all pieces on the board                                                                                           | The locations of all pieces on the board is stored as a list (filled with placeholders at the start of the game).Each point on the board is labeled with a number from 0-23, which correspond with the values in the above list. | The locations of every point on the board minus the locations of points with a piece on them give the location of vacant points on the board.                               | The locations of vacant points on the board (same as the locations of points a player can place their piece in phase 1) |
| Number times pieces have been placed on the board for the first time                                                           | # of times pieces have been placed for the first time is a variable that acts as a counter. The variable is stored as an int.                                                                                                    | If all 18 pieces have been placed on the board for the first time, phase 1 has ended.Otherwise, phase 1 is still going.                                                     | Has phase 1 ended?                                                                                                      |
| Piece’s current positionTotal pieces that the  player controlling the piece has in playLocations of vacant points on the board | Piece’s position is an integer from 0-23. Total pieces a player has is stored as an int.Locations of vacant points is stored as a list.                                                                                          | If the player only has 3 pieces left, the piece may move to any vacant point.Otherwise, the piece may only move to vacant points that are adjacent to its current position. | Points that a piece is able to move to.                                                                                 |


# ISPO PLAN CONTINUED

|                                                                                                                                                                      |                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                            |                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| ## INPUT                                                                                                                                                             | ## STORAGE                                                                                                                                                                                                                                                     | ## PROCESS                                                                                                                                                                                                                                                 | ## OUTPUT                                                   |
| Positions of white pieces in playPositions of black pieces in playLocation that a piece just occupied, colour of that pieceLocations of pieces in all possible mills | Positions of white pieces is stored as a list.Positions of black pieces is stored as a list.Location of the point that was just occupied is stored as an int.Piece colour is stored as a string.Locations of pieces in all possible mills is stored as a list. | Find the location of pieces in possible mills that involve the location that a piece just occupied.If there are pieces of the same colour in those possible mill positions on the board, a mill has been formed.Otherwise, a mill has not been formed yet. | Has a mill (3 in a row) been formed?                        |
| Location of opposing piece that player wishes to removePositions of pieces opponent has in playLocations of pieces in all possible mills                             | Location of piece to be removed stored as an int.Positions of opponent’s pieces is stored as a list.Locations of pieces in all possible mills is stored as a list.                                                                                             | If all of the opponent’s pieces are a part of mills, the player’s choice is legal.Otherwise, see if the piece to be removed is a part of a mill. If so, the player’s choice is illegal, and if not, the choice is legal.                                   | Can the opposing piece a player wants to remove be removed? |
| Number white pieces in playNumber of black pieces in playPositions of white pieces in playPositions of black pieces in play                                          | Number of white/black pieces in play: different variables, both stored as intsPositions of white/black pieces in play: different variables, both stored as lists                                                                                               | See if any player has only 2 pieces in play.See if any player is completely unable to move.If either are true, someone has won. Otherwise, no one has won yet.                                                                                             | Has a player won?                                           |


# FUNCTION OUTLINE

Pseudocode and list of functions is attached in a separate file.


# USE OF PROGRAMMING CONCEPTS

Variables (global, local, constant)

- Constants

  - Constants with integer values are used to determine the length of various horizontal lines on the board

  - Constants with list values are used to determine positions of points on the board that are adjacent to position index, positions of pieces in possible vertical mills, and positions of pieces in possible horizontal mills

- Global Variables

  - The above constants are all global

  - There are no other global variables

- Local Variables

  - Local variables are present in almost all of the functions

  - Every function except for phase\_one() and phase\_two() have one or more parameters, which behave like local variables

  - Numerous local variables are initialized and manipulated within functions, as they store data that is needed for the functions to perform their purpose

Math Operators (including logical) and/or Math Module (eg. random)

- The Math Module is not used

- Math Operators (the following are used: +, \*)

  - Addition (+) is used to increase the values of counter variables, and to concatenate strings together in the function that prints the board

  - Multiplication (\*) is used for string multiplication in the function that prints the board, as characters like '━', and ' ' printed multiple times by being multiplied by integer values

- Logical operators:

  - The and, or, & not logical operators are used for the combination of the many conditional statements that exist in various functions

  - For example, if a vertical **or** horizontal mill has been formed by a player, then they get to remove an opposing piece 

* Comparison operators (==, !=, >, <, etc.) are used to compare two values

  - For example, the < operator is used to check if the number of white or black pieces are less than 3, which means that a player has lost

Functions and Built-in Methods

- Built-in Methods

  - print() is used to print instructions for the players, to print game information, to print the game board and to print the pieces on the board

  - range() is used to control how many times a for loop repeats

- Functions

  - The program is largely composed of functions

  - Different functions are used to carry out different tasks

  - Examples of tasks include printing the board, placing/moving/removing/counting pieces, finding possible moves, checking if a player has won, and more

Selection Constructs (if, elif, else)

- If, else, and elif

- If statements execute code when a certain condition is satisfied

  - For example, phase 2 begins **if** 9 black pieces have been placed

  - A player loses **if** they have less than 3 pieces in phase 2

  - A move is possible **if** the new position is vacant, and adjacent to the moving piece (**if** the player has 3 pieces, their pieces can jump to any vacant point)

- Elif statements allow for multiple statements to be checked

  - For example, if white has less than 3 pieces or is trapped, black wins, **else if** black has less than 3 pieces or is trapped, white wins

- Else statements execute if the if condition is not met

  - For example, **if** a player has no possible moves, they are trapped. **Else**, they are not trapped

Repetition Constructs (while, for)

- While loops run while a condition is met

  - For example, **while** no player has won, keep looping phase 2

  - **While** 9 black pieces have not been placed, loop phase 1

  - While statements control the phases of the game, by ending certain phases when a condition is no longer met

- Code in for loops repeatedly run a certain amount of times

- For each loops are used many times in the program to check if a condition is met for each item in the list spots

  - For example, **for each** item in spots, if that item equals the piece you’re counting for, increase a counter by 1

Data Structures (Strings, Lists, and/or Dictionaries, and their methods)

- Strings

  - Other than for printing purposes, strings are used to represent pieces (white or black) and placeholders (no piece) on the points of the board

  - The parameter player\_piece is used for the many functions that need to the state of a point on the board (whether it is occupied by a white or black piece, or a placeholder)

  - The values of pieces and placeholders are the following:

    - White piece: ‘▓▓▓’        On IDLE dark mode:![](https://lh7-us.googleusercontent.com/9h6N0XNQnhxwt6cxz2IaqT3PzYWJplhz77sw_E9aPcsMhQ4sLOBtC6cNW8VBBTKYzDpRNwjHaZcD4qDmUpBSyOtgus_YxeK7Hr7Gdredr7iV_3iyKzqK0KPOa38KfEFMfifX0TowdtQMjNQ4rjmF4Tw)

    - Black piece: ‘░░░’          On IDLE dark mode: ![](https://lh7-us.googleusercontent.com/WY6ntiKnzTr-nVn0uo8v8vMJFKZZ0PZ3X8T40UsUIhhMz6GJekZHWbQUiw9ObwAoFojCpLKEuf8qRdH_L6pvScvjtHtxrQMvNBqMhGBEkHltEenKWZd4ejLIQyJ3b-fuP-hYBKzbIXhscYrWGFxLJCM)

    - Placeholder: ‘ ● ’

  - The colours for white and black pieces appear to be inverted on this document, because the program is tailored for Idle dark mode

- Dictionaries

  - Dictionaries are not used in this program

- Lists

  - The locations of pieces on the board are kept track of using the list spots, where each index represents a position on the board (0-23)

    - Each item in piece spots has a value of ‘▓▓▓’, ‘░░░’, or  ‘ ● ’

    - The index of an item in spots represents the position of a piece, and the value of the item represents the piece or placeholder that occupies the point

    - This variable is used as a parameter in most of the functions, because knowing what pieces occupy which spots is essential for the game to be played

    - At first, the placeholder value is appended to spots 24 times

    - When pieces are placed/moved/removed, the values of certain items are adjusted to accurately depict what is happening on the board

  -  Lists are also used to represent locations of possible moves for a specific piece are needed, and to represent the positions of 3 pieces in a potential vertical or horizontal mill that a specific piece is involved in
