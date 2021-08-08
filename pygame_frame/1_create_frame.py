import pygame

# 초기화 (무조건 필요)
pygame.init()

# 화면 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 게임 타이틀 설정
pygame.display.set_caption("Game Name") # 타이틀 이름

# 게임 실행
running = True # 게임이 진행중인지 확인을 위한 변수 (꺼지지 않도록 유지)
while running:
    # 이벤트 대기
    for event in pygame.event.get(): # pygame 을 하기 위해서 무조건 알아야 함 (이벤트를 얻는지 체크하는 것)
        # 게임 종료 이벤트
        if event.type == pygame.QUIT: # 오른쪽 위에 '창 닫기' 버튼을 눌렀을 때 발생하는 이벤트 (창을 닫았을 때 발생)
            running = False # 게임 진행중이 아니라고 설정 후 While문 탈출

# 게임 종료
pygame.quit() # pygame 종료