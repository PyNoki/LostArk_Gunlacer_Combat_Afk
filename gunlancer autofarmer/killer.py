from imports import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.end
pause_key = Key.backspace
exit_key = Key.backspace
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("Autofisher is running")
    print("- Controls:")
    print("\t end = Resume")
    print("\t backspace = Pause")
    print("\t backspace = Exit")
    print("-----------------------------------------------------")
    print('Press end to start ...')

def main():
    pot = 0
    repair = 0
    phase = 0
    shield = 0

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:

            if pot >= 15:
                pydirectinput.keyDown('6')
                pydirectinput.keyUp('6')
                pot = 0

            '''if repair >= 300:
                time.sleep(1)
                pydirectinput.keyDown('esc')
                pydirectinput.keyUp('esc')
                time.sleep(5)
                pydirectinput.moveTo(1265, 431)
                time.sleep(1)
                pyautogui.click()
                time.sleep(3)
                pydirectinput.moveTo(1255, 689)
                time.sleep(3)
                pyautogui.click()
                time.sleep(3)
                pydirectinput.moveTo(1087, 426)
                time.sleep(3)
                pyautogui.click()
                time.sleep(3)
                pydirectinput.keyDown('esc')
                pydirectinput.keyUp('esc')
                time.sleep(3)
                pydirectinput.keyDown('esc')
                pydirectinput.keyUp('esc')
                repair = 0'''


            if phase == 0:
                pydirectinput.moveTo(949, 534) # center
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(1043, 525) # middle right
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(1053, 430) #top right
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(954, 353) #top middle
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(853, 395) #left top
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(842, 487) #left middle
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(827, 566) #left bottom
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(958, 608) #bottom middle
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1

            if phase == 0:
                pydirectinput.moveTo(958, 545) #bottom right
                if pyautogui.locateOnScreen('enemybar.png'):
                    phase = 1
            
            if phase == 1:
                if pyautogui.locateOnScreen('shout.png') and phase == 1 and shield == 0:
                    pydirectinput.keyDown('a')
                    pydirectinput.keyUp('a')
                    time.sleep(2)
                    phase = 0

                if pyautogui.locateOnScreen('thunder.png') and phase == 1 and shield == 0:
                    pydirectinput.keyDown('d')
                    pydirectinput.keyUp('d')
                    time.sleep(2)
                    phase = 0

                if pyautogui.locateOnScreen('shout.png') == None and pyautogui.locateOnScreen('thunder.png') == None and shield == 0 and phase == 1:
                    pydirectinput.keyDown('z')
                    pydirectinput.keyUp('z')
                    time.sleep(0.6)
                    shield = 1

                if pyautogui.locateOnScreen('shout.png') and shield == 1 and phase == 1:
                    pydirectinput.keyDown('a')
                    pydirectinput.keyUp('a')
                    time.sleep(2)
                    pydirectinput.keyDown('z')
                    pydirectinput.keyUp('z')
                    shield = 0
                    phase = 0

                if pyautogui.locateOnScreen('thunder.png') and shield == 1 and phase == 1:
                    pydirectinput.keyDown('d')
                    pydirectinput.keyUp('d')
                    time.sleep(2)
                    pydirectinput.keyDown('z')
                    pydirectinput.keyUp('z')
                    shield = 0
                    phase = 0

            pot += 1
            repair += 1
                
            lis.stop()

if __name__ == "__main__":
    main()



