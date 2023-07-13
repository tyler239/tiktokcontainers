#Importing the libraries
import webbrowser, pyautogui
from Utils.utils import *

#Put here the (x,y) location of the required elements
firefox_search_bar = (516, 64)
archive_search_bar = (505,657)
open_button_of_search_bar = (1191,687)


def main() :
    accounts = getAccounts()
    path = getVideoPath() 

    #Open the browser in google
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
        likeRandomVideo()
        randomAwait()

        #Click in upload video
        try : locateAndClick('upload.png')
        except : 
            closeWindow()
            continue

        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()
    
        #Click on "select file" button
        try : locateAndClick('selectFile.png')
        except : 
            closeWindow()
            continue

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
        try : locateAndClick('hashtag.png')
        except : 
            closeWindow()
            continue

        deleteAutoGui()
        pyautogui.typewrite(account[1], interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()

        #Click on the post button
        try : locateAndClick('post.png')
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

        #Check if there is a captcha
        captchaWithOutThread()
    
        closeWindow()
        
   

if __name__ == '__main__' :
    main()
