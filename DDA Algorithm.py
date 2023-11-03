from PIL import Image as img




def PixelIn(x,y,im):
    print(x,y)
    im.putpixel((x,y),0)   #add co-ordination in with x+something, y+something

def ROUND(a):
    return int(a + 0.5)



def Line(x1,y1, x2, y2):

    im = img.new(mode='1', size=(1000, 1000), color=1)
    x, y = x1, y1
    length = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else (y2 - y1))
    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)
    for i in range(length):
        PixelIn(ROUND(x),ROUND(y),im)
        x += dx
        y += dy
    im.save('DDA.png')
    im.show()
    #plt.plot(4,5,400,500)
    #plt.show()
if __name__=='__main__':
    Line(4,5,400,500)