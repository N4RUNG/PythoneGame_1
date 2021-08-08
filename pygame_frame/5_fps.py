import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\pygame_frame\\back.png")

character = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\pygame_frame\\chac.png")
char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width/2) - (char_width/2)
char_y_pos = screen_height - char_height

to_x_L = 0
to_x_R = 0
to_y_U = 0
to_y_D = 0

# 이동 속도
char_speed = 1

running = True
while running:
    # 초당 프레임 설정
    dt = clock.tick(60) # 60프레임
    print(f" fps : {str(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y_U -= char_speed
            if event.key == pygame.K_DOWN:
                to_y_D += char_speed
            if event.key == pygame.K_LEFT:
                to_x_L -= char_speed
            if event.key == pygame.K_RIGHT:
                to_x_R += char_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y_U = 0
            if event.key == pygame.K_DOWN:
                to_y_D = 0
            if event.key == pygame.K_LEFT:
                to_x_L = 0
            if event.key == pygame.K_RIGHT:
                to_x_R = 0
    
    char_x_pos += ((to_x_L+to_x_R) * dt) # 프레임에 따라 이동 속도가 차이가 없게 해줌.
    char_y_pos += ((to_y_U+to_y_D) * dt) 

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > (screen_width-char_width):
        char_x_pos = (screen_width-char_width)
    
    if char_y_pos < 0:
        char_y_pos = 0
    elif char_y_pos > (screen_height-char_height):
        char_y_pos = (screen_height-char_height)

    screen.blit(background, (0, 0))
    screen.blit(character, (char_x_pos,  char_y_pos))

    pygame.display.update()

pygame.quit()