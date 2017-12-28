import pygame,random
from random import randint

pygame.init()

display_width=800
display_height=600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
blue = (0,70,250)

img =pygame.image.load('Green-School-Board.png')
img2 =pygame.image.load('arrows.png')

posArr=((300,100),(370,100),(440,100),(510,100),(580,100),(650,100),(720,100),
        (300,170),(370,170),(440,170),(510,170),(580,170),(650,170),(720,170),
        (300,240),(370,240),(440,240),(510,240),(580,240),(650,240),(720,240),
        (300,310),(370,310),(440,310),(510,310),(580,310),(650,310),(720,310),
        (300,380),(370,380),(440,380),(510,380),(580,380),(650,380),(720,380),
        (300,450),(370,450),(440,450),(510,450),(580,450),(650,450),(720,450))
colorArr=[0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,
          0,0,0,0,0,0,0]
winningVerticalCombos = {0: [0, 7, 14, 21], 1: [7, 14, 21, 28], 2:[14, 21, 28, 35], 3: [1, 8, 15, 22],
                4: [8, 15, 22, 29], 5: [15, 22, 29, 36], 6: [2, 9, 16, 23], 7: [9, 16, 23, 30],
                8: [16, 23, 30, 37], 9: [3, 10, 17, 24], 10: [10, 17, 24, 31], 11: [17, 24, 31, 38],
                12: [4, 11, 18, 25], 13: [11, 18, 25, 32], 14: [18, 25, 32, 39], 15: [5, 12, 19, 26],
                16: [12, 19, 26, 33], 17: [19, 26, 33, 40], 18: [6, 13, 20, 27], 19: [13, 20, 27, 34],
                20: [ 20, 27, 34, 41]};

#24 total
winningHorizontalCombos = {0: [0, 1, 2, 3], 1: [1, 2, 3, 4], 2: [2, 3, 4, 5], 3: [3, 4, 5, 6],
                            4: [7, 8, 9, 10], 5: [8, 9, 10, 11], 6: [9, 10, 11, 12], 7: [10, 11, 12, 13], 
                            8: [14, 15, 16, 17], 9: [15, 16, 17, 18], 10: [16, 17, 18, 19], 11: [17, 18, 19, 20],
                            12: [21, 22, 23, 24], 13: [22, 23, 24, 25], 14: [23, 24, 25, 26], 15: [24, 25, 26, 27], 
                            16: [28, 29, 30, 31], 17: [29, 30, 31, 32], 18: [30, 31, 32, 33], 19: [31, 32, 33, 34],
                            20: [35, 36, 37, 38], 21: [36, 37, 38, 39], 22: [37, 38, 39, 40], 23: [38, 39, 40, 41]};
#24 total
winningDiagonalCombos = {0: [0, 8, 16, 24], 1: [7, 15, 23, 31], 2: [14, 22, 30, 38],
                            3: [1, 9, 17, 25], 4: [8, 16, 24, 32], 5: [15, 23, 31, 34], 
                            6: [2, 10, 18, 26], 7: [9, 17, 25, 33], 8: [16, 24, 32, 40],
                            9: [3, 11, 19, 27], 10: [10, 18, 26, 34], 11: [17, 25, 33, 41],
                            12: [3, 9, 15, 21], 13: [10, 16, 22, 28], 14: [17, 23, 29, 35],
                            15: [4, 10, 16, 22], 16: [11, 17, 23, 29], 17: [18, 24, 30, 36],
                            18: [5, 11, 17, 23], 19: [12, 18, 24, 30],20: [19, 25, 31, 37],
                            21: [6, 12, 18, 24], 22: [13, 19, 25, 31], 23: [20, 26, 32, 38]};

range_x=(260,330,400,470,540,615,680,750)

range_y=(60,135,205,275,345,415,485,555)


blue_arr=((367,72),(457,72),(547,72),(637,72),
              (322,117),(412,117),(502,117),(592,117),
              (367,162),(457,162),(547,162),(637,162))

white_arr=((322,387),(412,387),(502,387),(592,387),
              (367,342),(457,342),(547,342),(637,342),
              (322,297),(412,297),(502,297),(592,297))

