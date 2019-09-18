import pygame, sys
from pygame.locals import*
import random


WINDOWWIDTH = 800
WINDOWHEIGHT = 400
mainClock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AI_Game_Wins = 0
Player_Game_Wins = 0
AI_score = 0
Player_score = 0
ball_pos = [0,0]
ball_vel = [0,0]
BALL_RADIUS = 5
horz = 0
vert = 0
Player_points = 11
Ai_points = 11
points_Needed_Win = 11

def terminate():
    pygame.quit()
    sys.exit()


def  waitForPlayerInput():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


# function that creates the ball and sets its initial speed
def ball_create(right):
    global ball_pos, ball_vel, horz, vert

    ball_pos = [WINDOWWIDTH // 2, random.randrange(100, 400, 100)]
    horz = random.randrange(2,5)
    vert = random.randrange(-5,5)

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]

# set up the pygame and the window

pygame.init()
fps = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pong No Walls')
pygame.mouse.set_visible(False)
font1 = pygame.font.SysFont("Times New Roman", 20)
paddleImg = pygame.image.load('Blue_rectangle.png')
paddleImgRedraw = pygame.transform.scale(paddleImg, (8, 100))
paddleImgRedraw2 = pygame.transform.scale(paddleImg, (100, 8))
# set up the sounds
pongSound = pygame.mixer.Sound('pongPop2.wav')
pygame.mixer.music.load('bensound-happyrock.mp3')
AI_point = pygame.mixer.Sound('AIScore.wav')
Player_point = pygame.mixer.Sound('goalScore.wav')
winner_Round_AI = pygame.mixer.Sound('winnerAI.wav')
winner_Round_Player = pygame.mixer.Sound('winnerPlayer.wav')


