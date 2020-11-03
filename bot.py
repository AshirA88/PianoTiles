from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Postion of mouse for every column
#Tile 1 Position: X:  750 Y:  400 RGB: ( 77,  80, 116)
#Tile 2 Position: X:  885 Y:  400 RGB: (  77,  80, 116)
#Tile 3 Position: X:  1030 Y:  400 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  1165 Y:  400 RGB: ( 80,  83, 116)

#Function to Click on Black Square
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#While loop for the game till 'q' is pressed to quit
while keyboard.is_pressed('q') == False:    
    if pyautogui.pixel(750, 400)[0] == 0:
        click(750, 400)
    if pyautogui.pixel(885, 400)[0] == 0:
        click(885, 400)
    if pyautogui.pixel(1030, 400)[0] == 0:
        click(1030, 400)
    if pyautogui.pixel(1165, 400)[0] == 0:
        click(1165, 400)