sqr_arr=([(0,0),(345,50),(0,0),(435,50),(0,0),(525,50),(0,0),(615,50)],
              [(300,95),(0,0),(390,95),(0,0),(480,95),(0,0),(570,95),(0,0)],
              [(0,0),(345,140),(0,0),(435,140),(0,0),(525,140),(0,0),(615,140)],
              [(300,185),(0,0),(390,185),(0,0),(480,185),(0,0),(570,185),(0,0)],
              [(0,0),(345,230),(0,0),(435,230),(0,0),(525,230),(0,0),(615,230)],
              [(300,275),(0,0),(390,275),(0,0),(480,275),(0,0),(570,275),(0,0)],
              [(0,0),(345,320),(0,0),(435,320),(0,0),(525,320),(0,0),(615,320)],
              [(300,365),(0,0),(390,365),(0,0),(480,365),(0,0),(570,365),(0,0)])

piece_arr=([(0,0),(367,72),(0,0),(457,72),(0,0),(547,72),(0,0),(637,72)],
              [(322,117),(0,0),(412,117),(0,0),(502,117),(0,0),(592,117),(0,0)],
              [(0,0),(367,162),(0,0),(457,162),(0,0),(547,162),(0,0),(637,162)],
              [(322,207),(0,0),(412,207),(0,0),(502,207),(0,0),(592,207),(0,0)],
              [(0,0),(367,252),(0,0),(457,252),(0,0),(547,252),(0,0),(637,252)],
              [(322,297),(0,0),(412,297),(0,0),(502,297),(0,0),(592,297),(0,0)],
              [(0,0),(367,342),(0,0),(457,342),(0,0),(547,342),(0,0),(637,342)],
              [(322,387),(0,0),(412,387),(0,0),(502,387),(0,0),(592,387),(0,0)])

range_sqr_x=(300,345,390,435,480,525,570,615,660)

range_sqr_y=(50,95,140,185,230,275,320,365,410)

click_x=(295,345,390,435,480,525,570,615,660)

click_y=(50,95,140,185,230,275,320,365,410)

boared_arr=[[0,2,0,2,0,2,0,2],
            [2,0,2,0,2,0,2,0],
            [0,2,0,2,0,2,0,2],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]]

options=[]
choice=False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("2 games in 1")
clock = pygame.time.Clock()

