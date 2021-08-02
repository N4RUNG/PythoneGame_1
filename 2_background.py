import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\back.png") # \를 /로 바꿔도 되고 \\로 해도 됨.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 게임 이미지 설정
    screen.fill((255, 255, 255)) # RGB 값을 받아서 화면을 채워줌.
#    screen.blit(background, (0, 0)) # 이미랑 어디에 나타날 지 좌표를 적음. (좌표는 튜플 형식으로)

    # 게임 화면 업데이트
    pygame.display.update() # 게임 화면을 계속 그려줌. (계속 호출되어야 함)

pygame.quit()