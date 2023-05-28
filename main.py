#Importing the libraries
import webbrowser, pyautogui
from Utils.utils import *

#Put here the (x,y) location of the required elements
profile_icon = (1332,115)
logout_location = (1240,462)
search_bar = (505,657)
open_button_of_search_bar = (1191,687)


def main() :
    accounts = getAccounts()
    path = getVideoPath() 

    for account in accounts :

        #Open the browser in google
        webbrowser.open('https://www.google.com/')
        awaitPure()

        #Change to the container  
        chooseContainer(account[0])
        randomAwait()

        #Go to tiktok
        locateAndClick('magnifying.png')
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
        except : closeWindow()

        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()
    
        #Click on "select file" button
        try : locateAndClick('selectFile.png')
        except : closeWindow()

        randomAwait()

        #Click on the search bar of the archive explorer
        pyautogui.click(search_bar ,duration = 1)

        #Put the path of the video
        pyautogui.typewrite(path, interval = 0.1)

        #Click in open
        pyautogui.click(open_button_of_search_bar,duration = 1)
        awaitPure()

        #Add captions
        try : locateAndClick('hashtag.png')
        except : closeWindow()

        deleteAutoGui()
        pyautogui.typewrite(account[1], interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()

        #Click on the post button
        try : locateAndClick('post.png')
        except : closeWindow()
             
        awaitPure()
 
        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the profile button
        try : locateAndClick('viewProfile.png')
        except : closeWindow()
             
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()
    
        closeWindow()
        
   

if __name__ == '__main__' :
    main()
