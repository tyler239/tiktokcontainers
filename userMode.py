#Importing the libraries
import webbrowser, pyautogui, random, logging
from Utils.utils import *

firefox_search_bar = (516, 64)

logging.basicConfig(filename='tiktok.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def main() :
    logging.info(f'Program started in the {__name__} sctipt')
    accounts = getAccounts()
    random.shuffle(accounts)

    webbrowser.open('https://www.google.com/')
    awaitPure()

    for account in accounts :    
        logging.info(f'############ Account: {account[0]} ############')

        #Change to the container  
        chooseContainer(account[0])
        randomAwait() 

         #Go to tiktok
        try : locateAndClick('magnifying.png')
        except : 
            try : pyautogui.click(firefox_search_bar, duration = 1)
            except : 
                logging.warning('Nor the magnifying glass nor the search bar were found')
                closeWindow()
                continue 
        pyautogui.typewrite('https://www.tiktok.com', interval = 0.25)
        pyautogui.press('enter')
        awaitPure()

        #Check if there is a captcha
        captchaWithOutThread()

        #Possibly like a video
        for _ in range(random.randint(0,5)) :
            try: 
                likeRandomVideo()
            except :
                logging.warning('There was a problem liking a video')
                pass
            randomAwait()
        
        closeWindow()


if __name__ == '__main__' :
    main()
