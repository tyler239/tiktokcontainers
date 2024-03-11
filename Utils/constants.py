import os
import ctypes
import random
import platform

BASE_PATH = f"{os.environ.get('USERPROFILE')}\\tiktokcontainers"

ACCOUNTS = [1,2,3,4,5,6,7]

hashtags = '#sucesso #ganhardinheiroonline #ferramentas #marketingdigital #sites #jovensdenegócios #riqueza #milionario #rico #money'

HASHTAGS = lambda : ''.join([random.choice([i for i in hashtags.split(' ') if i]) for _ in range(3)])

if platform.system() == 'Windows' :
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        TIKTOK_CENTER = (screensize[0]//2, screensize[1]//2)
else :
        TIKTOK_CENTER = (720, 400)

firefox_search_bar = (screensize[0]//2, int((screensize[1])*1/14))


COMMENTS = ['bem', 'nem falo isso ai', 'kkkkkkkkkkk', 'kkk', 'k', 'KKKKKKKKKKKKKKKK', 'KKKKKKKKK'
            , 'K', 'KK', 'SKSKSKSKSKSSKSKSKSKSKSKSS', 'APSDOIFAPSIOJFDJASIJDF', 'RS', 'RSRSRSRSRSRS',
            'rsrs', 'botei fe', 'la ele', 'la ele mil', 'hahahaahahahahaahaha', 'ahahahahaahah'
            , 'ha', 'ah', 'ahh', 'ahhh', 'ahhh ent ele e', 'jeejejejeejejej', 'JEJEJEEJEJEJEJE', 
            'je', 'lmao', 'LMAO', 'idk...', 'aka yo mama', 'cringe', 'fake']