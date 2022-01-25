import random
import time
from turtle import  Turtle
class PingPongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.DrawBallMethods = [self.shape, self.fillcolor, self.penup, self.goto, self.speed, self.seth]
        self.DrawBallParameters = ["circle", "white", "", self.GenerateRandomXYCordinates(), 0, 35]

        self.RefreshPingPongBall()

    def RefreshPingPongBall(self):
        for _ in range(len(self.DrawBallMethods)):
            if self.DrawBallParameters[_] =="":
                self.DrawBallMethods[_]()
            else:
                self.DrawBallMethods[_](self.DrawBallParameters[_])
        self.MovePingPongBall("Forward")

    def GenerateRandomXYCordinates(self):
        return (random.randint(-60, 100), random.randint(-60, 0))

    def MovePingPongBall(self, Direction):
        if Direction == "Forward":
            self.forward(4)
        else:
            self.backward(4)
