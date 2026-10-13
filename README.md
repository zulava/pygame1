Pygame Tutorial in VS Code (for Game Dev)
This tutorial is for Advanced-level middle school students who already understand basic Python (variables, if/else, loops, functions) and are ready to build a game using Pygame.

1. Initial Setup

a. Install Python
Download Python from python.org/downloads
During installation, check "Add Python to PATH" (important!)
Verify it worked by opening a terminal/CMD and typing:
python --version

b. Install VS Code
Download from code.visualstudio.com
Install as usual

c. Install the Python Extension in VS Code
Open VS Code → click the Extensions icon (the 4-square icon in the left sidebar)
Search for "Python" (by Microsoft) → click Install
(Optional but recommended) Also install the "Pylance" extension for better autocomplete

d. Install the Pygame Library
Open the terminal in VS Code: menu Terminal → New Terminal
Type:
pip install pygame
Verify it worked:
python -m pygame.examples.aliens
If a simple alien shooter game shows up, the installation succeeded! 🎉

2. Project Folder Structure
Create a project folder, e.g. my-first-game/, then open that folder in VS Code (File → Open Folder).
my-first-game/
├── main.py          <- main game code
├── assets/
│   ├── images/       <- images/sprites
│   └── sounds/        <- sound effects & music
