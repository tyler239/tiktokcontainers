#Importing the libraries
import webbrowser, pyautogui, random
from Utils.utils import *
from Utils.constants import *
import logging


logFile = os.path.join(os.environ.get('USERPROFILE'), 'tiktokcontainers', 'tiktok.log')
logging.basicConfig(filename=logFile, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def selectFile(path, selectFile) :
        # Click on "select file" button
        locateAndClick(selectFile)
        randomAwait();randomAwait();randomAwait()

        # Put the path of the video
        pyautogui.write(path)
        pyautogui.press('enter')

def putHashtags() :
    locateAndClick('hashtag.png')
    deleteAutoGui()
    pyautogui.typewrite(HASHTAGS() , interval = 0.3)
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
            paths = []; stop = 0
            while len(paths) < 2  and stop < 5:
                stop += 1
                path = getVideoPath()
                if path not in paths : paths.append(path)
        except :    
            logging.warning('There was no video to upload')
            exit()

        #Change to the container  
        if chooseContainer(account) == False :
            logging.warning(f'The container {account} does not exist')
            continue

        pyautogui.write('https://www.tiktok.com/creator-center/upload')
        pyautogui.press('enter')
        awaitPure()

        # Check it the user is or not logged in
        if isLoggedIn() == False :
            logging.warning(f'The user {account} is not logged!!!')
            closeWindow()
            continue

        #Check if there is a captcha
        #captchaWithOutThread()

        
        # In this for loop, we post all the videos that were selected
        for path in paths : 
            try : selectFile(path, 'selectFile.png')
            except :
                logging.warning('Error in selecting the file, first try')
                try : selectFile(path, 'selectFile2.png')
                except :
                    logging.warning('Error in selecting the file, second try, going to the next path')
                    pyautogui.hotkey('ctrl', 'r')
                    continue

            # Wait 3 minutes to upload the video
            sleep(210)

            try : putHashtags()  
            except Exception as e :
                logging.warning(f'Error in adding the hashtags: {e}')
                
            
            # Scroll down to post the video
            try : 
                pyautogui.scroll(-1000)
                randomAwait()
                randomAwait()
                locateAndClick('post.png')
            except : 
                try :
                    pyautogui.hotkey('ctrl', 'r')
                    locateAndClick('leavePage.png')
                    awaitPure()
                    selectFile(path, 'selectFile2.png')
                    putHashtags()
                    pyautogui.scroll(-1000)
                    randomAwait();randomAwait()
                    locateAndClick('post.png')
                except :
                    logging.warning('Error in posting the video. Going to the next account')
                    break            
                    
            awaitPure()
            # Check if there is a captcha
            # captchaWithOutThread()

            # Click on the post another video button 
            try : locateAndClick('uploadAnother.png')
            except : 
                try :
                    randomAwait()
                    locateAndClick('leavePage.png')
                    randomAwait()
                except :
                    break
            
        # Preparing to go to next account
        awaitPure()
        closeWindow()
    
    logging.info('Program finished in the uploadMode sctipt')
    closeWindow()
    exit()


if __name__ == '__main__' :
    main()