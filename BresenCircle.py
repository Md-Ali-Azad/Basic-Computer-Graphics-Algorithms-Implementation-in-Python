from PIL import Image as img

def drawCircle(xc, yc ,x, y,im):
    print(xc+x, yc+y)
    print(xc-x, yc+y)
    print(xc+x, yc-y)
    print(xc-x, yc-y)

    print(xc+y, yc+x)
    print(xc-y, yc+x)
    print(xc+y, yc-x)
    print(xc-y, yc-x)
    im.putpixel((xc+x, yc+y), 0)
    im.putpixel((xc-x, yc+y), 0)
    im.putpixel((xc+x, yc-y), 0)
    im.putpixel((xc-x, yc-y), 0)
    im.putpixel((xc+y, yc+x), 0)
    im.putpixel((xc-y, yc+x), 0)
    im.putpixel((xc+y, yc-x), 0)
    im.putpixel((xc-y, yc-x), 0)

def circleBres(xc,yc,r)  :
    im = img.new(mode='1', size=(1000,1000),color=1)
    x,y = 0,r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y,im)
    while (y >= x):
        # // for each pixel we will
        # // draw all eight pixels

        x+=1

        #  check for decision parameter
        #  and correspondingly
        #  update d, x, y
        if (d > 0):   #d<0 ractangle
            y-=1
            d = d + 4 * (x - y) + 10

        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y,im)
    im.save('circle.png')
    im.show()
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #file_path = os.path.join(dir_path,"circle.png")
    #im.show()
    #im.save(fp=file_path)

circleBres(500,400,300)