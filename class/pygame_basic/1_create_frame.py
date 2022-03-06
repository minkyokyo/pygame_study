import pygame

pygame.init() #초기화 하는 작업, 반드시 해야함 import pygame -> pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름
#event loop가 실행되고 있어야 화면이 꺼지지 않는다

# 이벤트 루프
running = True #게임이 진행중인가?

'''
이벤트 루프 : 프로그램이 종료되지 않도록 계속 이벤트가 들어오나 예의 주시하면서 대기.
사용자가 키보드 입력하는지, 마우스를 동작하는지,,,

'''
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생되었는지
        if event.type == pygame.QUIT: #닫기 버튼
            running = False
#pygame 종료
pygame.quit()

