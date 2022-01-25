import random
from turtle import Turtle
from math import ceil
import time
class PingPongPaddle:
    def __init__(self):
        self.Paddle ={"Computer":list(), "Player":list()}
        self.PaddleColors = {"Computer": "red", "Player" :"blue"}
        self.PaddleCoordinates ={"Computer":(-400, -40), "Player" :(400, -40)}
        self.SetBallAngle = [240, 210, 180, 150, 120]
        for PaddleType in self.Paddle:
            for _ in range(5):
                self.Paddle[PaddleType].append(Turtle("square"))
                self.Paddle[PaddleType][_].shapesize(1,.75,5)
                self.Paddle[PaddleType][_].color(self.PaddleColors[PaddleType])
                self.Paddle[PaddleType][_].penup()
                self.Paddle[PaddleType][_].goto(self.PaddleCoordinates[PaddleType][0],
                                                self.PaddleCoordinates[PaddleType][1] +(_*20))
        self.Paddle["Player"][4].seth(90)
        self.Paddle["Player"][0].seth(270)
        self.Paddle["Computer"][4].seth(90)
        self.Paddle["Computer"][0].seth(270)

    def RestetPaddle(self):
        for PaddleType in self.Paddle:
            for _ in range(5):
                self.Paddle[PaddleType][_].goto(self.PaddleCoordinates[PaddleType][0],
                                                self.PaddleCoordinates[PaddleType][1] + (_ * 20))
    def MovePLayerPaddleUp(self, PaddleType):
        if  self.Paddle[PaddleType][4].ycor() <= 380:
            for _ in range(0,4):
                self.Paddle[PaddleType][_].goto(self.Paddle[PaddleType][_+1].xcor(), self.Paddle[PaddleType][_+1].ycor())
            self.Paddle[PaddleType][4].forward(20)

    def MovePLayerPaddleDown(self, PaddleType):
        if self.Paddle[PaddleType][0].ycor() >= -380:
            for _ in range(4,0, -1):
                self.Paddle[PaddleType][_].goto(self.Paddle[PaddleType][_-1].xcor(), self.Paddle[PaddleType][_-1].ycor())
            self.Paddle[PaddleType][0].forward(20)

    def MoveComputerPaddle(self, BallYCor):
        RandPixels = [0,20,40,60,80,100, 120, 140, -20,40,-60,-80,-100,-120,-140]
        RandDistance =int(float(BallYCor/20)) * 20 #+ int(random.choice(RandPixels))
        if self.Paddle["Computer"][0].ycor() > BallYCor:
            #while self.Paddle["Computer"][0].ycor() > RandDistance:
                self.MovePLayerPaddleDown("Computer")
        if self.Paddle["Computer"][4].ycor() < BallYCor:
            #while self.Paddle["Computer"][4].ycor() < RandDistance:
                self.MovePLayerPaddleUp("Computer")



