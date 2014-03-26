from PIL import Image



def findCoords(im) :

    pixels = im.load()
    w, h = im.size

    #find x of flappy bird

    for x in range(w):
        for y in range(h):    
            r,g,b = pixels[x,y]
            if r == 212 and g == 191 and b == 39  :
              _r, _g, _b = pixels[x+14, y]
              if _r == 234 and _g == 80 and _b == 64 :
                 flappy_x = x
                 flappy_y = y
                 break

    try :
        flappy_x
        flappy_y
    except :
        NameError
        return
    else :  
        print "Flappy bird pos x: ", flappy_x, "y: ",flappy_y

    pos = -1

    Y = h-200
    
    #find x to start
    for x in range(flappy_x + 50, w):
        r,g,b = pixels[x, Y]
        #print "X ",x," Y ", h-200
        #print r, g, b
        if r == 85 and g == 128 and b == 34:
            pos = x
            break

    flag = False
    if pos != -1 :
        for y in range(Y, 0, -1):
            r,g,b = pixels[pos, y]
            if flag == False and r == 112  and g == 197 and b == 206: #blue
                flag = True
                y2 = y

            if flag == True and r != 112  and g != 197 and b != 206 :   # not blue
                y1 = y
                break
    try:
        y1
        y2
    except : NameError 
    else:
        
        print "x : ", pos, "y : ", y1
        print "x : ", pos, "y : ", y2
        
    print "Finished"

if __name__ == "__main__" :
    im = Image.open("C:/Users/PratikONE/Desktop/grab_1393228856-86.png")
    findCoords(im)
