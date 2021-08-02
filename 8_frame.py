import pygame

# 초기화 (무조건 필요)
pygame.init()

# 화면 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 게임 타이틀 설정
pygame.display.set_caption("Game Name") # 타이틀 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\back.png") # \를 /로 바꿔도 되고 \\로 해도 됨.

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\Administrator\\Desktop\\-\\5. git\\PythonGame1\\chac.png")
char_size = character.get_rect().size # 이미지의 크기를 구해올 수 있음.
char_width = char_size[0] # 캐릭터의 가로 크기
char_height = char_size[1] # 캐릭터의 새로 크기
char_x_pos = (screen_width/2) - (char_width/2) # 화면 가로 크기의 절반에서 캐릭터 가로의 크기의 절반을 뺀 위치 (중앙)
char_y_pos = screen_height - char_height # 화면 세로 크기의 아래에서 캐릭터 세로 크기를 뺀 위치

# 이동 좌표
to_x = 0
to_y = 0

# 이동 속도
char_speed = 1

# 적 캐릭터 불러오기
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

# 게임 실행
running = True # 게임이 진행중인지 확인을 위한 변수 (꺼지지 않도록 유지)
while running:
    # 초당 프레임 설정
    dt = clock.tick(60) # 60프레임
    print(f" fps : {str(clock.get_fps())}")

    # 이벤트 대기
    for event in pygame.event.get(): # pygame 을 하기 위해서 무조건 알아야 함 (이벤트를 얻는지 체크하는 것)
        # 게임 종료 이벤트
        if event.type == pygame.QUIT: # 오른쪽 위에 '창 닫기' 버튼을 눌렀을 때 발생하는 이벤트 (창을 닫았을 때 발생)
            running = False # 게임 진행중이 아니라고 설정 후 While문 탈출
        
        # 키보드 누름 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # 누른 키가 위쪽 방향키
                to_y -= char_speed
            if event.key == pygame.K_DOWN: # 누른 키가 아래쪽 방향키
                to_y += char_speed
            if event.key == pygame.K_LEFT: # 누른 키가 왼쪽 방향키
                to_x -= char_speed
            if event.key == pygame.K_RIGHT: # 누른 키가 오른쪽 방향키
                to_x += char_speed
        
        # 방향키를 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: # 뗀 키가 위, 아래 방향키
                to_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 뗀 키가 왼, 오른 방향키
                to_x = 0
    
    # 캐릭터 이동
    char_x_pos += (to_x * dt) # 프레임에 따라 이동 속도가 차이가 없게 해줌.
    char_y_pos += (to_y * dt) 

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
    
    # 게임 이미지 설정
    screen.blit(background, (0, 0)) # 이미랑 어디에 나타날 지 좌표를 적음. (좌표는 튜플 형식으로)

    # 게임 캐릭터 설정
    screen.blit(character, (char_x_pos,  char_y_pos))

    # 적 캐릭터 설정
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

    # 게임 화면 업데이트
    pygame.display.update() # 게임 화면을 계속 그려줌. (계속 호출되어야 함)

# 잠시 대기
pygame.time.delay(1000) # 1초 대기

# 게임 종료
pygame.quit() # pygame 종료