# https://github.com/camdat/shapepaper
# Created by Nathan Tokala [camdat]

import Image, ImageDraw
from random import randint
import random
import aggdraw
import commands
# Change these two vars if you don't use 1920x1080
resx = 1920 
resy = 1080
# You MUST change this to at least use your prefered bgsetter 
command = "feh --bg-fill file.png"

# lots of random
shape = random.randint(0, 10)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
darkr = int(r*0.75)
darkg = int(g*0.75)
darkb = int(b*0.75)
# create a new image with random background colors
im = Image.new("RGBA", (resx*2,resy*2 ),(r, g, b, 255)  )
# init drawing
draw = aggdraw.Draw(im)
brush = aggdraw.Brush((darkr, darkg, darkb))
pen = aggdraw.Pen((darkr, darkg, darkb), 100)
# create lots of ifs for each shape and some rotations
if (shape == 0) or (shape == 7):
	triangle = Image.new('RGBA',(500, 500))
	draw = aggdraw.Draw(triangle)
	draw.polygon((0, 500, 250, 0, 500, 500), brush)
	draw.flush()
	if shape == 7:
		triangle = triangle.transpose(Image.ROTATE_180)
		im.paste(triangle, (resx-250, resy-250, resx+250, resy+250), triangle)
	else:
		im.paste(triangle, (resx-250, resy-250, resx+250, resy+250), triangle)
elif shape == 1:
        square = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(square)
        draw.polygon((0, 0, 500, 0, 500, 500, 0, 500), brush)
        draw.flush()
        im.paste(square, (resx-250, resy-250, resx+250, resy+250), square)
elif (shape == 2) or (shape == 8):
        rect = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(rect)
        draw.polygon((0, 100, 500, 100, 500, 400, 0, 400), brush)
        draw.flush()
        if shape == 8:
                rect = rect.transpose(Image.ROTATE_90)
                im.paste(rect, (resx-250, resy-250, resx+250, resy+250), rect)
        else:
        	im.paste(rect, (resx-250, resy-250, resx+250, resy+250), rect)
elif shape == 3:
        circle = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(circle)
        draw.ellipse((0, 0, 500, 500), brush)
        draw.flush()
        im.paste(circle, (resx-250, resy-250, resx+250, resy+250), circle)
elif shape == 4:
	cross = Image.new('RGBA',(500, 500))
	draw = aggdraw.Draw(cross)
	draw.line((0, 0, 500, 500), pen)
	draw.line((0, 500, 500, 0), pen)
	draw.flush()
	im.paste(cross, (resx-250, resy-250, resx+250, resy+250), cross)
elif shape == 5:
        plus = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(plus)
        draw.line((250, 0, 250, 500), pen)
        draw.line((0, 250, 500, 250), pen)
        draw.flush()
        im.paste(plus, (resx-250, resy-250, resx+250, resy+250), plus)
elif (shape == 6) or (shape == 9):
        pen = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(pen)
        draw.polygon((250, 0, 0, 220, 100, 500, 400, 500, 500, 220), brush)
        draw.flush()
        if shape == 9:
                pen = pen.transpose(Image.ROTATE_180)
                im.paste(pen, (resx-250, resy-250, resx+250, resy+250), pen)
        else:
        	im.paste(pen, (resx-250, resy-250, resx+250, resy+250), pen)
elif shape == 10:
        hex = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(hex)
        draw.polygon((140, 0, 0, 250, 140, 500, 360, 500, 500, 250, 360, 0), brush)        
	draw.flush()
        im.paste(hex, (resx-250, resy-250, resx+250, resy+250), hex)
# save file 
im.save("file.png", "PNG")  
print r,g,b,darkr,darkg,darkb
print shape
status, output = commands.getstatusoutput(command)  # status=0 if success
