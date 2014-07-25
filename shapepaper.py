import Image, ImageDraw
from random import randint
import random
import aggdraw

resx = 1920 #Change these two vars if you dont use 1920x1080
resy = 1080

shape = random.randint(0, 4)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
darkr = int(r*0.75)
darkg = int(g*0.75)
darkb = int(b*0.75)

im = Image.new("RGBA", (resx*2,resy*2 ),(r, g, b, 255)  )

draw = aggdraw.Draw(im)
brush = aggdraw.Brush((darkr, darkg, darkb))
#delete if paint isnt used
p = aggdraw.Pen((darkr, darkg, darkb), 100)
#

if shape == 0:
	triangle = Image.new('RGBA',(500, 500))
	draw = aggdraw.Draw(triangle)
	draw.polygon((0, 500, 250, 0, 500, 500), brush)
	draw.flush()
	im.paste(triangle, (resx-250, resy-250, resx+250, resy+250), triangle)
elif shape == 1:
        square = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(square)
        draw.polygon((0, 0, 500, 0, 500, 500, 0, 500), brush)
        draw.flush()
        im.paste(square, (resx-250, resy-250, resx+250, resy+250), square)
elif shape == 2:
        rect = Image.new('RGBA',(500, 500))
        draw = aggdraw.Draw(rect)
        draw.polygon((0, 100, 500, 100, 500, 400, 0, 400), brush)
        draw.flush()
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
	draw.line((0, 0, 500, 500), p)
	draw.line((0, 500, 500, 0), p)
	draw.flush()
	im.paste(cross, (resx-250, resy-250, resx+250, resy+250), cross)

	 
im.save("file.png", "PNG")  
print r,g,b,darkr,darkg,darkb
print shape
