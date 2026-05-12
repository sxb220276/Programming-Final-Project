# PFDA SNAKE

## Demo

Demo Video: <https://youtu.be/BH5L-Z6F0Js>

## GitHub Repository

GitHub Repo: <https://github.com/sxb220276/Programming-Final-Project>

## Description

This project was a recreation of snake from scratch.
Everything that was made was made by me with little asssitance.

### Feature: Movement

The player character is completely controlled by the w a s d keys.
When the player goes a direction, they cannot go the opposite direction.
For example, if the player goes left, they cannot go right until they change direction.

### Feature: Snake Body

The snake tracks each part of the body, every bit behind the head inherits the next bit's position.
If the player overlaps with any part of the snake's body, the game resets. 
The same goes for if the snake leaves the screen borders.

### Feature: Fruit

On initialization, a fruit bit is spawned randomly on the screen.
When the snake head overlaps with a fruit, a score value is increased and a new fruit spawns.
The snake body then grows by one.

### Feature: Screen Changes

When the fruit score gets high enough, the game screen starts changing.
Text displays in the middle of the screen and changes with enough score to create a moving narrative.
After enough fruit eaten, the narrative then ends abruptly with the program closing.
