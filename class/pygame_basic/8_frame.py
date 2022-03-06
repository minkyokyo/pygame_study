
import pygame
###########################################
#기본 초기화 (반드시 해야함)

pygame.init() #초기화 하는 작업, 반드시 해야함 import pygame -> pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름
#event loop가 실행되고 있어야 화면이 꺼지지 않는다

#FPS
clock = pygame.time.Clock();
##################################################################

#1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도,폰트 등)


running = True #게임이 진행중인가?


while running:
    #dt는 델타
    dt = clock.tick(30)#tick안에 원하는 프레임수를 넣는다. 게임화면의 초당 프레임수 설정
    
    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생되었는지
        if event.type == pygame.QUIT: #닫기 버튼
            running = False
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌처리
 
    # 5. 화면에 그리기


    #매 프레임마다 화면을 그려줘야 한다. 반드시 계속해서 호출 되어야 한다.
    pygame.display.update() 

#pygame 종료
pygame.quit()