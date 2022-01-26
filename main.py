import time

from PingPong import  PingPong
GameOn = True
PingPongGame = PingPong()
GameScore =5
#PingPongGame.PingPongBoard.tracer(0)
PingPongGame.PingPongBoard.tracer(0)
while GameOn:
    time.sleep(0.01)
    PingPongGame.CalculateBallToBoundaryDistance()
    PingPongGame.CalculatePaddleToBallDistance()
    #print(PingPongGame.BallDirection)
    PingPongGame.PingPongBallObject.MovePingPongBall(PingPongGame.BallDirection)
    if PingPongGame.StartMovingComputerPaddle:
        PingPongGame.MoveComputerPaddle()
    PingPongGame.PingPongBoard.update()
    if PingPongGame.PingPongScoreBoardObject.ComputerScore ==GameScore or \
            PingPongGame.PingPongScoreBoardObject.PlayerScore ==GameScore:
        GameOn = False

if PingPongGame.PingPongScoreBoardObject.ComputerScore ==GameScore :
    PingPongGame.PingPongScoreBoardObject.PrintResult("You Lost")
else:
    PingPongGame.PingPongScoreBoardObject.PrintResult("You Won")
PingPongGame.PingPongBoard.mainloop()