def text_objects(text, font,color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()
def text_settings(display,x,y,z,k,txt,txt_color,size):
    smallText = pygame.font.Font("chawp.ttf",size)
    textSurf,textReact = text_objects(txt, smallText,txt_color)
    textReact.center = (x+(z/2),y+(k/2))
    display.blit(textSurf,textReact)

def button(display,x,y,z,k,txt,action=None,size=40):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+z > mouse[0] > x and y+k > mouse[1] > y:
        text_settings(display,x,y,z,k,txt,black,size)
        if click[0] == 1 and action != None:
            pygame.mixer.music.load('Tiny Button Push-Sound.mp3')
            pygame.mixer.music.play(0)
            if action == "exit":
                terminate_game()
            elif action == "instructions":
                instructions()
            elif action == "connect four":
                connect_four()
            elif action == "checkers":
                checkers() 
            elif action == "menu":
                game_intro()
            elif action == "checkers_instructions":
                checkers_instructions()
            elif action== "connect_four_instructions":
                connect_four_instructions()
                
    else:
        text_settings(display,x,y,z,k,txt,white,size)

def game_intro():
    gameDisplay.fill(white)
    gameDisplay.blit(img,(0,0))
    largeText = pygame.font.Font("chawp.ttf",100)
    textSurf,textReact=text_objects("2 games in 1",largeText,white)
    textReact.center=((display_width/2),(display_height/5))
    gameDisplay.blit(textSurf,textReact)
    update_game()
    clock.tick(15)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
        reset()
        button(gameDisplay, 300, 200, 200, 50,"checkers","checkers")
        button(gameDisplay, 300, 270, 200, 50,"connect four","connect four") 
        button(gameDisplay, 300, 340, 200, 50,"instructions","instructions") 
        button(gameDisplay, 300, 410, 200, 50,"exit","exit")                
        update_game()      

def checkers():
    '''
    activates the checkers window
    '''
    gameDisplay.fill(white)
    gameDisplay.blit(img,(0,0))
    text_settings(gameDisplay, 100, 50, 100, 100, "player 1", white, 20)
    text_settings(gameDisplay, 100, 70, 100, 100, "vs", white, 20)
    text_settings(gameDisplay, 100, 90, 100, 100, "computer", white, 20)
    text_settings(gameDisplay, 100, 120, 100, 100, "good luck!!!", white, 20)
    boared_checkers()
    global options
    global choice
    turn=randint(1,2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn==1:
                    if mark_player(choice)==-1:
                        choice=True
                        options=player_moves()
                    else:
                        choice=False
                    if make_move(options):
                        turn=change(turn)
            if turn==2:
                if run_ai():
                    turn=change(turn)
                
        button(gameDisplay, 70, 470, 70, 50, "menu", "menu")    
        update_game()
        clock.tick(60)
        

def clicked_piece():
    '''
    returns the index of the matrix where the clicked piece is found
    '''
    mouse=pygame.mouse.get_pos()
    x,y=-1,0
    for i in range(len(click_x)-1):
        if click_x[i]<mouse[0]<click_x[i+1]:
            x=i
    for j in range(len(click_y)-1):
        if click_y[j]<mouse[1]<click_y[j+1]:
            y=j
    return (x,y)

def clicked_sqr():
    '''
    returns the index of the matrix where the clicked sqr is found
    '''
    mouse=pygame.mouse.get_pos()
    x,y=-1,0
    for i in range(len(click_x)-1):
        if range_sqr_x[i]<mouse[0]<range_sqr_x[i+1]:
            x=i
    for j in range(len(click_y)-1):
        if range_sqr_y[j]<mouse[1]<range_sqr_y[j+1]:
            y=j
    return (x,y)

def check_move(p):
    '''
    check if a move is available for player including eating option and return the index where the move can be preformed 
    '''
    x,y=(-1,0),(-1,0)
    l1,l2=0,7
    #h1 is left,h2 is right
    h1,h2=(p[0]-1,p[1]-1),(p[0]+1,p[1]-1)
    #working with matrix p[1]-x and p[0]-y
    if l1<=p[0]<=l2 and l1<=p[1]<=l2:
        if  boared_arr[p[1]][p[0]]!=0:
            if l1<=h1[0]<=l2:
                if boared_arr[h1[1]][h1[0]]==0:
                    x=h1 
            if l1<=h2[0]<=l2:
                if boared_arr[h2[1]][h2[0]]==0:
                    y=h2
    return (x,y)

def check_move_ai(p):
    x,y=(-1,0),(-1,0)
    l1,l2=0,7
    #h1 is left,h2 is right
    h1,h2=(p[0]-1,p[1]+1),(p[0]+1,p[1]+1)
    #working with matrix p[1]-x and p[0]-y
    if l1<=p[0]<=l2 and l1<=p[1]<=l2:
        if  boared_arr[p[1]][p[0]]!=0:
            if l1<=h1[0]<=l2:
                if boared_arr[h1[1]][h1[0]]==0:
                    x=h1 
            if l1<=h2[0]<=l2:
                if boared_arr[h2[1]][h2[0]]==0:
                    y=h2
    return (x,y)
    
def check_eat(p):
    '''
    check if a eat is avilable  for player includeing eating option and return the index where the move can be preformed 
    '''
    x,y=(-1,0),(-1,0)
    l1,l2=0,7
    #h1 is left,h2 is right
    h1,h2=(p[0]-1,p[1]-1),(p[0]+1,p[1]-1)
    nh1,nh2=(p[0]-2,p[1]-2),(p[0]+2,p[1]-2)
    if l1<=nh1[0]<=l2 and l1<=nh1[1]<=l2 and l1<=h1[0]<=l2 and l1<=h1[1]<=l2:
        if boared_arr[h1[1]][h1[0]]==2 and boared_arr[nh1[1]][nh1[0]]==0:
            x=nh1
    if l1<=nh2[0]<=l2 and l1<=nh2[1]<=l2 and l1<=h2[0]<=l2 and l1<=h2[1]<=l2:
        if boared_arr[h2[1]][h2[0]]==2 and boared_arr[nh2[1]][nh2[0]]==0:
            y=nh2
    return(x,y)

def check_eat_ai(p):
    x,y=(-1,0),(-1,0)
    l1,l2=0,7
    #h1 is left,h2 is right
    h1,h2=(p[0]-1,p[1]+1),(p[0]+1,p[1]+1)
    nh1,nh2=(p[0]-2,p[1]+2),(p[0]+2,p[1]+2)
    if l1<=nh1[0]<=l2 and l1<=nh1[1]<=l2 and l1<=h1[0]<=l2 and l1<=h1[1]<=l2:
        if boared_arr[h1[1]][h1[0]]==1 and boared_arr[nh1[1]][nh1[0]]==0:
            x=nh1
    if l1<=nh2[0]<=l2 and l1<=nh2[1]<=l2 and l1<=h2[0]<=l2 and l1<=h2[1]<=l2:
        if boared_arr[h2[1]][h2[0]]==1 and boared_arr[nh2[1]][nh2[0]]==0:
            y=nh2
    return(x,y)

def player_moves():
    '''
    returns a list of the two options of the selected piece if theres no options returns 
    an empty list if there is only 1 options return a list with len 1
    '''
    k=clicked_piece()
    options=[k]
    m=check_move(k)
    e=check_eat(k)
    if m[0][0]!=-1:
        options.append(('movel',m[0]))
    if m[1][0]!=-1:
        options.append(('mover',m[1]))
    if e[0][0]!=-1:
        options.append(('eatl',e[0]))
    if e[1][0]!=-1:
        options.append(('eatr',e[1]))    
    return options

def player_king_moves():
    k=clicked_piece()
    options=player_moves()
    m=check_move_ai(k)
    e=check_eat_ai(k)
    if m[0][0]!=-1:
        options.append(('moveld',m[0]))
    if m[1][0]!=-1:
        options.append(('moverd',m[1]))
    if e[0][0]!=-1:
        options.append(('eatld',e[0]))
    if e[1][0]!=-1:
        options.append(('eatrd',e[1]))    
    return options

def random_pieace():
    random.seed()
    while True:
        x=randint(0,7)
        y=randint(0,7)
        if boared_arr[y][x]==2 or boared_arr[y][x]==4:
            return (x,y)
        
def ai_moves():
    k=random_pieace()
    options=[k]
    m=check_move_ai(k)
    e=check_eat_ai(k)
    if m[0][0]!=-1:
        options.append(('move',m[0]))
    if m[1][0]!=-1:
        options.append(('move',m[1]))
    if e[0][0]!=-1:
        options.append(('eatld',e[0]))
    if e[1][0]!=-1:
        options.append(('eatrd',e[1]))    
    return options

def run_ai():
    k=ai_moves()
    while len(k)==1:
        k=ai_moves()
    if k[1][0]=='eatld' or k[1][0]=='eatrd':
        move_ai(k[0],k[1][1],k[1][0])
        return True
    if len(k)==3:
        if k[2][0]=='eatld' or k[2][0]=='eatrd':
            move_ai(k[0],k[2][1],k[2][0])
            return True
    if len(k)==2:
        move_ai(k[0],k[1][1],k[1][0])
        return True
    else:
        num=randint(1,2)
        move_ai(k[0],k[num][1],k[num][0])
        return True
    return False

def move_ai(i,n,msg):
    '''
    set the piece on the boared after selected place and delete last place of piece
    '''
    
    '''
    change the other value in the sqr u stupid son of a bitch 
    '''
    if msg=='move':
        boared_arr[n[1]][n[0]]=2
        boared_arr[i[1]][i[0]]=0
        circle(blue, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
    elif msg=='eatl':
        boared_arr[n[1]][n[0]]=2
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]-1][i[0]-1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]-1][i[0]-1][0],sqr_arr[i[1]-1][i[0]-1][1],45,45)
        circle(blue, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
    elif msg=='eatr':
        boared_arr[n[1]][n[0]]=2
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]-1][i[0]+1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]-1][i[0]+1][0],sqr_arr[i[1]-1][i[0]+1][1],45,45)
        circle(blue, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
    elif msg=='eatld':
        boared_arr[n[1]][n[0]]=2
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]+1][i[0]-1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]+1][i[0]-1][0],sqr_arr[i[1]+1][n[0]-1][1],45,45)
        circle(blue, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)    
    elif msg=='eatrd':
        boared_arr[n[1]][n[0]]=2
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]+1][i[0]+1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]+1][i[0]+1][0],sqr_arr[i[1]+1][i[0]+1][1],45,45)
        circle(blue, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)

