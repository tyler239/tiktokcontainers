#Importing the libraries
import os
import webbrowser, pyautogui, random, logging
from Utils.utils import *; from Utils.constants import *

logFile = os.path.join(os.environ.get('USERPROFILE'), 'tiktokcontainers', 'tiktok.log')
logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def main() :
    logging.info('Program started in the user sctipt')
    accounts = ACCOUNTS
    random.shuffle(accounts)

    if not webbrowser.open('https://www.google.com/') :
        logging.warning('The browser was not opened')
        exit()
    
    awaitPure();randomAwait();randomAwait()

    for account in accounts :    
        logging.info(f'############ Account: {account} ############')

        #Change to the container  
        chooseContainer(account)
        randomAwait();randomAwait();randomAwait() 

         #Go to tiktok
        try : locateAndClick('magnifying.png')
        except : 
            try : pyautogui.click(firefox_search_bar, duration = 1)
            except : 
                logging.warning('Nor the magnifying glass nor the search bar were found')
                closeWindow()
                continue 
        pyautogui.write('https://www.tiktok.com')
        pyautogui.press('enter')
        awaitPure();randomAwait();randomAwait()

        #Check if the user is logged in
        if isLoggedIn() == False :
            logging.warning(f'The user {account} is not logged!!!')
            closeWindow()
            continue

        #Check if there is a captcha
        #captchaWithOutThread()

        #Possibly like a video
        for _ in range(random.randint(7,21)) :
            try: 
                #When the user likes the video
                #1/3 of chances to comment 
                #and 1/6 to follow
                #All included in this function
                likeCommentFollow()
                    
                if random.randint(1,7) == 4 :
                    #UP
                    pyautogui.scroll(1100)
                    randomAwait()
                else :
                    #DOWN
                    pyautogui.scroll(-1100)
                    randomAwait()
                    if random.randint(1,3) == 3 : pyautogui.scroll(-1100)

                randomMovement()
                randomAwait()
                randomAwait()

            except :
                logging.warning('There was a problem liking a video')
                pyautogui.press('down')

            randomAwait()

        closeWindow()
    
    # To close the browser that was first opened
    randomAwait()
    closeWindow()


if __name__ == '__main__' :
    main()