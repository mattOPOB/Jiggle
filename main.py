import win32api
import pyautogui

state = win32api.GetKeyState(0x10)

def move():
    # While SHIFT KEY not pressed
    while win32api.GetAsyncKeyState(0x10) == 0:
        pyautogui.moveTo(600, 100, duration=0.001)
        pyautogui.moveTo(105, 105, duration=0.001)

    #When SHIFT KEY pressed
    print("■                                       ■")
    print("■■■■■■■ THANK YOU FOR JIGGLING! ■■■■■■■■■")
    main()


def main():

    print("\n■■■■■■■■■■■ WELCOME TO JIGGLE ■■■■■■■■■■■")
    print("■            Start to jiggle            ■")
    print("■                                       ■")
    start()


def start():
    user_input = input("■       Please enter 'x' to start:  ")

    if user_input == "x" or "X":
        print("■        Press 'SHIFT KEY' to stop" + "      ■")
        move()

    elif user_input != "x" or "X":
        print("Not a valid input, please enter 'x' to start")
        start()


if __name__ == "__main__":
    main()