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

## 4. Making a Character That Can Move

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


# Try running it with the **Run** button (▶) in the top-right corner of VS Code, or press `F5`.


## 5. Adding an Image (Sprite)

# Load an image (put the image file in the assets/images/ folder)
player_image = pygame.image.load("assets/images/player.png")
player_image = pygame.transform.scale(player_image, (50, 50))  # resize

# Inside the loop, replace pygame.draw.rect with:
screen.blit(player_image, (player_x, player_y))


## 6. Collision Detection

# The easiest way is using `pygame.Rect`:


player_box = pygame.Rect(player_x, player_y, 50, 50)
enemy_box = pygame.Rect(enemy_x, enemy_y, 50, 50)

if player_box.colliderect(enemy_box):
    print("Collision!")



## 7. Score and Text

font = pygame.font.SysFont(None, 48)
score = 0

# Inside the loop, after screen.fill():
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))


## 8. Sound and Music


pygame.mixer.init()

# Background music (loops forever)
pygame.mixer.music.load("assets/sounds/music.mp3")
pygame.mixer.music.play(-1)  # -1 = loop forever

# One-time sound effect
jump_sound = pygame.mixer.Sound("assets/sounds/jump.wav")
jump_sound.play()


## 9. Simple Game Over Screen

def show_game_over(screen):
    big_font = pygame.font.SysFont(None, 72)
    text = big_font.render("GAME OVER", True, (255, 50, 50))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)