#Importing the libraries
import webbrowser, pyautogui, random
from Utils.utils import *
from Utils.constants import *
import logging


logFile = os.path.join(os.environ.get('USERPROFILE'), 'tiktokcontainers', 'tiktok.log')
logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def selectFile(path) :
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
        pyautogui.typewrite(HASHTAGS() , interval = 0.1)
        randomAwait()

        #Add description here if necessary !!!!!!!!!
        
        #Scroll down to post the video
        pyautogui.scroll(-1000)
        randomAwait()
        randomAwait()


def main() :
    logging.info('Program started in the uploadMode sctipt')
    accounts = ACCOUNTS
    random.shuffle(accounts)

    #Open the browser in google
    if not webbrowser.open('https://www.google.com/') :
        logging.warning('The browser was not opened')
        exit()
        
    awaitPure()

    for account in accounts :
        logging.info(f'############ Account: {account} ############')

        try : 
            path = getVideoPath()
        except : 
            logging.warning('There was no video to upload')
            exit()

         #Change to the container  
        chooseContainer(account)
        randomAwait()

        #Go to tiktok upload url
        try : locateAndClick('magnifying.png')
        except : 
            try : pyautogui.click(firefox_search_bar, duration = 1)
            except : 
                logging.warning('Nor the magnifying glass nor the search bar were found')
                closeWindow()
                continue 
        pyautogui.typewrite('https://www.tiktok.com/upload', interval = 0.25)
        pyautogui.press('enter')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        try : selectFile(path)
        except :
            logging.warning('Error in selecting the file, first try')
            closeWindow()
            continue

        #Click on the post button
        try : 
            locateAndClick('post.png')
        except : 
           try :
               pyautogui.hotkey('ctrl', 'r')
               locateAndClick('leavePage.png')
               awaitPure()
               selectFile(path)
               locateAndClick('post.png')
           except :
               logging.warning('Error in posting the video')
               closeWindow()
               continue            
             
        awaitPure()
        #Check if there is a captcha
        captchaWithOutThread()

        #Click on the profile button
        try : locateAndClick('viewProfile.png')
        except : 
            logging.debug('The view profile button was not found')
            closeWindow()
            continue
            
        awaitPure()
        closeWindow()


if __name__ == '__main__' :
    main()