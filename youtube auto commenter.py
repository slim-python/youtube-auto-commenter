import pyautogui
import time

print("""

█░░█ █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀▄ █▀▀    █▀▀█ █░░█ ▀▀█▀▀ █▀▀█    █▀▀ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
█▄▄█ █░░█ █░░█ ░░█░░ █░░█ █▀▀▄ █▀▀    █▄▄█ █░░█ ░░█░░ █░░█    █░░ █░░█ █░▀░█ █░▀░█ █▀▀ █░░█ ░░█░░ █▀▀ █▄▄▀  ==> By ABHI   
▄▄▄█ ▀▀▀▀ ░▀▀▀ ░░▀░░ ░▀▀▀ ▀▀▀░ ▀▀▀    ▀░░▀ ░▀▀▀ ░░▀░░ ▀▀▀▀    ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░▀▀
""")

print("THIS SCRIPT WILL AUTO COMMENT ON ANY LIVE YOUTUBE VIDEO")
def mainmenu():
    print("1 . to start")
    print("2 . to stop")
    selection=int (input("Enter choice: "))
    if selection==1:
        print("\n WARNING!!! to stop the script, you have to take your cursor to the top left, 3-4 times (untill it stops)")
        print("also you will have to maximize your browser window, in order to run this program\n")
            #take the comment from the user
        comment = input(str("enter the comment: "))

        time.sleep(3)
        # 3 second sleep to prepare the position for mouse cursor
        while True:
            time.sleep(1)
            pyautogui.click(1459,965)
            pyautogui.write(comment)
            pyautogui.click(1774,1019)
            pyautogui.click(1325,950)
    elif selection ==2:
        quit()
    else:
        print("""

        ##########################
        ɪɴᴠᴀʟɪᴅ ᴄʜᴏɪᴄᴇ Sᴛᴀʀᴛ ᴀɢᴀɪɴ
        ##########################
        
        """)
        mainmenu()


mainmenu()
