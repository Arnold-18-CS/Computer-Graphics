import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.paint()

# A bezier cureve is a versatile curve
# Has 4 points, 2 anchors at the ends, and 2 controls to
# control the curveof the anchors

ctx.move_to(100,150) # set up first anchor point
ctx.curve_to(200,100,400,300,500,200) # set up control points then final anchor
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(5)
ctx.stroke()

ctx.move_to(400,400) # set up first anchor point
ctx.curve_to(200,300,100,500,100,200) # set up control points then final anchor
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('bezier_curve.png')