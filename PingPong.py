import random
import time
from turtle import Screen

from PingPongBall import PingPongBall
from PingPongNet import PingPongNet
from PingPongScoreBoard import PingPongScoreBoard
from PingPongPaddle import PingPongPaddle

class PingPong():
    def __init__(self):
        self.PingPongBoard = Screen()
        self.PingPongBoard.screensize(940, 800 , "black")
        self.DrawGameObjects()
        self.StartMovingComputerPaddle= False
        self.BallDirection = "Forward"
        self.RandomComputerPaddlePosition = random.randint(0,4)
        self.AccurateHits =0
        self.RandomAccurateHits =random.randint(1,5)
        self.RandomYcor =0

    def DrawGameObjects(self):
        PingPongGameObject = PingPongNet()
        self.PingPongScoreBoardObject = PingPongScoreBoard()
        self.PingPongPaddleObject = PingPongPaddle()
        self.PingPongBoard.onkey(self.MoveUp, "Up")
        self.PingPongBoard.onkey(self.MoveDown, "Down")
        self.PingPongBoard.listen()
        self.PingPongBallObject =PingPongBall()


    def MoveUp(self):
        self.PingPongPaddleObject.MovePLayerPaddleUp("Player")

    def MoveDown(self):
        self.PingPongPaddleObject.MovePLayerPaddleDown("Player")

    def MoveBall(self, Direction):
        self.PingPongBallObject.MovePingPongBall(Direction)

    def MoveComputerPaddle(self):
        if self.AccurateHits > self.RandomAccurateHits:
            BallYCor = self.PingPongBallObject.ycor()+ 100
        else:
            BallYCor = self.PingPongBallObject.ycor()
        self.PingPongPaddleObject.MoveComputerPaddle(int(BallYCor), self.RandomComputerPaddlePosition)

    def CalculatePaddleToBallDistance(self):
        for PaddleType in self.PingPongPaddleObject.Paddle :
            for _ in range (5):
                if self.PingPongPaddleObject.Paddle[PaddleType][_].distance(self.PingPongBallObject) <=15 :
                    self.PingPongBallObject.seth(self.PingPongPaddleObject.SetBallAngle[_])
                    if PaddleType == "Player":
                        self.StartMovingComputerPaddle = True
                        self.RandomComputerPaddlePosition = random.randint(0, 4)
                        if self.AccurateHits > self.RandomAccurateHits :
                            self.RandomYcor = random.randint(-400, 400)
                    else:
                        self.StartMovingComputerPaddle = False
                        self.AccurateHits +=1

                    if PaddleType == "Player":
                        self.BallDirection = "Forward"
                    else:
                        self.BallDirection = "Backward"

    def CalculateBallToBoundaryDistance(self):
        if self.PingPongBallObject.xcor() >= 470 or self.PingPongBallObject.xcor() <= -470 :
            if self.PingPongBallObject.xcor() >= 470:
                self.PingPongScoreBoardObject.RefreshScoreBoard(1,0)
            else :
                self.PingPongScoreBoardObject.RefreshScoreBoard(0,1)
            self.PingPongBallObject.RefreshPingPongBall()
            self.PingPongPaddleObject.RestetPaddle()
            self.StartMovingComputerPaddle = False
            self.BallDirection = "Forward"
            self.AccurateHits =0
            self.RandomAccurateHits = random.randint(1, 5)
            time.sleep(1)

        if self.PingPongBallObject.ycor() >= 400 :
            if self.BallDirection =="Forward":
                self.PingPongBallObject.seth(random.randint(220,240))
            else:
                self.PingPongBallObject.seth(random.randint(100,120))

        if  self.PingPongBallObject.ycor() <= -400 :
            if self.BallDirection =="Forward":
                self.PingPongBallObject.seth(random.randint(100,120))
            else:
                self.PingPongBallObject.seth(random.randint(220, 240))





