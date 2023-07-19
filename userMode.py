#Importing the libraries
import webbrowser, pyautogui, random
from Utils.utils import *

firefox_search_bar = (516, 64)


def main() :
    accounts = getAccounts()
    random.shuffle(accounts)

    webbrowser.open('https://www.google.com/')
    awaitPure()

    for account in accounts :    

        #Change to the container  
        chooseContainer(account[0])
        randomAwait() 

         #Go to tiktok
        try : locateAndClick('magnifying.png')
        except : 
            try : pyautogui.click(firefox_search_bar, duration = 1)
            except : 
                closeWindow()
                continue 
        pyautogui.typewrite('https://www.tiktok.com', interval = 0.25)
        pyautogui.press('enter')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        #Possibly like a video
        for _ in range(random.randint(0,5)) :
            likeRandomVideo()
            randomAwait()
        
        closeWindow()


if __name__ == '__main__' :
    main()
