from time import sleep
from Utils.constants import *
import random, os, pyautogui, random, logging

#Await functions
randomAwait = lambda : sleep(random.randint(1,3))
awaitPure = lambda : sleep(random.randint(5,10))

def isLoggedIn() :
    if(justLocate('login.png') != 1) :
        randomAwait()
        return False

    if(justLocate('login2.png') != 1) :
        randomAwait()
        return False

    return True

#User Interface functions
def deleteAutoGui() :
       for _ in range(3) : pyautogui.hotkey('ctrl', 'right')
       for _ in range(50) : pyautogui.press('backspace')


def locateAndClick(image) :
        assetsPath = os.path.abspath(os.path.dirname(__file__).replace('Utils', 'Assets'))

        # Try to locate the image in the English and Portuguese folder
        if os.path.exists(os.path.join(assetsPath, 'Images', 'English', image)) :
            p = os.path.join(os.getcwd(), 'Assets', 'Images', 'English',  image)
        elif os.path.exists(os.path.join(assetsPath, 'Images', 'Portuguese', image)) :
            p = os.path.join(os.getcwd(), 'Assets', 'Images', 'Portuguese',  image)

        # Try to click the image with 3 different confidences
        for i in range(3) :
                c = 0.9 - (i/10 if i != 0 else 0)
                t = pyautogui.locateCenterOnScreen(p, grayscale=False, confidence=c)
                if(t) :
                      pyautogui.click(t, duration = random.randint(1,2))
                      return 
                awaitPure()
                
        logging.warning(f'Element {image} was not found')
        pyautogui.press('down')
        raise Exception('Error in loading the page(element to click was not found)! Program stoped')

def justLocate(image) :
        assetsPath = os.path.abspath(os.path.dirname(__file__).replace('Utils', 'Assets'))

        # Try to locate the image in the English and Portuguese folder
        if os.path.exists(os.path.join(assetsPath, 'Images', 'English', image)) :
            p = os.path.join(os.getcwd(), 'Assets', 'Images', 'English',  image)
        elif os.path.exists(os.path.join(assetsPath, 'Images', 'Portuguese', image)) :
            p = os.path.join(os.getcwd(), 'Assets', 'Images', 'Portuguese',  image)

        # Try to click the image with 3 different confidences
        for i in range(3) :
                c = 0.9 - (i/10 if i != 0 else 0)
                t = pyautogui.locateCenterOnScreen(p, grayscale=False, confidence=c)
                if(t) :
                      return t
                
        # If it does not find the image, return 1
        return 1
                


def likeCommentFollow() : 
      # Max of 2 loops for the same video
      x = random.randint(1,2)
      for _ in range(x) :     
            
            #Await for a sec
            if (random.randint(1,5) == 5) : awaitPure()
            else : randomAwait()

            #Like a video or do a random movement
            if(random.randint(1,2) == 2) : 
                try : locateAndClick('like.png')
                except :
                      try : 
                        t = justLocate('comments.png')
                        if t != 1 : pyautogui.click(t[0], t[1]-75, duration = 1)
                      except : 
                        logging.warning('Nor the like button nor the comment button were found')
                        pyautogui.press('l')
        
            randomAwait()
            if(random.randint(1,10) == 10) : 
                commentOnVideo()

            randomAwait()
            if(random.randint(1,20) == 20) :
                try : locateAndClick('follow.png')
                except : pass
           
            randomMovement()

def commentOnVideo() :
      try : 
        locateAndClick('comments.png')
      except :
        pyautogui.click(TIKTOK_CENTER, duration = 1)
        pyautogui.press('enter')
     
      randomAwait()
      randomAwait()
      awaitPure()
      randomMovement()
      randomAwait()
      try :
            locateAndClick('addComment.png')
            pyautogui.typewrite(random.choice(COMMENTS), interval = 0.25)
            pyautogui.press('enter')
      except :
            p = justLocate('volumeOn.png')
            if p != 1 :
                pyautogui.click(p[0]+85, p[1], duration = 1)
                pyautogui.typewrite(random.choice(COMMENTS), interval = 0.25)
                pyautogui.press('enter')
            else :
                  p = justLocate('volumeOff.png')
                  if p != 1 :
                        pyautogui.click(p[0]+85, p[1], duration = 1)
                        pyautogui.typewrite(random.choice(COMMENTS), interval = 0.25)
                        pyautogui.press('enter')
      finally :
            randomAwait()
            randomAwait()
            locateAndClick('exitFromComments.png')
            randomAwait()


def randomMovement() :
      pyautogui.moveTo(random.randint(530,750), random.randint(300,700), duration = 1.5)


#Functions related to the video
def getVideoPath():
    videos_dir = os.path.join(os.getcwd(), 'Assets', 'Videos')

    # Check if the "Videos" folder exists, and create it if it doesn't
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)

    if len(os.listdir(videos_dir)) == 0:
        print('There is no video to upload')
        raise Exception('There is no video to upload')

    return os.path.join(videos_dir, random.choice(os.listdir(videos_dir)))

def excludeUsedVideo(path) :
        os.remove(path)

#Captcha functions
def captchaWithOutThread() :
    randomAwait()
    return
    if(pyautogui.locateOnScreen('Assets\\Images\\English\\captcha.png') or 
       pyautogui.locateOnScreen('Assets\\Images\\English\\dragAndSlide.png') or 
       pyautogui.locateOnScreen('Assets\\Images\\Portuguese\\3D.png') or 
       pyautogui.locateOnScreen('Assets\\Images\\Portuguese\\3D2.png')
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
    awaitPure()
    pyautogui.keyDown('shift')
    pyautogui.hotkey('ctrl', f'{num}')
    pyautogui.keyUp('shift')