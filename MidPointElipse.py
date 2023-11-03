
from PIL import Image as img

def PixelIn(x,y,xc,yc,im):
	im.putpixel((x+xc, y+yc), 0) #1st q
	im.putpixel((-x+xc, y+yc), 0)#2nd q
	im.putpixel((x+xc, -y+yc), 0) #3rd q
	im.putpixel((-x+xc, -y+yc), 0) #4th q

def ROUND(a):
	return int(a+0.5)

def midptellipse(rx, ry, xc, yc):
	im = img.new(mode='1', size=(1000, 1000), color=1)
	x = 0
	y = ry
	# Initial decision parameter of region 1
	d1 = ((ry * ry) - (rx * rx * ry) +
		  (0.25 * rx * rx))
	dx = 2 * ry * ry * x
	dy = 2 * rx * rx * y
	# For region 1
	while (dx < dy):
		# Print points based on 4-way symmetry
		print("(", x + xc, ",", y + yc, ")")
		print("(", -x + xc, ",", y + yc, ")")
		print("(", x + xc, ",", -y + yc, ")")
		print("(", -x + xc, ",", -y + yc, ")")
		PixelIn(x,y,xc,yc,im)
		# Checking and updating value of
		# decision parameter based on algorithm
		if (d1 < 0):
			x += 1
			dx = dx + (2 * ry * ry)
			d1 = d1 + dx + (ry * ry)
		else:
			x += 1
			y -= 1
			dx = dx + (2 * ry * ry)
			dy = dy - (2 * rx * rx)
			d1 = d1 + dx - dy + (ry * ry)

		# Decision parameter of region 2
	d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
		  ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))

	# Plotting points of region 2
	while (y >= 0):

		# printing points based on 4-way symmetry
		print("(", x + xc, ",", y + yc, ")")
		print("(", -x + xc, ",", y + yc, ")")
		print("(", x + xc, ",", -y + yc, ")")
		print("(", -x + xc, ",", -y + yc, ")")
		PixelIn(x,y,xc,yc,im)

		# Checking and updating parameter
		# value based on algorithm
		if (d2 > 0):
			y -= 1
			dy = dy - (2 * rx * rx)
			d2 = d2 + (rx * rx) - dy
		else:
			y -= 1
			x += 1
			dx = dx + (2 * ry * ry)
			dy = dy - (2 * rx * rx)
			d2 = d2 + dx - dy + (rx * rx)
	# Driver code
	im.show()


# To draw a ellipse of major and
# minor radius 15, 10 centred at (50, 50)
midptellipse(100, 150, 500, 500)
