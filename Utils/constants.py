import ctypes
import random
import platform

ACCOUNTS = [1,2,3,4,5,6,7,8,9]

hashtags = '#amazonfinds #amazonmusthaves #amazon #coolproducts #kitchen #gadgets #giftideas #homehacks #lifehacks #kitchenhacks #home #amazonfinds #amazonmusthaves #amazon #coolproducts #gadgets #giftideas #homehacks #lifehacks #home #kitchen #amazonfinds #amazonmusthaves #amazon #coolproducts #gadgets #giftideas #homehacks #lifehacks #techtok #home #tech'

HASHTAGS = lambda : ''.join([random.choice([i for i in hashtags.split(' ') if i]) for _ in range(3)])


firefox_search_bar = (516, 64)
archive_search_bar = (505,657)
open_button_of_search_bar = (1191,687)

if platform.system() == 'Windows' :
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        TIKTOK_CENTER = (screensize[0]//2, screensize[1]//2)
else :
        TIKTOK_CENTER = (720, 400)



COMMENTS = ['bem', 'nem falo isso ai', 'kkkkkkkkkkk', 'kkk', 'k', 'KKKKKKKKKKKKKKKK', 'KKKKKKKKK'
            , 'K', 'KK', 'SKSKSKSKSKSSKSKSKSKSKSKSS', 'APSDOIFAPSIOJFDJASIJDF', 'RS', 'RSRSRSRSRSRS',
            'rsrs', 'botei fe', 'la ele', 'la ele mil', 'hahahaahahahahaahaha', 'ahahahahaahah'
            , 'ha', 'ah', 'ahh', 'ahhh', 'ahhh ent ele e', 'jeejejejeejejej', 'JEJEJEEJEJEJEJE', 
            'je', 'lmao', 'LMAO', 'idk...', 'aka yo mama', 'cringe', 'fake']