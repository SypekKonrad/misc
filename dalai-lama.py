import sys, pygame

pygame.init()

# set up of pygame
size = width, height = 800, 600

# speed of dalai-lama
speed = [15, 15]

# flying object(dalai_lama)
dalai_lama = pygame.image.load("dalai_lama.png")
dalai_lamarect = dalai_lama.get_rect()

# name bar
pygame.display.set_caption("dalai-lama")

#background
background = pygame.display.set_mode((800,600))

#color of background
color = (255,255,255)

#score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x,y): # shows on screen score
    score = score_font.render('punkty: ' + str(score_value), True, (216,160,84))
    background.blit(score, (x,y))


# timer
clock = pygame.time.Clock()
counter, countdown_timer_text = 20, '20'.rjust(15)
counter2 = counter
countdown_font = pygame.font.SysFont('WideLatin', 16)
def setup_countdown_timer():
    pygame.time.set_timer(pygame.USEREVENT, 1000)
setup_countdown_timer()

# mouse input
left, middle, right = pygame.mouse.get_pressed()

def render_countdown_timer():
    remaining_seconds = counter2 - int((pygame.time.get_ticks() / 1000))
    remaining_seconds_text = str(remaining_seconds).rjust(15)
    background.blit(countdown_font.render(remaining_seconds_text, True, (216, 160, 84)), (0, 40))
    if remaining_seconds <= 0:
        raise Exception(str('test'))
    
render_countdown_timer()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
           
                counter -= 1
                countdown_timer_text = str(counter).rjust(15)

        if event.type == pygame.MOUSEBUTTONDOWN and dalai_lamarect.collidepoint(event.pos) and event.button == 1:
            val = 1
            score_value += 1
            pygame.time.set_timer(my_event, 125, 1)


        # exit
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
            running = False

    # countdown timer goes to 0 then the app is closed
    dalai_lamarect = dalai_lamarect.move(speed)

    # dalai-lama reaches horizontal
    if dalai_lamarect.left < 0 or dalai_lamarect.right > width:

        speed[0] = -speed[1]

    # dalai-lama reaches vertical
    if dalai_lamarect.top < 0 or dalai_lamarect.bottom > height:

        speed[1] = -speed[1]

    show_score(textX, textY)
    pygame.display.update()
    background.fill(color)
    pygame.display.flip()
    clock.tick(60)



