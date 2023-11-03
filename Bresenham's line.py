from PIL import Image as img


def PixelIn(x,y,im):
    print(x,y)
    im.putpixel((x,y),0)   #add co-ordination in with x+something, y+something




def Line(x1,y1, x2, y2):

    im = img.new(mode='1', size=(1000, 1000), color=1)
    p1=[]
    m1=[]
    x,y=x1,y1
    dx=x2-x1
    dy=y2-y1
    dt=2*(dy-dx)
    ds=2*dy
    d=2*dy-dx
    while x<x2:
        x+=1
        if d<0:
            d=d+ds
        else:
            y+=1
            d=d+dt

        PixelIn(x,y,im)
        #
    im.save('line.png')
    im.show()
    #plt.plot(4,5,400,500)
    #plt.show()
if __name__=='__main__':
    Line(1,1,8,5)