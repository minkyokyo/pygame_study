import pygame
import random

pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기") #게임 이름
#event loop가 실행되고 있어야 화면이 꺼지지 않는다

#배경화면 설정
background = pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\paper_background.png")


#FPS
clock = pygame.time.Clock();

#캐릭터 설정
character =  pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\angel.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height-character_height

character_speed = 0.6

#이동할 좌표
to_x = 0

#똥 설정
pooh =  pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\poop_fence.png")
pooh_size = pooh.get_rect().size
pooh_width = pooh_size[0]
pooh_height = pooh_size[1]
pooh_x_pos = random.randrange(0,screen_width-pooh_width)
pooh_y_pos = 0

pooh_speed = 0.4

# 폰트 정의
game_font = pygame.font.Font(None,40) #폰트 객체 생성 ( 폰트 , 크기)
#총 시간
total_time = 10
#시작 시간 정보
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴


def game_lose():
    #text
    game_over_text = game_font.render("GAME OVER",True,(0,0,0))
    screen.blit(background,(0,0))
    screen.blit(game_over_text,(screen_width/2,screen_height/2))
    pygame.display.update()

# 이벤트 루프
running = True #게임이 진행중인가?

while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get(): #어떤 이벤트가 발생되었는지
        if event.type == pygame.QUIT: #닫기 버튼
            running = False
        
        if event.type == pygame.KEYDOWN: # 키를 눌렀을 때,
            if event.key == pygame.K_LEFT:
                to_x -=character_speed
            if event.key == pygame.K_RIGHT:
                to_x +=character_speed
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:#키를 눌렀다가 떼었을 때,
                to_x=0
    
    
    #캐릭터 이동
    character_x_pos += to_x *dt
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #똥 떨어짐
    if pooh_y_pos > screen_height:
        pooh_y_pos = 0
        pooh_x_pos = random.randrange(0,screen_width-pooh_width)

    pooh_y_pos+=pooh_speed *dt
    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = pooh.get_rect()
    enemy_rect.left = pooh_x_pos
    enemy_rect.top = pooh_y_pos
    
    #충돌 체크
    #coliderect -> 사각형 기준으로 충돌이 있었는지 확인
    if character_rect.colliderect(enemy_rect): #캐릭터가 적과 충돌 했는가?
            character =  pygame.image.load("D:\\develop\\Game\\python_game\\class\\resource\\image\\dead_angel.png")
            screen.blit(character,(character_x_pos,character_y_pos))
            pygame.display.update()
            #잠시 대기
            pygame.time.delay(1000) #2초 정도 대기
            
            #game_lose()
            running=False    
           
    
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(pooh,(pooh_x_pos,pooh_y_pos))
    
    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 
    #경과 시간(ms)을 1000으로 나누어서 초 단위로 표시.
    
    timer=game_font.render("Time : "+str(int(elapsed_time)), True,(0,0,0))
    screen.blit(timer, (10,10))
    
    pygame.display.update() 
     


#잠시 대기
pygame.time.delay(2000) #2초 정도 대기

#pygame 종료
pygame.quit()