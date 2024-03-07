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

        # Change to the container if it exists
        if chooseContainer(account) == False :
            logging.warning(f'The container {account} does not exist')
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
        for _ in range(random.randint(8,16)) :
            try: 
                if random.randint(1,4) == 4 : back2ForYou()

                likeCommentFollow()


                if random.randint(1,10) == 10 :
                    #UP
                    pyautogui.press('up')
                    randomAwait()
                else :
                    #DOWN
                    pyautogui.press('down')
                    randomAwait()
                    if random.randint(1,2) == 2 : pyautogui.scroll(-1100)

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
    logging.info('Program finished')