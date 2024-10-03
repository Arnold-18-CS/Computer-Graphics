import cairo, math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5,0.5,0.5)
ctx.paint()

ctx.arc(500,700, 200, 0, 2*math.pi)
ctx.set_source_rgb(1,0,0.55)
ctx.fill()

A = [1,2,3,4]
B = A
B.append(100 )
print(A)
surface.write_to_png('computer_color.png')
