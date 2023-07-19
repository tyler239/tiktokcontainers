#Importing the libraries
import webbrowser, pyautogui, random
from Utils.utils import *

#Put here the (x,y) location of the required elements
firefox_search_bar = (516, 64)
archive_search_bar = (505,657)
open_button_of_search_bar = (1191,687)


def selectFile(path, hashtag) :
     #Click on "select file" button
        locateAndClick('selectFile.png')

        randomAwait()

        #Click on the search bar of the archive explorer
        pyautogui.click(archive_search_bar ,duration = 1)

        #Put the path of the video
        pyautogui.typewrite(path, interval = 0.1)

        #Click in open
        pyautogui.click(open_button_of_search_bar,duration = 1)
        awaitPure()
        sleep(180)

        #Add captions
        locateAndClick('hashtag.png')
         
        deleteAutoGui()
        pyautogui.typewrite(hashtag , interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()


def main() :
    accounts = getAccounts()
    random.shuffle(accounts)

    #Open the browser in google
    webbrowser.open('https://www.google.com/')
    awaitPure()

    for account in accounts :
        path = getVideoPath() 

         #Change to the container  
        chooseContainer(account[0])
        randomAwait()

        #Go to tiktok upload url
        try : locateAndClick('magnifying.png')
        except : 
            try : pyautogui.click(firefox_search_bar, duration = 1)
            except : 
                closeWindow()
                continue 
        pyautogui.typewrite('https://www.tiktok.com/upload', interval = 0.25)
        pyautogui.press('enter')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        try : selectFile(path, account[1])
        except :
            closeWindow()
            continue

        #Click on the post button
        try : 
            locateAndClick('post.png')
        except : 
           try :
               pyautogui.hotkey('ctrl', 'r')
               randomAwait()
               selectFile(path, account[1])
               locateAndClick('post.png')
           except :
               closeWindow()
               continue            
             
        awaitPure()
        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the profile button
        try : locateAndClick('viewProfile.png')
        except : 
            closeWindow()
            continue
            
        awaitPure()
        closeWindow()


if __name__ == '__main__' :
    main()