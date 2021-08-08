import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\pygame_frame\\back.png")

character = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\pygame_frame\\chac.png")
char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width/2) - (char_width/2)
char_y_pos = screen_height - char_height

# 이동 좌표
to_x_L = 0
to_x_R = 0
to_y_U = 0
to_y_D = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 키보드 누름 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # 누른 키가 위쪽 방향키
                to_y_U -= 1
            if event.key == pygame.K_DOWN: # 누른 키가 아래쪽 방향키
                to_y_D += 1
            if event.key == pygame.K_LEFT: # 누른 키가 왼쪽 방향키
                to_x_L -= 1
            if event.key == pygame.K_RIGHT: # 누른 키가 오른쪽 방향키
                to_x_R += 1
        
        # 키보드 뗌 이벤트
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: # 뗀 키가 위 방향키
                to_y_U = 0
            if event.key == pygame.K_DOWN: # 뗀 키가 아래 방향키
                to_y_D = 0
            if event.key == pygame.K_LEFT: # 뗀 키가 왼 방향키
                to_x_L = 0
            if event.key == pygame.K_RIGHT: # 뗀 키가 오른 방향키
                to_x_R = 0

    # 캐릭터 이동
    char_x_pos += (to_x_L+to_x_R)
    char_y_pos += (to_y_U+to_y_D) 

    # 가로 경계
    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > (screen_width-char_width):
        char_x_pos = (screen_width-char_width)
    
    # 세로 경계
    if char_y_pos < 0:
        char_y_pos = 0
    elif char_y_pos > (screen_height-char_height):
        char_y_pos = (screen_height-char_height)

    screen.blit(background, (0, 0))
    screen.blit(character, (char_x_pos,  char_y_pos))

    pygame.display.update()

pygame.quit()