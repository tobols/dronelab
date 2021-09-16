from djitellopy import Tello
from time import sleep

def runDrone():
    tello = Tello()
    tello.connect()
    print(tello.get_battery())

    tello.takeoff()
    tello.send_rc_control(0, 30, 0, 50)
    sleep(2)
    tello.send_rc_control(0, 0, 0, 0)

    tello.land()


class main:
    def __init__(self):
        runDrone()


if __name__ == '__main__':
    m = main()
