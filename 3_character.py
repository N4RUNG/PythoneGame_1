import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\back.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\chac.png")
char_size = character.get_rect().size # 이미지의 크기를 구해올 수 있음.
char_width = char_size[0] # 캐릭터의 가로 크기
char_height = char_size[1] # 캐릭터의 새로 크기
char_x_pos = (screen_width/2) - (char_width/2) # 화면 가로 크기의 절반에서 캐릭터 가로의 크기의 절반을 뺀 위치 (중앙)
char_y_pos = screen_height - char_height # 화면 세로 크기의 아래에서 캐릭터 세로 크기를 뺀 위치

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))

    # 게임 캐릭터 설정
    screen.blit(character, (char_x_pos,  char_y_pos))

    pygame.display.update()

pygame.quit()