import urx
from time import sleep
from robot_controls import robot_positions
from robot_vision import vision
from robot_brain import weighted_table

#rob = urx.Robot("141.252.128.7")
#print("Connected")

sleep(0.2)  #leave some time to robot to process the setup commands

positions = robot_positions.positions("D:/Documents/Minors/Robotarm/Programs/2048/robot_controls/positions.txt")

board = None

def main():
    #rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)
    vision.init()
    direction = None
    while (direction != -1):
        direction = getDirection()
        #doMove(direction)
    #rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)
    # loop
    #doMove(getDirection())
    # wait until robot has moved and repeat

    #done
    vision.releaseCamera()

def doMove(direction):

    #go to center of screen and do move
    rob.movel(positions.get("center"), wait=True, vel=0.7, acc=1.1)
    if direction == 0:
        rob.movel(positions.get("left"), wait=True, vel=0.7, acc=1.1)
    elif direction == 1:
        rob.movel(positions.get("up"), wait=True, vel=0.7, acc=1.1)
    elif direction == 2:
        rob.movel(positions.get("right"), wait=True, vel=0.7, acc=1.1)
    elif direction == 3:
        rob.movel(positions.get("down"), wait=True, vel=0.7, acc=1.1)
    #move back to start
    rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)

def getDirection():
    last_board = board
    board = vision.updateBoard()
    while (last_board == board):
        print("Waiting for board change...")
        sleep(1)
        board = vision.updateBoard()
    print board
    return weighted_table.getMove(board, 4)
    # return ai.getMove(board)

#temporary
# rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)
# doMove(0)
# doMove(2)
# doMove(3)
# doMove(1)
# rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)
main()
print("Done")
