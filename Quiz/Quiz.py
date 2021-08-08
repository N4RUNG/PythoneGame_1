'''
Quiz} 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

[게임 조건]
 1. 캐릭터는 화면 가장 아래에 위치하고, 좌우로만 이동 가능함.
 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정함.
 3. 캐릭터가 똥을 피하면 다음 똥이 자동으로 떨어짐.
 4. 캐릭터가 똥과 충돌하면 게임 종료를 시킴.
 5. FPS는 30으로 고정함.

[게임 이미지]
 1. 배경 : 480×640 (가로×세로) - background.png
 2. 캐릭터 : 70×70 - character.png
 3. 똥 : 70×70 - enemy.png
'''
import pygame
from random import *

######################### 메인 #########################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()
######################### 메인 #########################

# 1. 사용자 게임 설정
# 배경 만들기
background = pygame.image.load("C:/Users/Administrator/Desktop/-/5. git/PythonGame1/Quiz/background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/Administrator/Desktop/-/5. git/PythonGame1/Quiz/character.png")
char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width/2) - (char_width/2)
char_y_pos = screen_height - char_height

# 적 만들기
enemy = pygame.image.load("C:/Users/Administrator/Desktop/-/5. git/PythonGame1/Quiz/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, (screen_width-enemy_width))
enemy_y_pos = 0

# 이동 좌표 설정 (자연스러운 이동을 위해 좌, 우 분리)
to_x_L = 0 # 캐릭터 왼쪽 이동
to_x_R = 0 # 캐릭터 오른쪽 이동
to_y = 0 # 적 이동

# 폰트(글꼴) 설정
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 타이머 시간 시작 정보 저장
start_ticks = pygame.time.get_ticks() # 시간 tick 을 받아옴.

# 게임 실행
running = True # 게임이 진행중인지 확인을 위한 변수 (꺼지지 않도록 유지)
while running:
    # 초당 프레임 설정
    dt = clock.tick(60) # 60프레임
    print(f" fps : {str(clock.get_fps())}")

    # 흘러간 시간
    elapsed_time = ((pygame.time.get_ticks()  - start_ticks) / 1000) # 단위가 ms 라서 1000으로 나누어, s 로 표시
    timer = game_font.render(str(round(elapsed_time, 2)), True, (0, 0, 0)) # 정수형으로 바꿔준 것을 문자형으로 바꿔줌 (출력 글자, True, 글자 색상)

    char_speed = (0.5 + (int(elapsed_time)/200))
    enemy_speed = (0.5 + (int(elapsed_time)/100))

    # 2. 이벤트 처리
    for event in pygame.event.get(): # pygame 을 하기 위해서 무조건 알아야 함 (이벤트를 얻는지 체크하는 것)
        # 게임 종료 이벤트
        if event.type == pygame.QUIT: # 오른쪽 위에 '창 닫기' 버튼을 눌렀을 때 발생하는 이벤트 (창을 닫았을 때 발생)
            running = False # 게임 진행중이 아니라고 설정 후 While문 탈출
        
        # 키보드 누름 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 누른 키가 왼쪽 방향키
                to_x_L -= char_speed
            elif event.key == pygame.K_RIGHT: # 누른 키가 오른쪽 방향키
                to_x_R += char_speed
        
        # 키보드 뗌 이벤트
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: # 뗀 키가 오른 방향키
                to_x_L = 0
            if event.key == pygame.K_RIGHT: # 뗀 키가 오른 방향키
                to_x_R = 0

    # 3. 캐릭터 위치 설정
    char_x_pos += ((to_x_L + to_x_R) * dt) # 프레임에 따라 이동 속도가 차이가 없게 해줌.
    char_y_pos += (to_y * dt) 

    # 적 캐릭터 위치 설정
    enemy_y_pos += (enemy_speed * dt)

    if enemy_y_pos > (screen_height-enemy_height):
        enemy_y_pos = 0
        enemy_x_pos = randint(0, (screen_width-enemy_width))

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

    # 4. 충돌 처리
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
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (char_x_pos,  char_y_pos))
    screen.blit(enemy, (enemy_x_pos,  enemy_y_pos))
    screen.blit(timer, (10, 10))

    # 게임 화면 업데이트
    pygame.display.update() # 게임 화면을 계속 그려줌. (계속 호출되어야 함)

# 잠시 대기
pygame.time.delay(500) # 0.5초 대기

# 게임 종료
pygame.quit() # pygame 종료