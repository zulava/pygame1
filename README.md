# 🎮 Pygame Tutorial in VS Code (for Game Dev)

This tutorial is for **advanced-level middle school students** who already understand basic Python (variables, if/else, loops, functions) and are ready to build a game using **Pygame**.

---

## Table of Contents

1. [Initial Setup](#1-initial-setup)
   - [a. Install Python](#a-install-python)
   - [b. Install VS Code](#b-install-vs-code)
   - [c. Install the Python Extension in VS Code](#c-install-the-python-extension-in-vs-code)
   - [d. Install the Pygame Library](#d-install-the-pygame-library)
2. [Project Folder Structure](#2-project-folder-structure)

---

## 1. Initial Setup

### a. Install Python

1. Download Python from [python.org/downloads](https://www.python.org/downloads/).
2. During installation, check **"Add Python to PATH"** (important!).
3. Verify it worked by opening a terminal/CMD and typing:

   ```bash
   python --version
   ```

### b. Install VS Code

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Install as usual.

### c. Install the Python Extension in VS Code

1. Open VS Code and click the **Extensions** icon (the 4-square icon in the left sidebar).
2. Search for **"Python"** (by Microsoft) and click **Install**.
3. *(Optional but recommended)* Also install the **"Pylance"** extension for better autocomplete.

### d. Install the Pygame Library

1. Open the terminal in VS Code: menu **Terminal → New Terminal**.
2. Type:

   ```bash
   pip install pygame-ce
   ```

3. Verify it worked:

   ```bash
   python -m pygame.examples.aliens
   ```

If a simple alien shooter game shows up, the installation succeeded! 🎉

---

## 2. Project Folder Structure

Create a project folder, e.g. `my-first-game/`, then open that folder in VS Code (**File → Open Folder**).

```
my-first-game/
├── main.py          <- main game code
├── assets/
│   ├── images/      <- images/sprites
│   └── sounds/      <- sound effects & music
```
