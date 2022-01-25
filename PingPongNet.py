from turtle import Turtle
class PingPongNet (Turtle):
    def __init__(self):
        super().__init__()
        self.DrawNetMethods =[self.width, self.pencolor, self.penup, self.goto, self.pendown, self.seth, self.forward,
                              self.ht]
        self.DrawNetParameters = [5, "white", "", (0, 400) , "", 270, 800, "" ]
        self.DrawNet()

    def DrawNet(self):
        for _ in range(len(self.DrawNetMethods)):
            if self.DrawNetParameters[_] =="":
                self.DrawNetMethods[_]()
            else:
                self.DrawNetMethods[_](self.DrawNetParameters[_])