from PIL import Image as img

def drawMidCircle1(xc, yc ,x, y,im):
    im.putpixel((x+xc, -y+yc), 0)
    im.putpixel((y+xc, x+yc), 0)
    im.putpixel((-y+xc, x+yc), 0)

def drawMidCircle2(xc, yc ,x, y,im):
    im.putpixel((x+xc, y+yc), 0)
    im.putpixel((-x+xc, y+yc), 0)
    im.putpixel((x+xc, -y+yc), 0)
    im.putpixel((-x+xc, -y+yc), 0)

def drawMidCircle3(xc, yc ,x, y,im):
    im.putpixel((y+xc, x+yc), 0)
    im.putpixel((-y+xc, x+yc), 0)
    im.putpixel((y+xc, -x+yc), 0)
    im.putpixel((-y+xc, -x+yc), 0)



def MidcircleBres(x_centre,y_centre,r)  :
    im = img.new(mode='1', size=(900,900),color=1)
    x = r
    y = 0

    # Printing the initial point the
    # axes after translation
    print("(", x + x_centre, ", ",
          y + y_centre, ")",
          sep="", end="")

    # When radius is zero only a single
    # point be printed
    if (r > 0):
        print("(", x + x_centre, ", ",
              -y + y_centre, ")",
              sep="", end="")
        print("(", y + x_centre, ", ",
              x + y_centre, ")",
              sep="", end="")
        print("(", -y + x_centre, ", ",
              x + y_centre, ")", sep="")
        drawMidCircle1(x_centre, y_centre,x,y, im)
        # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if (x < y):
            break

        # Printing the generated point its reflection
        # in the other octants after translation
        print("(", x + x_centre, ", ", y + y_centre,
              ")", sep="", end="")
        print("(", -x + x_centre, ", ", y + y_centre,
              ")", sep="", end="")
        print("(", x + x_centre, ", ", -y + y_centre,
              ")", sep="", end="")
        print("(", -x + x_centre, ", ", -y + y_centre,
              ")", sep="")
        drawMidCircle2(x_centre, y_centre,x,y, im)


        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            print("(", y + x_centre, ", ", x + y_centre,
                  ")", sep="", end="")
            print("(", -y + x_centre, ", ", x + y_centre,
                  ")", sep="", end="")
            print("(", y + x_centre, ", ", -x + y_centre,
                  ")", sep="", end="")
            print("(", -y + x_centre, ", ", -x + y_centre,
                  ")", sep="")
            drawMidCircle3(x_centre, y_centre, x, y, im)

            # Driver Code
    im.show()


MidcircleBres(500,400,300)