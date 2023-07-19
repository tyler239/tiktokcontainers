import random, os, pyautogui,  time, random
from time import sleep


#Await functions
randomAwait = lambda : sleep(random.randint(1,3))
awaitPure = lambda : sleep(random.randint(25,30))


#User Interface functions
def deleteAutoGui() :
       for _ in range(3) : pyautogui.hotkey('ctrl', 'right')
       for _ in range(50) : pyautogui.press('backspace')


def locateAndClick(image) :
        p = os.path.join(os.getcwd(), 'Assets', 'Images', 'English',  image)

        for i in range(3) :
                c = 0.9 - (i/10 if i != 0 else 0)
                t = pyautogui.locateCenterOnScreen(p, grayscale=False, confidence=c)
                if(t) :
                      pyautogui.click(t, duration = random.randint(1,3))
                      return 
                awaitPure()
                
        raise Exception('Error in loading the page(element to click was not found)! Program stoped')


def likeRandomVideo() : 
      x = random.randint(1,4)
      for _ in range(1,x) : 
            
            #Await for a sec
            if (int(time.time())%5 == 0) : awaitPure()
            else : randomAwait()

            #Like a video or do a random movement
            if(int(time.time())%3 == 0) : locateAndClick('like.png')
            else : randomMovement()

            randomAwait()
            pyautogui.scroll(-1100)
            sleep(random.randint(1,2))
            pyautogui.scroll(-1100)

def randomMovement() :
      pyautogui.move(random.randint(-100,100), random.randint(-100,100), duration = 0.5)


#Functions related to the video
def getVideoPath() :
        video_options = []
        path = os.path.join(os.getcwd(), 'Assets', 'Videos')
        for filename in os.listdir(path) :
                video_options.append(filename)

        if len(video_options) == 0 :
                print('There is no video to upload')
                raise Exception('There is no video to upload') 
              
        return os.path.join(os.getcwd(), 'Assets', 'Videos', random.choice(video_options))

def excludeUsedVideo(path) :
        os.remove(path)


#Getting the accounts information from the file
def getAccounts() :
    
    #If the directory "Accounts" or the file "accounts.txt" doesn't exist, create them
    if(os.path.exists(os.path.join(os.getcwd() ,'Accounts')) == False) : os.mkdir('Accounts')
    if(os.path.exists(os.path.join(os.getcwd(), 'Accounts', 'accounts.txt')) == False) :
        with open(os.path.join(os.getcwd(), 'Accounts', 'accounts.txt'), 'w') as file :
            file.write('')

    accounts = []
    path = os.path.join(os.getcwd(), 'Accounts', 'accounts.txt')
    with open(os.path.abspath(path) ,'r') as file :
        for line in file :
              t = tuple(el.strip() for el in line.split(','))
              accounts.append(t)

    if(len(accounts) == 0) : 
        print('There is no account to upload the video')
        raise Exception('There is no account to upload the video')
    
    return accounts


#Captcha functions
def captchaWithOutThread() :
    randomAwait()
    if(pyautogui.locateOnScreen('Assets\Images\English\captcha.png') or 
       pyautogui.locateOnScreen('Assets\Images\English\dragAndSlide.png') or 
       pyautogui.locateOnScreen('Assets\Images\Portuguese\\3D.png') or 
       pyautogui.locateOnScreen('Assets\Images\Portuguese\\3D2.png')
       ):
        input('Captcha DETECTED, resolve mannually the captcha and after press "ENTER" to continue the program')
        print('The program will continue in 30 seconds...')
        awaitPure()

#Proxy functions
def setUpProxy(proxy) :
        os.system('cmd /c netsh winhttp set proxy ' + proxy)

def removeProxy() :
        os.system('cmd /c netsh winhttp reset proxy')


#If something goes wrong, logout 
def closeWindow() :
      awaitPure()
      pyautogui.hotkey('ctrl', 'w')


#Choose a container
def chooseContainer(num) :
    pyautogui.keyDown('shift')
    pyautogui.hotkey('ctrl', f'{num}')
    pyautogui.keyUp('shift')