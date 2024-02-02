import pygame
import time
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000,800
PLAYER_WIDTH, PLAYER_HEIGHT = 90, 100

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Polly Dodge")


BG = pygame.transform.scale(pygame.image.load("pic.jpeg"), (WIDTH,HEIGHT))
PLAYER_ICON = pygame.transform.scale(pygame.image.load("icon.jpeg"), 
                                     (PLAYER_WIDTH, PLAYER_HEIGHT))                       # add image of a player
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player,elapsed_time,stars):
    
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1 , "white")
    WIN.blit(time_text, (10,10))

    WIN.blit(PLAYER_ICON, (player.x, player.y))                                         # changed the black block to PLAYER_ICON image

    for star in stars:
        pygame.draw.rect(WIN, "blue", star)


    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()
    player = PLAYER_ICON.get_rect(topleft=(200, HEIGHT - PLAYER_HEIGHT))
    start_time = time.time()
    elapsed_time = 0
    start_add_increment = 2000
    start_count = 0
    stars = []
    hit = False

    while run:

        start_count += clock.tick(60) 
        elapsed_time = time.time() - start_time

        if start_count > start_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, - STAR_HEIGHT, 
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            start_add_increment = max(200, start_add_increment - 50)
            start_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH :
            player.x += PLAYER_VEL   

        for star in stars[:]:
            star.y += PLAYER_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break 

        if hit:
            lost_text = FONT.render("You Lost!", 1, "Black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 
                                 - lost_text.get_height() /2))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        draw(player, elapsed_time,stars)

    pygame.quit()

if __name__ == "__main__":
    main()