def mark_player(choice):
    '''
    mark the player if there is an option to move include eat
    '''
    options=player_moves()
    i=piece_arr[options[0][1]][options[0][0]][0]
    j=piece_arr[options[0][1]][options[0][0]][1]
    
    if len(options)>1:
        if boared_arr[options[0][1]][options[0][0]]==1 and not choice:
            circle(red,i,j,20,0)
            boared_arr[options[0][1]][options[0][0]]=-1
            return -1
        elif boared_arr[options[0][1]][options[0][0]]==-1:
            circle(white,i,j,20,0)
            boared_arr[options[0][1]][options[0][0]]=1
            return 1
    return None
           

                
            
def make_move(options):
    '''
    checks if clicked sqr equals to possible move and move the player if can
    '''
    k=clicked_sqr()
    size=len(options)
    l1,l2=0,7
    i=1
    if l1<=options[0][0]<=l2 and l1<=options[0][1]<=l2:
        if boared_arr[options[0][1]][options[0][0]]==-1:
            while i<size:
                if k==options[i][1]:
                    if options[i][0]=='movel':
                        move(options[0],k,'move')
                        return True
                    elif options[i][0]=='mover':
                        move(options[0],k,'move')
                        return True
                    elif options[i][0]=='eatl':
                        move(options[0],k,'eatl')
                        return True
                    elif options[i][0]=='eatr':
                        move(options[0],k,'eatr')
                        return True
                i+=1
    return False

