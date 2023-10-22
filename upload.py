#Importing the libraries
import webbrowser, pyautogui, random
from Utils.utils import *
from Utils.constants import *
import logging


logFile = os.path.join(os.environ.get('USERPROFILE'), 'tiktokcontainers', 'tiktok.log')
logging.basicConfig(filename=logFile, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def selectFile(path, selectFile) :
     #Click on "select file" button
        locateAndClick(selectFile)

        randomAwait()

        # Let's try to insert the path of the video in the input bar
        loc = justLocate('archiveName.png')
        
        if loc == 1 : 
            # If the archive name was not found
            print('The archive name was not found')
            loc = justLocate('archiveOpenButton.png')
            
            if loc == 1 : 
            # If the archive open button was not found
                print('The archive open button was not found')
                loc = justLocate('archiveCancelButton.png')

                if loc == 1 :
                # If the archive cancel button was not found
                    print('The archive cancel button was not found')
                    logging.warning('The archive name, the archive open button and the archive cancel button were not found')
                    closeWindow()
                    return
                else :
                # If the archive cancel button was found
                    pyautogui.click(loc[0]-100, loc[1]-14, duration = 1)
            else :
            # If the archive open button was found
                pyautogui.click(loc[0]-50, loc[1]-14, duration = 1)
        else : 
        # If the archive name was found
            pyautogui.click(loc[0]+40, loc[1], duration = 1)

        # Put the path of the video
        pyautogui.typewrite(path, interval = 0.1)
        pyautogui.press('enter')


        #Add captions
        sleep(210)
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

    '''
    This outter loop is to control how many videos each account will post
    '''
    for _ in range(3) :
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

            # Check it the user is or not logged in
            if justLocate('login2.png') != 1 :
                logging.warning(f'The user {account} not is logged!!!')
                accounts.remove(account)
                closeWindow()
                continue

            #Check if there is a captcha
            captchaWithOutThread()

            try : selectFile(path, 'selectFile.png')
            except :
                logging.warning('Error in selecting the file, first try')
                try : selectFile(path, 'selectFile2.png')
                except :
                    logging.warning('Error in selecting the file, second try, going to the next account')
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
                    selectFile(path, 'selectFile2.png')
                    locateAndClick('post.png')
                except :
                    logging.warning('Error in posting the video. Going to the next account')
                    closeWindow()
                    continue            
                
            awaitPure()
            #Check if there is a captcha
            captchaWithOutThread()

            #Click on the profile button
            try : locateAndClick('manage.png')
            except : 
                try :
                    logging.info('The manage button was not found')
                    closeWindow()
                    randomAwait()
                    locateAndClick('leavePage.png')
                except :
                    pass
            
            awaitPure()
            closeWindow()


if __name__ == '__main__' :
    main()