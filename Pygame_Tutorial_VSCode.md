# Pygame Tutorial in VS Code (for Game Dev Extracurricular)

This tutorial is for **Advanced-level** middle school students who already understand basic Python (variables, if/else, loops, functions) and are ready to build a game using **Pygame**.

---

## 1. Initial Setup

### a. Install Python
1. Download Python from [python.org/downloads](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"** (important!)
3. Verify it worked by opening a terminal/CMD and typing:
   ```bash
   python --version
   ```

### b. Install VS Code
1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install as usual

### c. Install the Python Extension in VS Code
1. Open VS Code → click the **Extensions** icon (the 4-square icon in the left sidebar)
2. Search for **"Python"** (by Microsoft) → click **Install**
3. (Optional but recommended) Also install the **"Pylance"** extension for better autocomplete

### d. Install the Pygame Library
1. Open the terminal in VS Code: menu **Terminal → New Terminal**
2. Type:
   ```bash
   pip install pygame
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
│   ├── images/       <- images/sprites
│   └── sounds/        <- sound effects & music
```

> Tip: Set up the `assets` folder from the start to stay organized. Grab free images/sounds from [Kenney.nl](https://kenney.nl/assets) or [OpenGameArt.org](https://opengameart.org/).

---

## 3. Basic Anatomy of a Pygame Program

Every Pygame game follows the same structure:

```python
import pygame

# 1. Initialize
pygame.init()

# 2. Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

# 3. Game loop (the heart of every game)
running = True
clock = pygame.time.Clock()

while running:
    # 3a. Check events (player input, close button, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3b. Update game logic (position, score, etc.)

    # 3c. Redraw the screen
    screen.fill((30, 30, 60))  # background color (RGB)
    pygame.display.flip()      # show the drawn result

    clock.tick(60)  # cap at 60 frames per second

pygame.quit()
```

**Key concepts explained:**
- `pygame.init()` → turns on all pygame modules
- **Game loop** → code that keeps running while the game is active (check input → update → draw → repeat)
- `clock.tick(60)` → keeps the game running at a stable 60 FPS (not too fast/slow)
- `pygame.display.flip()` → "displays" everything that has been drawn onto the screen

---

## 4. Making a Character That Can Move

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Character Movement")
clock = pygame.time.Clock()

# Player's starting position (a simple square)
player_x, player_y = 400, 300
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are currently pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill((20, 20, 40))
    pygame.draw.rect(screen, (0, 200, 100), (player_x, player_y, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Try running it with the **Run** button (▶) in the top-right corner of VS Code, or press `F5`.

---

## 5. Adding an Image (Sprite)

```python
# Load an image (put the image file in the assets/images/ folder)
player_image = pygame.image.load("assets/images/player.png")
player_image = pygame.transform.scale(player_image, (50, 50))  # resize

# Inside the loop, replace pygame.draw.rect with:
screen.blit(player_image, (player_x, player_y))
```

---

## 6. Collision Detection

The easiest way is using `pygame.Rect`:

```python
player_box = pygame.Rect(player_x, player_y, 50, 50)
enemy_box = pygame.Rect(enemy_x, enemy_y, 50, 50)

if player_box.colliderect(enemy_box):
    print("Collision!")
```

---

## 7. Score and Text

```python
font = pygame.font.SysFont(None, 48)
score = 0

# Inside the loop, after screen.fill():
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))
```

---

## 8. Sound and Music

```python
pygame.mixer.init()

# Background music (loops forever)
pygame.mixer.music.load("assets/sounds/music.mp3")
pygame.mixer.music.play(-1)  # -1 = loop forever

# One-time sound effect
jump_sound = pygame.mixer.Sound("assets/sounds/jump.wav")
jump_sound.play()
```

---

## 9. Simple Game Over Screen

```python
def show_game_over(screen):
    big_font = pygame.font.SysFont(None, 72)
    text = big_font.render("GAME OVER", True, (255, 50, 50))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
```

---

## 10. Recommended Learning Path (for the Club)

| Week | Focus |
|---|---|
| 1 | Installation + empty game window |
| 2 | Character movement with keyboard |
| 3 | Add sprite/image + background |
| 4 | Collision detection + simple enemy |
| 5 | Score + on-screen text |
| 6 | Sound & music |
| 7 | Game over + restart |
| 8 | Polish (main menu, levels, etc.) |

---

## 11. Common Troubleshooting

| Problem | Cause & Solution |
|---|---|
| `ModuleNotFoundError: No module named 'pygame'` | Pygame isn't installed on the interpreter VS Code is using. Check the interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter" |
| The game window closes immediately | Run it from the terminal (`python main.py`) instead of double-clicking the file, so you can see the error message |
| Image doesn't show up | Check the file path relative to `main.py`'s location, and make sure the file name & extension match exactly (case-sensitive on some systems) |
| Game is laggy/stuttering | Make sure `clock.tick(60)` is inside the loop |

---

## 12. Additional Learning Resources
- Official docs: [pygame.org/docs](https://www.pygame.org/docs/)
- Free assets: [Kenney.nl](https://kenney.nl/assets), [OpenGameArt.org](https://opengameart.org/)
- Built-in pygame example game: `python -m pygame.examples.aliens`

---

*This tutorial is designed to support the Middle School Game Development Extracurricular module — it can serve as a student handout during the "Production" sessions (meetings 8–13).*
