import cairo
import math


surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.paint()

# Draw an arc
ctx.arc(0, 0, 150, 0, math.pi/2)
# We use radians where 2*math.pi is a full circle
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(5)
ctx.stroke()

# Drawing circles of descending radii
ctx.arc(300,200,150,0,2*math.pi)
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(5)
ctx.stroke()

ctx.arc(300,200,100,0,2*math.pi)
ctx.set_source_rgb(0.3,0.3,0.3)
ctx.fill_preserve()
ctx.set_source_rgb(0.3,0.3,0.3)
ctx.set_line_width(5)
ctx.stroke()

ctx.arc(300,200,50,0,2*math.pi)
ctx.set_source_rgb(1,1,1)
ctx.fill_preserve()
ctx.set_source_rgb(1,1,1)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('circles_and_arcs.png')