def move(i,n,msg):
    '''
    set the piece on the boared after selected place and delete last place of piece
    '''
    if msg=='move':
        boared_arr[n[1]][n[0]]=1
        boared_arr[i[1]][i[0]]=0
        circle(white, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
    elif msg=='eatl':
        boared_arr[n[1]][n[0]]=1
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]-1][i[0]-1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]-1][i[0]-1][0],sqr_arr[i[1]-1][i[0]-1][1],45,45)
        circle(white, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
    elif msg=='eatr':
        boared_arr[n[1]][n[0]]=1
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]-1][i[0]+1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]-1][i[0]+1][0],sqr_arr[i[1]-1][i[0]+1][1],45,45)
        circle(white, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)
    elif msg=='eatld':
        boared_arr[n[1]][n[0]]=1
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]+1][i[0]-1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]+1][i[0]-1][0],sqr_arr[i[1]+1][n[0]-1][1],45,45)
        circle(white, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)    
    elif msg=='eatrd':
        boared_arr[n[1]][n[0]]=1
        boared_arr[i[1]][i[0]]=0
        boared_arr[i[1]+1][i[0]+1]=0
        sqrt(black, sqr_arr[i[1]][i[0]][0],sqr_arr[i[1]][i[0]][1],45,45)
        sqrt(black, sqr_arr[i[1]+1][i[0]+1][0],sqr_arr[i[1]+1][i[0]+1][1],45,45)
        circle(white, piece_arr[n[1]][n[0]][0], piece_arr[n[1]][n[0]][1], 20, 0)   

def boared_checkers():
    '''
    draws the boared on the screen
    '''
    x=300
    y=50
    for i in range(4):
        for j in range(4):
            sqrt(red, x, y, 45, 45)
            sqrt(black,x,y+45,45,45)
            y+=90
        x+=90
        y=50
    x=345
    y=50
    for i in range(4):
        for j in range(4):
            sqrt(red, x, y+45, 45, 45)
            sqrt(black,x,y,45,45)
            y+=90
        x+=90
        y=50
    for i in range(len(white_arr)):
        circle(blue, blue_arr[i][0], blue_arr[i][1], 20, 0)
        circle(white, white_arr[i][0], white_arr[i][1], 20, 0)
        
def sqrt(color,x,y,z,k,w=0):
    '''
    creates a sqr on the screen
    '''
    pygame.draw.rect(gameDisplay, color, (x,y,z,k),w)
            
