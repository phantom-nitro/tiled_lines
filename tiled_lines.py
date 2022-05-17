from turtle import *
import random

setup(1080, 1080)

def tiling(x,y,s,l,mode = "straight"):
	#s = size, l = level of recursion
	#if level of recursion is 0 then we draw
	if l==0:

		if mode == "straight":

			#vertical
			if random.random() < 0.5:
				penup()
				goto(x, y+s)
				pendown()
				goto(x, y-s)

			#horizontal
			else:
				penup()
				goto(x-s, y)
				pendown()
				goto(x+s,y)

		elif mode == "diagonal":
			#top left to bottom right
			if random.random() < 0.5:
				penup()
				goto(x-s, y+s)
				pendown()
				goto(x+s, y-s)

			#bottom left to top right
			else:
				penup()
				goto(x-s, y-s)
				pendown()
				goto(x+s,y+s)

		elif mode == "both":

			randnum = random.random()

			#vertical
			if randnum > 0.75:
				penup()
				goto(x, y+s)
				pendown()
				goto(x, y-s)

			#horizontal
			elif randnum > 0.5:
				penup()
				goto(x-s, y)
				pendown()
				goto(x+s,y)


			#top left to bottom right
			elif randnum > 0.25:
				penup()
				goto(x-s, y+s)
				pendown()
				goto(x+s, y-s)

			#bottom left to top right
			elif randnum >0:
				penup()
				goto(x-s, y-s)
				pendown()
				goto(x+s,y+s)


	#split the screen and go to next level of recursion
	else:
		s /= 2
		l -= 1
		tiling(x-s,y+s,s,l,mode)
		tiling(x+s,y+s,s,l,mode)
		tiling(x-s,y-s,s,l,mode)
		tiling(x+s,y-s,s,l,mode)

width(3)
hideturtle()
tracer(False)
tiling(0,0,400, 5, mode = "diagonal")
tracer(True)

exitonclick()
