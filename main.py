import time

from PingPong import  PingPong
GameOn = True
PingPongGame = PingPong()

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
PingPongGame.PingPongBoard.mainloop()

