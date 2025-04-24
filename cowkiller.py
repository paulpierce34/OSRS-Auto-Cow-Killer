import time
import pyautogui
import cv2


pyautogui.FAILSAFE = True ## This enables you to cancel 
confidencelevel = 0.54 ## .51 is clutch
cowhideconfidencelevel = .77 #.73 is good
boneconfidencelevel = .50
compassconfidencelevel = .60


    




def bury():
    print ('Kicking off burying script...')
    allbones = ["bones1.png"]
    count = 0
    while (1==1):
        if (count > 10):
            cows()
        print("Looking for bones")
        for bone in allbones:
            print (f'Looking for {bone}')
            bonelocation = pyautogui.locateOnScreen(bone, confidence=boneconfidencelevel)
            if (bonelocation):
                print (f"Found {bone}! at {bonelocation}")
                centerofhide = pyautogui.center(bonelocation)
                pyautogui.moveTo(centerofhide, duration=.5)
                # Pick up loot
                pyautogui.click()
                time.sleep(.5)
                pyautogui.click()
                time.sleep(.25)
                pyautogui.click()
                time.sleep(.29)
                pyautogui.click()
                print ("Sleeping 6 secs.")
                time.sleep(2)
                del bonelocation ## clear variable
                break  
            else:
                count += 1
                print('No bones found... Back to cows() function')
                cows()

        print ('No bones found in allbones array....')

def loot():
    print ('Kicking off looting script...')
    allhides = ["cowhide.png", "cowhide2.png"]
    count = 0
    while (1==1):
        if (count > 5):
            #bury() ## if you want to bury bones
            cows()
        for hide in allhides:
            print (f'Looking for {hide}')
            hidelocation = pyautogui.locateOnScreen(hide, confidence=cowhideconfidencelevel)
            if (hidelocation):
                count +=1
                print (f">>> Found COWHIDE {hide}! at {hidelocation}")
                centerofhide = pyautogui.center(hidelocation)
                pyautogui.moveTo(centerofhide, duration=.5)
                pyautogui.rightClick()
                pyautogui.move(0,100, duration=.5)
                pyautogui.click()
                time.sleep(2)
                del hidelocation
            else:
                print('Unable to find cowhide... trying again')
                count +=1
                #bury() ## if you want to bury bones
                cows()
        

def cows():
    allcows = ["cowsie.png", "cowsie2.png", "cowsie3.png", "cowsie4.png", "cowsie5.png", "cowsie6.png"]
    count = 0
    while (1==1):
        print ("Kicking off cows() script")
        for cowpic in allcows:
            print (f'Looking for {cowpic}')
            cowlocation = pyautogui.locateOnScreen(cowpic, confidence=confidencelevel)
            if (cowlocation):
                print (f"Found {cowpic}! at {cowlocation}")
                centerofcow = pyautogui.center(cowlocation)
                pyautogui.moveTo(centerofcow, duration=.2)
                pyautogui.click()
                print ("Sleeping 8 secs.")
                time.sleep(6)
                del cowlocation
            else:
                if (count > 8):
                    count = 0
                    print("40 count exceeded! Kicking off loot() function for cowhides")
                    loot()
                count += 1   
        print ('None found in allcows array....')

try:
    cows()
except KeyboardInterrupt:
    print ("CTRL + C detected. Exiting script.")
    exit(0)
    
        
