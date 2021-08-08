import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

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

char_speed = 1

# 적 캐릭터 불러오기
enemy = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\pygame_frame\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

running = True
while running:
    dt = clock.tick(60)
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
    
    char_x_pos += ((to_x_L+to_x_R) * dt)
    char_y_pos += ((to_y_U+to_y_D) * dt) 

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > (screen_width-char_width):
        char_x_pos = (screen_width-char_width)
    
    if char_y_pos < 0:
        char_y_pos = 0
    elif char_y_pos > (screen_height-char_height):
        char_y_pos = (screen_height-char_height)

    # 캐릭터 rect 정보 업데이트
    char_rect = character.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    # 적 캐릭터 rect 정보 업데이트
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if char_rect.colliderect(enemy_rect): # char_rect 와 enemy_rect 가 충돌했는지 체크함.
        print("충돌했어요.")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (char_x_pos,  char_y_pos))

    # 적 캐릭터 설정
    screen.blit(enemy, (enemy_x_pos,  enemy_y_pos))

    pygame.display.update()

pygame.quit()