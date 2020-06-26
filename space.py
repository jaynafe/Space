import pygame
import sys


class Pony(object):
    # pony---定義類別
    def __init__(self):
        # 定義初始化
        self.ponyRect = pygame.Rect(65,50,50,50)
        self.ponyStatus = [ pygame.image.load("assets/1.png"),
                            pygame.image.load("assets/2.png"),
                            pygame.image.load("assets/dead.png"),]
        self.status = 0
        self.ponyX = 120
        self.ponyY = 350
        self.jump = False
        self.jumpSpeed = 15
        self.gravity = 1
        self.dead = False


    def ponyupdate(self):
    # 定義移動方法
        if self.jump :
            #跳躍狀態
           self.jumpSpeed -= 1
           self.ponyY -= self.jumpSpeed
        else :
           self.gravity += 0
           self.ponyY += self.gravity
        self.ponyRect[1] = self.ponyY


class Tube(object):
    # Tube---定義類別
    def __init__(self):
    # 定義初始化
        self.wallx = 400
        self.tubeUp = pygame.image.load("assets/top.png")
        self.tubeDown = pygame.image.load("assets/bottom.png")

    def UpdateTube(self):
    # 定義移動方法
        self.wallx -=5
        if self.wallx < -80 :
            global score
            score += 1
            self.wallx = 400

def createMap():
    #建立地圖
    screen.blit(background, (0, 0))
    #顯示Tube
    screen.blit(Tube.tubeUp,(Tube.wallx,-300))
    screen.blit(Tube.tubeDown,(Tube.wallx,500))
    Tube.UpdateTube()

    #顯示pony
    if Pony.dead :
        Pony.status = 2
    elif Pony.jump :
        Pony.status = 1

    screen.blit(Pony.ponyStatus[Pony.status] ,(Pony.ponyX , Pony.ponyY))
    Pony.ponyupdate()
    screen.blit(font.render('Score:' + str(score), -1 , (255,255,255)),(100,50))

    pygame.display.update()

def checkDead(): #檢測是否死亡
    upRect = pygame.Rect(Tube.wallx,-300,Tube.tubeUp.get_width(),Tube.tubeUp.get_height())
    downRect = pygame.Rect(Tube.wallx,500,Tube.tubeDown.get_width(),Tube.tubeDown.get_height())
    #檢測矩形碰撞
    if upRect.colliderect(Pony.ponyRect) or downRect.colliderect(Pony.ponyRect) :
        Pony.dead = True
    #邊界檢測
    if not 0 < Pony.ponyRect[1] < height :
        Pony.dead = True
        return True
    else :
        return False

def getResult():
    #獲取總分
    final_text1 = "Game Over"
    final_text2 = "Your final score is :" + str(score)
    ft1_font = pygame.font.SysFont("Arial",70)
    ft1_surf = font.render(final_text1,1,(242,3,36))
    ft2_font = pygame.font.SysFont("Arial",50)
    ft2_surf = font.render(final_text2,1,(2253,177,6))

    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.update()


if __name__ == '__main__':
    # 主程式
    pygame.init()

    pygame.font.init() #字體
    font = pygame.font.SysFont(None,50)

    size = width , height = 400,650 #視窗大小
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock() #遊戲速度
    color = (255,255,255)

    Pony = Pony()
    Tube = Tube()
    score = 0 #分數初始值為0
    
    while True:
        clock.tick(60) #每秒60次
        #取得按鍵壓下
        pressed = pygame.key.get_pressed()
        #迴圈
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #如果按W且玩家沒死
            if pressed[pygame.K_w] and not Pony.dead :
                #跳躍
                Pony.jump = True
                #重力值
                Pony.gravity = 1
                #跳躍速度
                Pony.jumpSpeed = 10
                #如果按A且玩家沒死
            if pressed[pygame.K_a] and not Pony.dead :
                #左移10
                Pony.ponyX -= 10
                #跳躍
                Pony.jump = True
                #重力
                Pony.gravity = 1
                #跳躍速度
                Pony.jumpSpeed = 10
                #如果按D且玩家沒死
            if pressed[pygame.K_d] and not Pony.dead :
                #右移10
                Pony.ponyX += 10
                #跳躍
                Pony.jump = True
                #重力
                Pony.gravity = 1
                #跳躍速度
                Pony.jumpSpeed = 10
                #如果按S且玩家沒死
            if pressed[pygame.K_s] and not Pony.dead :
                #下移10
                Pony.ponyY -= 10
                Pony.jump = True

        background = pygame.image.load("assets/background.png")
        if checkDead() :
            getResult()
        else :
            createMap()
        createMap()
    pygame.quit()