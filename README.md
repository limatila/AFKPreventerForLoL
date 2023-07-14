# AFK Preventer for LOL

  This is a simple program to prevent you League of Legends game dealing you a AFK timer, if you got too busy at a time.
  It's a code focused into auto click into a small area of your screen so you will not get a AFK leaverbuster punishment.

-How to use:
  1. Download: The entire repo and ignore the 'dist' folder /OR/ open the folder 'dist' and download the EXEcutable(faster, heavier, only one file independent of a Python Interpreter)
  2. Execute: Run 'afklolprevent.py' /OR/ Run 'afklolprevent.exe'
  3. Have fun!: the program is a automatic auto clicker, you can shut it down by closing the console or pressing the default 'Ctrl + C'


# Rules of execution:
  At the opening, the program will countdown a 5 seconds delay, then it'll start. 
  After starting, it'll begin a counter to check if the mouse is stopped in place. if it's not, the program will not autoclick anything.
  If it's stopped for 20 seconds(meaning that the player is afk) then it'll start auto clicking to move the Champion, preventing the game from giving you a AFK alert.
  2 minutes after the mouse being stopped, the mouse WILL STOP, not preventing the afk alert, to avoid suspicious of "hacking"
  If you move your mouse manually again, the counter will reset and the program will be able to autoclick again, preventing the AFK alert.


  OBS: 
  1. After 4 hours of usage, the program will exit.
  2. The console will display some logs about the execution, including if the mouse has moved, and how long has the execution of the preventer has passed (after 2min, will not be shown).
  3. All the logs will be also saved in 'Afk-Logs.txt", created within the folder the EXE is on activation.
  4. It might be a good idea to just change the name of the execution file (.py or .exe) to avoid suspicion of any anticheat search.


  
# Terms of use
This is a open software, amateur-based, without any burocracy and free to use. It was written by me with some inspiration in a video about automation of afk clicks.

By any means, i do not hold any responsibility about the usage of this code, i only wrote it to have more experience in automating a afk clicker in a screen.
This program can and cannot cause some suspicion about your League account, resulting in a ban for cheating. It's not tested in official live games, 
so there's no garanty you can pass uncognized while using this software. My advice is that you follow the Observation number 4. in the section above.