paddle1Pos = [4, WINDOWHEIGHT // 2]
paddle2Pos = [0, 0]
paddle3Pos = [0, 395]
paddle4Pos = [786, WINDOWHEIGHT // 2]
paddle5Pos = [700, 1]
paddle6Pos = [700, 395]


paddle1 = pygame.Rect(0, WINDOWHEIGHT // 2, 8, 100)
paddle2 = pygame.Rect(0, 1, 100, 8)
paddle3 = pygame.Rect(0, 390, 100, 8)
paddle4 = pygame.Rect(790, WINDOWHEIGHT // 2, 8, 100)
paddle5 = pygame.Rect(700, 1, 100, 8)
paddle6 = pygame.Rect(700, 390, 100, 8)
ball = pygame.draw.circle(windowSurface, BLACK, (WINDOWWIDTH // 2, WINDOWHEIGHT // 2), 10)

MOVESPEED = 5

# starting the game loop
while True:


    if random.randrange(0, 2) == 0:
        ball_create(True)
    else:
        ball_create(False)

    moveLeft = moveRight = moveUp = moveDown = 0
    pygame.draw.rect(windowSurface, WHITE, (200, 150, 100, 50))

    while True:


        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

        if moveDown and paddle1.bottom < WINDOWHEIGHT:
            paddle1.top += MOVESPEED
            paddle1Pos[1] += MOVESPEED
        if moveUp and paddle1.top > 0:
            paddle1.top -= MOVESPEED
            paddle1Pos[1] -= MOVESPEED
        if moveLeft and paddle2.left > 0 and paddle3.left > 0:
            paddle3.left -= MOVESPEED
            paddle2.left -= MOVESPEED
            paddle2Pos[0] -= MOVESPEED
            paddle3Pos[0] -= MOVESPEED
        if moveRight and paddle2.right < WINDOWWIDTH // 2 and paddle3.right < WINDOWWIDTH // 2:
            paddle3.right += MOVESPEED
            paddle2.right += MOVESPEED
            paddle2Pos[0] += MOVESPEED
            paddle3Pos[0] += MOVESPEED

        ball_pos[0] += int(ball_vel[0])
        ball_pos[1] += int(ball_vel[1])




        windowSurface.fill(BLACK)

        pygame.draw.line(windowSurface, WHITE, [WINDOWWIDTH // 2, 50], [WINDOWWIDTH // 2, 100], 1)
        pygame.draw.line(windowSurface, WHITE, [WINDOWWIDTH // 2, 150], [WINDOWWIDTH // 2, 200], 1)
        pygame.draw.line(windowSurface, WHITE, [WINDOWWIDTH // 2, 250], [WINDOWWIDTH // 2, 300], 1)
        pygame.draw.line(windowSurface, WHITE, [WINDOWWIDTH // 2, 350], [WINDOWWIDTH // 2, 400], 1)
        pygame.draw.rect(windowSurface, WHITE, paddle1)
        pygame.draw.rect(windowSurface, WHITE, paddle2)
        pygame.draw.rect(windowSurface, WHITE, paddle3)
        pygame.draw.rect(windowSurface, WHITE, paddle4)
        pygame.draw.rect(windowSurface, WHITE, paddle5)
        pygame.draw.rect(windowSurface, WHITE, paddle6)
        pygame.draw.circle(windowSurface, WHITE, ball_pos, 10)

        #displays the scores on the screen
        score1 = font1.render("Player Score " + str(Player_score), 1, WHITE)
        windowSurface.blit(score1, (50, 20))

        score3 = font1.render("Player Games Won " + str(Player_Game_Wins), 1, WHITE)
        windowSurface.blit(score3, (50, 40))

        score2 = font1.render("AI Score " + str(AI_score), 1, WHITE)
        windowSurface.blit(score2, (600, 20))

        score4 = font1.render("AI Games Won " + str(AI_Game_Wins), 1, WHITE)
        windowSurface.blit(score4, (600, 40))

        score5 = font1.render("Points needed to win " + str(Player_points), 1, WHITE)
        windowSurface.blit(score5, (50, 60))

        score6 = font1.render("Points needed to win " + str(Ai_points), 1, WHITE)
        windowSurface.blit(score6, (600, 60))

        paddle4Pos[1] = ball_pos[1]
        paddle5Pos[0] = ball_pos[0]
        paddle6Pos[0] = ball_pos[0]
        windowSurface.blit(paddleImgRedraw, paddle1)
        windowSurface.blit(paddleImgRedraw, paddle4)
        windowSurface.blit(paddleImgRedraw2, paddle2)
        windowSurface.blit(paddleImgRedraw2, paddle3)
        windowSurface.blit(paddleImgRedraw2, paddle5)
        windowSurface.blit(paddleImgRedraw2, paddle6)

        # Ai tracking the ball
        if int(paddle4Pos[1]) >= 0 and int(paddle4Pos[1]) <= WINDOWHEIGHT:
            paddle4.centery = ball_pos[1]

        if int(paddle5Pos[0]) >= WINDOWWIDTH // 2 + 50:
            paddle5.centerx = ball_pos[0]
            paddle6.centerx = ball_pos[0]

        #paddle1
        if int(ball_pos[0]) <= BALL_RADIUS + 10 and int(ball_pos[1]) in range(paddle1Pos[1] , paddle1Pos[1] + 100, 1):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()

        #paddle 4
        if int(ball_pos[0]) >= 777 and int(ball_pos[1]) in range(paddle4Pos[1], paddle4Pos[1] + 100, 1):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()
        #paddle 2
        if int(ball_pos[1]) <= BALL_RADIUS + 10 and int(ball_pos[0]) in range(paddle2.left, paddle2.right, 1):
            ball_vel[1] = -ball_vel[1]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()
        #paddle 3
        if int(ball_pos[1]) >= WINDOWHEIGHT - BALL_RADIUS - 10 and int(ball_pos[0]) in range(paddle3.left, paddle3.right, 1):
            ball_vel[1] = -ball_vel[1]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()
        #paddle 5
        if int(ball_pos[1]) <= 10 and int(ball_pos[0]) in range(paddle5.left, paddle5.right, 1):
            ball_vel[1] = -ball_vel[1]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()
        #paddle 6
        if int(ball_pos[1]) >= 384 and int(ball_pos[0]) in range(paddle6.left, paddle6.right, 1):
            ball_vel[1] = -ball_vel[1]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            pongSound.play()

        # scoring the balls
        if int(ball_pos[1]) < 0:
            if int(ball_pos[0]) >= WINDOWWIDTH // 2:
                Player_score = Player_score + 1
                Playerpoints = points_Needed_Win - Player_score
                Player_point.play()
                break
            else:
                AI_score = AI_score + 1
                Ai_points = points_Needed_Win - AI_score
                AI_point.play()
                break

        if int(ball_pos[1]) >= WINDOWHEIGHT + BALL_RADIUS:
            if int(ball_pos[0]) >= WINDOWWIDTH // 2:
                Player_score = Player_score + 1
                Player_points = points_Needed_Win - Player_score
                Player_point.play()
                break
            else:
                AI_score = AI_score + 1
                Ai_points = points_Needed_Win - AI_score
                AI_point.play()
                break

        if int(ball_pos[0]) > WINDOWWIDTH + BALL_RADIUS:
            Player_score = Player_score +1
            Player_point.play()
            Player_points = points_Needed_Win - Player_score
            break
        if int(ball_pos[0]) < 0 - BALL_RADIUS:
            AI_score = AI_score + 1
            AI_point.play()
            Ai_points = points_Needed_Win - AI_score
            break

        pygame.display.update()
        mainClock.tick(60)


    # Adds to the game score and resets game if one either Ai or Player is the best out of five
    if AI_score >= 11 and AI_score > Player_score - 2:
        AI_Game_Wins += 1
        AI_score = 0
        Player_score = 0
        Ai_points = 11
        Player_points = 11
        winner_Round_AI.play()
        if AI_Game_Wins == 3:
            pygame.mixer.music.play(-1, 0.0)
            gameOver1 = font1.render("Game Over: AI WINS  Press Button to play Again ", 1, WHITE)
            windowSurface.blit(gameOver1, (200, 150))
            pygame.display.update()
            waitForPlayerInput()
            pygame.mixer.music.stop()
            AI_Game_Wins = 0
            Player_Game_Wins = 0
    if Player_score >= 11 and Player_score > AI_score - 2:
        AI_score = 0
        Player_score = 0
        Player_Game_Wins += 1
        Aipoints = 11
        Playerpoints = 11
        winner_Round_Player.play()
        if Player_Game_Wins == 3:
            pygame.mixer.music.play(-1, 0.0)
            gameOver2 = font1.render("Game Over: Player WINS Press Button to play Again ", 1, WHITE)
            windowSurface.blit(gameOver2, (200, 150))
            pygame.display.update()
            waitForPlayerInput()
            pygame.mixer.music.stop()
            AI_Game_Wins = 0
            Player_Game_Wins = 0

    pygame.display.update()