def connect_four():
    '''
    activates the connect four window
    '''
    mouse = pygame.mouse.get_pos()
    turn=random.randint(1,2)
    gameDisplay.fill(black)
    gameDisplay.blit(img,(0,0))
    while True:
        boared_connect_four()
        button(gameDisplay, 70, 470, 70, 50, "menu", "menu")
        text_settings(gameDisplay, 100, 50, 100, 100, "player 1", white, 20)
        text_settings(gameDisplay, 100, 70, 100, 100, "vs", white, 20)
        text_settings(gameDisplay, 100, 90, 100, 100, "player 2", white, 20)
        text_settings(gameDisplay, 100, 120, 100, 100, "good luck!!!", white, 20)
        text_settings(gameDisplay, 100, 200, 100, 100, "turn:", white, 20)
        circle(black, 210, 98, 10, 10)
        circle(red, 210, 137, 10, 10)
        if turn==2:
            circle(black, 150, 300, 30, 30)
        else:
            circle(red, 150, 300, 30, 30) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    turn=set_circle(turn)
                 
        if win()==1:
            game_over(1)
        elif win()==2:
            game_over(2)
        if full()==True:
            game_over(0)
        update_game()
        clock.tick(60)

def full():
    '''
    checks if the boared is full
    '''
    for i in range(len(colorArr)):
        if colorArr[i]==0:
            return False
    return True
    
def game_over(num):
    '''
    activates the game over window
    '''
    gameDisplay.fill(black)
    gameDisplay.blit(img,(0,0))
    reset()
    while True:
        button(gameDisplay, 200, 300, 90, 50, "menu", "menu")
        button(gameDisplay, 450, 300, 230, 50, "play again", "connect four")
        if num==1:
            text_settings(gameDisplay, 350, 100, 100, 100, "player 1 is the winner!!!", white, 50)
        elif num==2:
            text_settings(gameDisplay, 350, 100, 100, 100, "player 2 is the winner!!!", white, 50)
        elif num==0:
            text_settings(gameDisplay, 350, 100, 100, 100, "its a draw!!!", white, 50) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
        update_game()
        clock.tick(60)
        
def reset():
    '''
    reset the boared
    '''
    for i in range(len(colorArr)):
        colorArr[i]=0
            
def win():
    '''
    checks if there is a winner and returns the number of the winner if no winner returns -1
    '''
    if win_one():
        return 1
    elif win_two():
        return 2
    else:
        return -1

def win_one():
    '''
    checks if player one is the winner returns true if he wins else return false
    '''
    for i in range(len(winningHorizontalCombos)):
        moves=winningHorizontalCombos[i]
        if colorArr[moves[0]]== 1 and colorArr[moves[1]]== 1 and colorArr[moves[2]]== 1 and colorArr[moves[3]]== 1:
            return True
    for i in range(len(winningDiagonalCombos)):
        moves=winningDiagonalCombos[i]
        if colorArr[moves[0]]== 1 and colorArr[moves[1]]== 1 and colorArr[moves[2]]== 1 and colorArr[moves[3]]== 1:
            return True
    for i in range(len(winningVerticalCombos)):
        moves=winningVerticalCombos[i]
        if colorArr[moves[0]]== 1 and colorArr[moves[1]]== 1 and colorArr[moves[2]]== 1 and colorArr[moves[3]]== 1:
            return True
    return False

def win_two():
    '''
    checks if player two is the winner returns true if he wins else return false
    '''
    for i in range(24):
        moves=winningHorizontalCombos[i]
        if colorArr[moves[0]]== 2 and colorArr[moves[1]]== 2 and colorArr[moves[2]]== 2 and colorArr[moves[3]]== 2:
            return True
    for i in range(24):
        moves=winningDiagonalCombos[i]
        if colorArr[moves[0]]== 2 and colorArr[moves[1]]== 2 and colorArr[moves[2]]== 2 and colorArr[moves[3]]== 2:
            return True
    for i in range(21):
        moves=winningVerticalCombos[i]
        if colorArr[moves[0]]== 2 and colorArr[moves[1]]== 2 and colorArr[moves[2]]== 2 and colorArr[moves[3]]== 2:
            return True
    return False

def change(turn):
    '''
    changes the turn between the players
    '''
    if turn==1:
        return 2
    return 1
        
