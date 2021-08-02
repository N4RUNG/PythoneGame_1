import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\back.png")

character = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\chac.png")
char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width/2) - (char_width/2)
char_y_pos = screen_height - char_height

to_x = 0
to_y = 0

char_speed = 1

enemy = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

# 폰트(글꼴) 설정
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 타이머 시간 설정
total_time = 10

# 타이머 시간 시작 정보 저장
start_ticks = pygame.time.get_ticks() # 시간 tick 을 받아옴.

running = True
while running:
    dt = clock.tick(60)
    print(f" fps : {str(clock.get_fps())}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= char_speed
            if event.key == pygame.K_DOWN:
                to_y += char_speed
            if event.key == pygame.K_LEFT:
                to_x -= char_speed
            if event.key == pygame.K_RIGHT:
                to_x += char_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    char_x_pos += (to_x * dt)
    char_y_pos += (to_y * dt) 

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > (screen_width-char_width):
        char_x_pos = (screen_width-char_width)
    
    if char_y_pos < 0:
        char_y_pos = 0
    elif char_y_pos > (screen_height-char_height):
        char_y_pos = (screen_height-char_height)

    char_rect = character.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if char_rect.colliderect(enemy_rect):
        print("충돌했어요.")
        running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (char_x_pos,  char_y_pos))
    screen.blit(enemy, (enemy_x_pos,  enemy_y_pos))

    # 흘러간 시간
    elapsed_time = ((pygame.time.get_ticks()  - start_ticks) / 1000) # 단위가 ms 라서 1000으로 나누어, s 로 표시

    # 타이머 설정
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0)) # 정수형으로 바꿔준 것을 문자형으로 바꿔줌 (출력 글자, True, 글자 색상)
    screen.blit(timer, (10, 10))

    # 타이머 시간 초과
    if (total_time - elapsed_time) <= 0:
        print("시간 종료")
        running = False

    pygame.display.update()

# 잠시 대기
pygame.time.delay(1000) # 1초 대기

pygame.quit()