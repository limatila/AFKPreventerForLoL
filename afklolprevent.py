#1.1: added flexible screensize detecter
import pyautogui as pag
import time; from random import randint, SystemRandom
from logging import debug, info, warning
InitArea = pag.size() #1366x768 no meu
print("""By Atila Lim
Simple script to click on yor screen to stay out of afk warns..
Press Ctrl+C to exit program(default cmd exit prompt)
\nStarting in 5 seconds...----------------""")

import defaultLog
from defaultLog import fileh
#fileh = FileHandler("Afk-logs.txt", 'a')
print('')
time.sleep(5)
print("Started --------------------------------")
info(f"You have an area of:{InitArea}")
print('')

SystemRandom
myPos = pag.position()
afk_timer = 0
while True:
    if afk_timer >= 14400: break
    if pag.position() == myPos: #if mousestopped
        afk_timer +=2
    else:
        afk_timer = 0
        myPos = pag.position()
        info("Mouse moved, not afk.")
    if afk_timer >= 240:
        warning("2 minutes time exceded: afk disabled")    
    elif afk_timer >= 20:
        #calc area to be used of the clicks
        myAreaX, myAreaY = pag.size() #if area changes, will still use this to get the area
        Xrange = [round((myAreaX/5) * 2), round((myAreaX/5) * 3)]
        Yrange = [round(myAreaY/4 * 2), round((myAreaY/4) * 3)]

        #execute the clicks
        floatsChoice = (SystemRandom().uniform(0, 1)) #secure random float
        info("Afk enabled.")
        xVar = randint(Xrange[0], Xrange[1])
        yVar = randint(Yrange[0], Yrange[1])
        pag.click(button="right", x=xVar, y=yVar)
        time.sleep(floatsChoice)
        pag.hotkey("S")
        myPos = pag.position()

        time_displayed = afk_timer
        debug(f'Time stoped: {time_displayed:,.1f} seconds(so or less).'.format(time_displayed))
    print('')
    time.sleep(2)

warning("4-hour time exceded: the program will now close.")

