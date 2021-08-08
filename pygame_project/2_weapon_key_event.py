import pygame
from os import *
from random import *

######################### 메인 #########################
# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기 설정
screen_height = 480 # 세로 크기 설정
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")

# FPS
clock = pygame.time.Clock()
######################### 메인 #########################

# 1. 사용자 게임 설정
# 현재 파일 설정
current_path = path.dirname(__file__) # 현재 파일의 위치 반환
image_path = path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 높이 계산

# 캐릭터 만들기
character = pygame.image.load(path.join(image_path, "character.png"))
char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width/2) - (char_width/2)
char_y_pos = screen_height-char_height-stage_height

# 무기 만들기
weapon = pygame.image.load(path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] # 캐릭터 중앙에서 나가게 함
weapons = [] # 무기 한 번에 여러 발 발사를 가능하게 함

# 이동 좌표 설정 (자연스러운 이동을 위해 좌, 우 분리)
to_x_L = 0 # 캐릭터 왼쪽 이동
to_x_R = 0 # 캐릭터 오른쪽 이동
to_y = 0 # 적 이동

# 이동 속도 설정
char_speed = 5
weapon_speed = 10

# 게임 실행
running = True # 게임이 진행중인지 확인을 위한 변수 (꺼지지 않도록 유지)
while running:
    # 초당 프레임 설정
    dt = clock.tick(30)

    # 2. 이벤트 처리
    for event in pygame.event.get(): # pygame 을 하기 위해서 무조건 알아야 함 (이벤트를 얻는지 체크하는 것)
        # 게임 종료 이벤트
        if event.type == pygame.QUIT: # 오른쪽 위에 '창 닫기' 버튼을 눌렀을 때 발생하는 이벤트 (창을 닫았을 때 발생)
            running = False # 게임 진행중이 아니라고 설정 후 While문 탈출
        
        # 키보드 누름 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 누른 키가 왼쪽 방향키
                to_x_L -= char_speed
            if event.key == pygame.K_RIGHT: # 누른 키가 오른쪽 방향키
                to_x_R += char_speed
            if event.key == pygame.K_SPACE: # 누른 키가 스페이스바
                weapon_x_pos = char_x_pos + (char_width/2) - (weapon_width/2)
                weapon_y_pos = char_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        # 키보드 뗌 이벤트
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: # 뗀 키가 오른 방향키
                to_x_L = 0
            if event.key == pygame.K_RIGHT: # 뗀 키가 오른 방향키
                to_x_R = 0

    # 3. 캐릭터 위치 설정
    char_x_pos += (to_x_L + to_x_R) # 프레임에 따라 이동 속도가 차이가 없게 해줌.
    char_y_pos += to_y

    # 가로 경계
    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > (screen_width-char_width):
        char_x_pos = (screen_width-char_width)
    
    # 무기 위치 설정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(character, (char_x_pos, char_y_pos))
    screen.blit(stage, (0, (screen_height-stage_height)))

    # 게임 화면 업데이트
    pygame.display.update() # 게임 화면을 계속 그려줌. (계속 호출되어야 함)

# 잠시 대기
pygame.time.delay(500) # 0.5초 대기

# 게임 종료
pygame.quit() # pygame 종료