def clicked_circle(mouse):
    '''
    checks if clicked circle is correct
    '''
    for k in range(len(range_x)-1):
        if range_x[k]<mouse[0]<range_x[k+1] and range_y[0]<mouse[1]<range_y[len(range_y)-1]:
            return (k,k+1)
    return (-1,0)
        
            
def set_circle(turn):
    '''
    set the circle on the boared if checks out and returns the turn of the player
    '''
    check=False
    mouse = pygame.mouse.get_pos()
    i = place(mouse)
    a=get_index(i)
    if i!=-1:
        if turn==1:
            check=player_one(a)
        else:
            check=player_two(a)
        if check:
            return change(turn)
    return turn

def place(mouse):
    '''
    checks if the clicked circle is avilable return the correct index if it is correct else returns -1
    '''
    k=clicked_circle(mouse)
    for i in range(42):
        if k[0]!=-1:
            for j in range(len(range_y)-1):
                if range_x[k[0]]< posArr[i][0] < range_x[k[1]] and range_y[j]<posArr[i][1]<range_y[j+1]:
                    return i
        else:
            break
    return -1    
def get_index(i):
    '''
    returns the correct index 
    '''
    if i<7:
        return i
    elif 7<i<14:
        return i-7
    elif 14<i<21:
        return i-14
    elif 21<i<28:
        return i-21
    elif 28<i<35:
        return i-28
    elif 35<i<42:
        return i-35
    return -1
    
def player_one(i):
    '''
    sets a circle for player 1 in the correct place on the boared with the given index return true if succesful else returns false
    '''
    if colorArr[i+35]==0:
        colorArr[i+35]=1;
        circle(red,posArr[i+35][0],posArr[i+35][1],25,25)
        return True
    elif colorArr[i+28]==0:
        colorArr[i+28]=1;
        circle(red,posArr[i+28][0],posArr[i+28][1],25,25)
        return True
    elif colorArr[i+21]==0:
        colorArr[i+21]=1;
        circle(red,posArr[i+21][0],posArr[i+21][1],25,25)
        return True
    elif colorArr[i+14]==0:
        colorArr[i+14]=1;
        circle(red,posArr[i+14][0],posArr[i+14][1],25,25)
        return True
    elif colorArr[i+7]==0:
        colorArr[i+7]=1;
        circle(red,posArr[i+7][0],posArr[i+7][1],25,25)
        return True
    elif colorArr[i]==0:
        colorArr[i]=1;
        circle(red,posArr[i][0],posArr[i][1],25,25)
        return True
    return False
            
def player_two(i):
    '''
    sets a circle for player 2 in the correct place on the boared with the given index return true if succesful else returns false
    '''
    if colorArr[i+35]==0:
        colorArr[i+35]=2;
        circle(black,posArr[i+35][0],posArr[i+35][1],25,25)
        return True
    elif colorArr[i+28]==0:
        colorArr[i+28]=2;
        circle(black,posArr[i+28][0],posArr[i+28][1],25,25)
        return True
    elif colorArr[i+21]==0:
        colorArr[i+21]=2;
        circle(black,posArr[i+21][0],posArr[i+21][1],25,25)
        return True
    elif colorArr[i+14]==0:
        colorArr[i+14]=2;
        circle(black,posArr[i+14][0],posArr[i+14][1],25,25)
        return True
    elif colorArr[i+7]==0:
        colorArr[i+7]=2;
        circle(black,posArr[i+7][0],posArr[i+7][1],25,25)
        return True
    elif colorArr[i]==0:
        colorArr[i]=2;
        circle(black,posArr[i][0],posArr[i][1],25,25)
        return True
    return False
    
def circle(color,x,y,r,w):
    '''
    creates a circle on the screen
    '''   
    pygame.draw.circle(gameDisplay,color,(x,y), r, w)
     
def boared_connect_four():
    '''
    creates the boared of the connect four game in the screen
    '''
    n=0
    m=0
    i=300
    j=100
    pygame.draw.rect(gameDisplay, white, (265,67,490,415), 5)
    while n<7:
        while m<6:
            circle(white,i,j,30,5)
            j+=70
            m+=1
        i+=70
        n+=1
        j=100
        m=0 
