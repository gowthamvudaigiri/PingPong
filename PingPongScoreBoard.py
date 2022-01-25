from turtle import Turtle
class PingPongScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ComputerScore =-1
        self.PlayerScore =-1
        self.DrawScoreBoardMethods = [self.reset, self.pencolor, self.penup, self.goto, self.write, self.goto, self.write,
                                      self.ht]

        self.DrawScoreBoardParameters = ["", "white", "", (-200, 300), [str(self.ComputerScore), ('Arial', 72, 'bold')],
                                         (200, 300), [str(self.PlayerScore), ('Arial', 72, 'bold')], ""]

        self.RefreshScoreBoard(1,1)

    def RefreshScoreBoard(self, IncrementComputerScore, IncrementPlayerScore):

        self.ComputerScore += IncrementComputerScore
        self.PlayerScore+=IncrementPlayerScore

        self.DrawScoreBoardParameters[4][0]= str(self.ComputerScore)
        self.DrawScoreBoardParameters[6][0] = str(self.PlayerScore)

        for _ in range(len(self.DrawScoreBoardMethods)):
            if self.DrawScoreBoardParameters[_] == "":
                self.DrawScoreBoardMethods[_]()
            elif self.DrawScoreBoardMethods[_] == self.write:
                self.write(self.DrawScoreBoardParameters[_][0], font=self.DrawScoreBoardParameters[_][1])
            else:
                self.DrawScoreBoardMethods[_](self.DrawScoreBoardParameters[_])

