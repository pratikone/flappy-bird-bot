import time
import Image
import ImageGrab
import flappy
from msvcrt import getch
from SendKeys import SendKeys



while True :
    time.sleep(0.3)
    t = str(time.time()).replace('.','-')
    tt = time.time()
    img = ImageGrab.grab()
    #img.save(''.join(['C:/Users/PratikONE/Desktop/grab_',t,'.png']))
    flappy.findCoords(img) #taking too much of time >1s, reduce to ~ 30 ms
    SendKeys('{SPACE}')

    