def instructions():
    '''
    activates the instructions window
    '''
    gameDisplay.fill(white)
    gameDisplay.blit(img,(0,0))
    largeText = pygame.font.Font("chawp.ttf",80)
    textSurf,textReact=text_objects("instructions",largeText,white)
    textReact.center=((display_width/2),(display_height/5))
    gameDisplay.blit(textSurf,textReact)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
        button(gameDisplay, 150, 200, 500, 50, "checkers instructions", "checkers_instructions")
        button(gameDisplay, 100, 300, 600, 50, "connect four instructions", "connect_four_instructions")
        update_game()
        clock.tick(60)
      
def checkers_instructions():
    '''
    activates the checkers instructions window
    '''
    gameDisplay.fill(white)
    gameDisplay.blit(img,(0,0))
    largeText = pygame.font.Font("chawp.ttf",50)
    textSurf,textReact=text_objects("checkers instructions",largeText,white)
    textReact.center=((display_width/2),(display_height/5))
    gameDisplay.blit(textSurf,textReact)
    rules=("checkers is played by two opponents, on opposite sides of the gameboard. ",
           " One player has the dark pieces the other has the light pieces.",
           " Players alternate turns. A player may not move an opponents piece. ",
           "A move consists of moving a piece diagonally to an adjacent unoccupied square. ",
           "If the adjacent square contains an opponents piece,and the square immediately " ,
           "beyond it is vacant, the piece may be captured (and removed from the game)",
           "by jumping over it. Only the dark squares of the checkered board are used.",
           " A piece may move only diagonally into an unoccupied square.",
           " Capturing is mandatory in most official rules, although  ",
           "some rule variations make capturing optional when presented. ",
          "In almost all variants, the player without pieces remaining,",
          " or who cannot move due to being blocked, loses the game." )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
        button(gameDisplay, 400, 500, 100, 50, "menu", "menu",30)
        button(gameDisplay, 530, 500, 220, 50, "instructions", "instructions",30)
        text_settings(gameDisplay, 200, 50, 400, 300, rules[0], white, 15)
        text_settings(gameDisplay, 160, 70, 400, 300, rules[1], white, 15)
        text_settings(gameDisplay, 175, 90, 400, 300, rules[2], white, 15)
        text_settings(gameDisplay, 200, 110, 400, 300, rules[3], white, 15)
        text_settings(gameDisplay, 200, 130, 400, 300, rules[4], white, 15)
        text_settings(gameDisplay, 180, 150, 400, 300, rules[5], white, 15)
        text_settings(gameDisplay, 180, 170, 400, 300, rules[6], white, 15)
        text_settings(gameDisplay, 180, 190, 400, 300, rules[7], white, 15)
        text_settings(gameDisplay, 180, 210, 400, 300, rules[8], white, 15)
        text_settings(gameDisplay, 180, 230, 400, 300, rules[9], white, 15)
        text_settings(gameDisplay, 180, 250, 400, 300, rules[10], white, 15)
        text_settings(gameDisplay, 180, 270, 400, 300, rules[11], white, 15)
        update_game()
        clock.tick(60)
        
def connect_four_instructions():
    '''
    activates the connect four instructions window 
    '''
    gameDisplay.fill(white)
    gameDisplay.blit(img,(0,0))
    largeText = pygame.font.Font("chawp.ttf",45)
    textSurf,textReact=text_objects("connect four instructions",largeText,white)
    textReact.center=((display_width/2),(display_height/5))
    gameDisplay.blit(textSurf,textReact)
    rules=("To win Connect Four you must be the first player to get ",
           "four of your colored checkers in a row .",
           "either horizontally, vertically or diagonally")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate_game()
        button(gameDisplay, 400, 500, 100, 50, "menu", "menu",30)
        button(gameDisplay, 530, 500, 220, 50, "instructions", "instructions",30)
        text_settings(gameDisplay, 200, 50, 400, 300, rules[0], white, 20)
        text_settings(gameDisplay, 110, 80, 400, 300, rules[1], white, 20)
        text_settings(gameDisplay, 140, 110, 400, 300, rules[2], white, 20)
        update_game()
        clock.tick(60)
      
      
def update_game():
    '''
    updates the game
    '''
    pygame.display.update() 
    
def terminate_game():
    '''
    terminates the game
    '''
    pygame.quit()
    quit()
    
game_intro()                        
terminate_game()
'''       
if __name__=='__game__':
    game_intro()                        
    terminate_game()
'''                   