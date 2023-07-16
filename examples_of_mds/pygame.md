---
title: Pygame Tutorial: Building a Space Invaders Game
date: 2023-07-17
tags: Game, Python, dev
summary: Pygame is a popular Python library for game development that provides an easy-to-use interface to create 2D games. 
slug: phaser3-intro
subtitle: In this tutorial, we will explore the basics of Pygame and build a classic Space Invaders game. Get ready for some alien-blasting fun!
---

# Pygame Tutorial: Building a Space Invaders Game

## Introduction

Welcome to this Pygame tutorial! Pygame is a popular Python library for game development that provides an easy-to-use interface to create 2D games. In this tutorial, we will explore the basics of Pygame and build a classic Space Invaders game. Get ready for some alien-blasting fun!

### Step 1: Setting up Pygame
To get started, make sure you have Pygame installed. You can install it using pip with the following command:

```
pip install pygame
```

### Step 2: Initializing the Game Window
Let's begin by creating the game window. Open your favorite Python editor and import the Pygame library. Then, initialize Pygame and create a game window with a specified width and height.

```python
import pygame

# Initialize Pygame
pygame.init()

# Create the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")
```

### Step 3: Adding the Player
Now, let's add the player character to the game. We'll create a spaceship image and load it onto the screen.

```python
# Load the spaceship image
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480

def player():
    # Draw the player onto the screen
    window.blit(player_img, (player_x, player_y))
```

### Step 4: Handling User Input
To allow the player to move the spaceship, we need to handle user input. We'll listen for keyboard events and update the player's position accordingly.

```python
# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Redraw the window
    window.fill((0, 0, 0))
    player()
    pygame.display.update()

# Quit Pygame
pygame.quit()
```

### Step 5: Adding Enemies
No Space Invaders game is complete without enemies! Let's create a group of alien enemies and display them on the screen.

```python
# Load the enemy image
enemy_img = pygame.image.load("alien.png")
enemy_x = 100
enemy_y = 50

def enemy():
    # Draw the enemy onto the screen
    window.blit(enemy_img, (enemy_x, enemy_y))

# Game loop
running = True
while running:
    # ...

    # Redraw the window
    window.fill((0, 0, 0))
    player()
    enemy()
    pygame.display.update()

# ...
```

### Step 6: Collision Detection
To make the game exciting, let's add collision detection. If the player's spaceship collides with an enemy, we'll display a "Game Over" message.

```python
# Game loop
running = True
game_over = False
while running:
    # ...

    # Check for collisions
    if player_x == enemy_x and player_y == enemy_y:
        game_over = True

    if game_over:
        # Display "Game Over" message
        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, (255, 255, 255))
        window.blit(text, (width // 2 - 150, height // 2))

    # ...

# ...
```

## Conclusion
Congratulations! You've successfully built a simple Space Invaders game using Pygame. You've learned the basics of creating a game window, handling user input, displaying characters, adding enemies, and implementing collision detection. Feel free to enhance your game with additional features such as scoring, power-ups, and sound effects.
