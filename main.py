import pygame
import time
import random
pygame.init()


dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake Game')

clock=pygame.time.Clock()
snakeBlock = 10
snakeSpeed = 15

fontStyle=pygame.font.SysFont(None,30)

def message(msg,color):
    mesg=fontStyle.render(msg,True,color)
    dis.blit(mesg,[dis_width/3,dis_height/3])

def gameLoop():
    game_over=False
    game_close=False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change =0
    y1_change = 0

    xFood= round(random.randrange(0,dis_width - snakeBlock)/10.0)*10.0
    yFood=round(random.randrange(0, dis_width - snakeBlock)/10.0)*10.0

    while not game_over:
        while game_close==True:
            dis.fill(grey)
            message("Game Over! Press X to Quit or R to Restart",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snakeBlock
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snakeBlock
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snakeBlock
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snakeBlock

        if x1 >= dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True

        x1+=x1_change
        y1+=y1_change
        dis.fill(grey)
        pygame.draw.rect(dis,black,[x1,y1,snakeBlock, snakeBlock])
        pygame.draw.rect(dis,brown,[xFood,yFood,snakeBlock,snakeBlock])
        pygame.display.update()
        clock.tick(snakeSpeed)

        if x1==xFood and y1==yFood:
            print("Yumm!")

    pygame.display.update()
    time.sleep(1)

    pygame.quit()
    quit()

gameLoop()