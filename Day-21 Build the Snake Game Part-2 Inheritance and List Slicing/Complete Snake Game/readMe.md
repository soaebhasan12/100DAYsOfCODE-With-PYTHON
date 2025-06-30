# 🐍 Snake Game Project

Welcome to the **Snake Game Project**, a classic arcade game built using Python's `turtle` module. This project is part of the **100 Days of Python Bootcamp** and demonstrates the use of **Object-Oriented Programming (OOP)** concepts, event-driven programming, and graphical user interface design.

---

## 📽️ Project Overview

In this game:
- The player controls a snake that moves around the screen.
- The snake grows longer each time it eats food.
- The game ends if the snake collides with the wall or its own body.
- The player's score is displayed in real-time.

---

## 📂 Project Structure

The project consists of the following files:

1. **[`main.py`](main.py)**  
   The main game loop that initializes the screen, listens for user input, and handles game logic such as collisions and score updates.

2. **[`snake.py`](snake.py)**  
   Contains the `Snake` class, which manages the snake's movement, growth, and direction changes.

3. **[`food.py`](food.py)**  
   Contains the `Food` class, which generates food at random positions on the screen.

4. **[`scoreboard.py`](scoreboard.py)**  
   Contains the `Scoreboard` class, which displays the player's score and shows a "GAME OVER" message when the game ends.

---

## 🎮 How to Play

1. Use the **arrow keys** to control the snake's direction:
   - **Up Arrow**: Move up  
   - **Down Arrow**: Move down  
   - **Left Arrow**: Move left  
   - **Right Arrow**: Move right  

2. The goal is to eat the blue food that appears randomly on the screen. Each time the snake eats food:
   - The snake grows longer.
   - The score increases by 1.

3. The game ends if:
   - The snake collides with the wall.
   - The snake collides with its own body.

---

## 🛠️ How to Run

1. Ensure you have **Python 3.x** installed on your system.
2. Clone this repository or download the files.
3. Run the `main.py` file in your Python IDE or terminal:
   ```bash
   python main.py