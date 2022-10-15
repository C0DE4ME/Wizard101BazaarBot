from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse

#Defines click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def refresh():
    print("Refreshing")
    click(1500, 850)
    time.sleep(0.05)
    click(640,360)
    time.sleep(2)

items = ['agave.jpg', 'agaveleaves.jpg']
page = 1
time.sleep(2)
refresh()
while keyboard.is_pressed('q') == False:
    click(1100,350)
    skip = 0
    print("Page: " + str(page))
    buy = 0
    i = 0
    for x in items:
        
        # Tells script whether to skip the first reagent after the first page
        skipAFP = 1
        p1Only = 1
        skip = 0
        if skipAFP == 1:
            if page > 1 and i <= 1:
                skip = 1

        if skip == 0:
            if pyautogui.locateOnScreen(items[i], region=(1150,500,280,530), grayscale=True, confidence=0.95)!= None:
                print("Found " + items[i] + " <-----------------------------------")
                buy = i+1
        i += 1
    if buy >= 1:
        # Clicks on item in shop
        pos = pyautogui.locateOnScreen(items[buy-1], confidence=(0.95))
        click(pos[0], pos[1])
        time.sleep(0.05)
        # Clicks on Buy More
        click(800, 1140)
        time.sleep(0.05)
        # Clicks on amount, enters 999
        click(1060, 850)
        time.sleep(0.05)
        pyautogui.press('9')
        pyautogui.press('9')
        pyautogui.press('9')
        # Clicks buy
        click(1080, 1110)
        time.sleep(1)
        # Clicks OK
        click(1540, 860)
        time.sleep(0.05)
        skip = 1
    print("Debug: " + str(pyautogui.pixel(1717, 1071)[0]))
    if pyautogui.pixel(1717, 1071)[0] == 205 and skip == 0 and p1Only == 0:
        print("Next page")
        click(1700,1120)
        page += 1
        time.sleep(0.05)
    else:
        page = 1
        refresh()
