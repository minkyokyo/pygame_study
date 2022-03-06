#FPS -> 초당 프레임 수 
#프레임 수가 높으면 부드럽다잉~

from ast import If
import pygame

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

#배경화면 설정
background = pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\character.png")
#캐릭터의 사이즈를 알아야한다.
character_size = character.get_rect().size #rectagle의 약자? rect = 사각형
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
#캐릭터의 위치
character_x_position = screen_width/2 - character_width/2 #화면 가로의 절반 크기 = 가운데
character_y_position = screen_height-character_height #화면 세로의  가장 아래 

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed =0.6

# 적 enemy 캐릭터
#캐릭터(스프라이트) 불러오기
enemy= pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\enemy.png")
#캐릭터의 사이즈를 알아야한다.
enemy_size = enemy.get_rect().size #rectagle의 약자? rect = 사각형
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
#캐릭터의 위치
enemy_x_position = screen_width/2 - enemy_width/2 #화면 가로의 절반 크기 = 가운데
enemy_y_position = screen_height/2-enemy_height #화면 세로의  가장 아래 


# 이벤트 루프
running = True #게임이 진행중인가?

'''
이벤트 루프 : 프로그램이 종료되지 않도록 계속 이벤트가 들어오나 예의 주시하면서 대기.
사용자가 키보드 입력하는지, 마우스를 동작하는지,,,

'''
while running:
    #dt는 델타
    dt = clock.tick(60)#tick안에 원하는 프레임수를 넣는다. 게임화면의 초당 프레임수 설정

# 캐릭터가 100만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10*10  = 100
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동. -> 5*20 = 100
# 똑같이 이동하기 위해서 프레임별로 이동하는 양이 달라져야 한다. 보정해야한다.

    print("fps : ", str(clock.get_fps()))
    for event in pygame.event.get(): #어떤 이벤트가 발생되었는지
        if event.type == pygame.QUIT: #닫기 버튼
            running = False
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인.
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -=character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x +=character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로
                to_y -=character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로
                to_y +=character_speed
                
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 
    
    #여기서 보정을 해줌. dt(델타 값을) 곱해준다.
    character_x_position += to_x *dt
    character_y_position += to_y *dt
    
    #가로 경계값 처리
    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
    
    #세로 경곗값 처리
    
    if character_y_position < 0:
        character_y_position = 0
    elif character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height       
    screen.blit(background,(0,0)) #백그라운드가 어디 나타날지 좌표 설정
    #0,0 -> 맨 왼쪽 위   
    
    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position
    
    #충돌 체크
    #coliderect -> 사각형 기준으로 충돌이 있었는지 확인
    if character_rect.colliderect(enemy_rect): #캐릭터가 적과 충돌 했는가?
            print("충돌함")
            running=False    
    
    screen.blit(character,(character_x_position,character_y_position)) #캐릭터 그리기
    
    screen.blit(enemy,(enemy_x_position ,enemy_y_position))
    
    #매 프레임마다 화면을 그려줘야 한다. 반드시 계속해서 호출 되어야 한다.
    pygame.display.update() 

#pygame 종료
pygame.quit()