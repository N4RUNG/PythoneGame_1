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

# 공 만들기
ball_images = [
    pygame.image.load(path.join(image_path, "balloon1.png")),
    pygame.image.load(path.join(image_path, "balloon2.png")),
    pygame.image.load(path.join(image_path, "balloon3.png")),
    pygame.image.load(path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 속도
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3

# 공
balls = [] # 한 번에 관리하기 위해 사전으로 저장
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 위에 쓴 공의 이미지 index 값
    "to_x" : 3, # 공의 x 이동 속도 ( 3이면 오른쪽으로 3의 속력으로, -3이면 왼쪽 방향으로 )
    "to_y" : -6, # 공의 y 이동 속도
    "init_spd_y" : ball_speed_y[0]}) # y 최초 속도


# 이동 좌표 설정 (자연스러운 이동을 위해 좌, 우 분리)
to_x_L = 0 # 캐릭터 왼쪽 이동
to_x_R = 0 # 캐릭터 오른쪽 이동
to_y = 0 # 적 이동

# 이동 속도 설정
char_speed = 7
weapon_speed = 10

# 사라질 무기, 공 정보
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작 시간

# 기본 게임 종료 메시지
game_result = "Game Over"

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

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls): # enumerate() 을 사용하면 리스트안에 있는 값의 idx 값과 그에 해당하는 값을 출력함.
        ball_x_pos = ball_val["pos_x"] # ball_val 에 있는 "pos_x" 의 값을 집어 넣음.
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size # 위에서 가져온 이미지 index 값 사용
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        # 가로 경계 효과
        if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:
            ball_val["to_x"] *= -1 # 좌우 변환을 위해 부호 변경함.
        
        # 세로 경계 효과
        if ball_y_pos > screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"] # 바닥에서 튕겨서 위로 올라감.
        else: # 바닥에 닿아서 튕겨 올라갈 때 외에는 속력을 감소시킴.
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    
    # 4. 충돌 처리
    # 캐릭터 rect
    char_rect = character.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    # 공 rect
    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_x_pos
        ball_rect.top = ball_y_pos

        # 캐릭터 <> 공
        if char_rect.colliderect(ball_rect):
            running = False
            break

        # 무기 rect
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            # 무기 <> 공
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                if ball_img_idx < 3: # 공의 이미지 값이 가장 작은 공이 아닌지 체크
                    # 현재 공 크기 체크
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 나눠진 공
                    balls.append({ # 왼쪽으로 튕겨가는 공
                        "pos_x" : ball_x_pos + (ball_width/2) - (small_ball_width/2),
                        "pos_y" : ball_y_pos + (ball_height/2) - (small_ball_height/2),
                        "img_idx" : ball_img_idx+1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx+1]})

                    balls.append({ # 오른쪽으로 튕겨나가는 공
                        "pos_x" : ball_x_pos + (ball_width/2) - (small_ball_width/2),
                        "pos_y" : ball_y_pos + (ball_height/2) - (small_ball_height/2),
                        "img_idx" : ball_img_idx+1,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx+1]})
                break
            break

    # 무기 <> 공 충돌 처리
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    # 모든 공이 사라짐
    if len(balls) == 0 :
        game_result = " Mission Complete !"
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_x_pos = val["pos_x"]
        ball_y_pos = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_x_pos, ball_y_pos))
    screen.blit(character, (char_x_pos, char_y_pos))
    screen.blit(stage, (0, (screen_height-stage_height)))

    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms를 s로 바꿈
    timer = game_font.render(f"Time : {int(total_time - elapsed_time)}", True, (0, 0, 0))
    timer_size = timer.get_rect().size
    screen.blit(timer, (screen_width - timer_size[0] - 10, 10))

    # 시간 초과
    if total_time - elapsed_time <= 0:
        game_result = " Time Out !"
        running = False

    # 게임 화면 업데이트
    pygame.display.update() # 게임 화면을 계속 그려줌. (계속 호출되어야 함)

# 게임 오버 메시지 출력
msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# 게임 종료
pygame.quit() # pygame 종료