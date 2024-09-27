import cairo, math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5,0.5,0.5)
ctx.paint()

# Bezier curve
ctx.move_to(200, 200)
ctx.curve_to(300, 400, 370, 100, 470, 300)
ctx.set_source_rgb(0,0,0)
ctx. set_line_width(10)
ctx.stroke()

ctx.set_source_rgb(1,0,0)

ctx.move_to(200,200)
ctx.line_to(300, 380)
ctx.set_line_width(3)
ctx.stroke()

ctx.move_to(470,300)
ctx.line_to(380, 120)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(3)
ctx.stroke()

# 2 triangles

ctx.move_to(600, 200)
ctx.line_to(900, 200)
ctx.line_to(900, 370)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

ctx.move_to(600, 220)
ctx.line_to(600, 380)
ctx.line_to(880, 380)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

# Circle
ctx.arc(500,700, 200, 0, 2*math.pi)
ctx.set_source_rgb(0,0,0)
ctx.fill()

ctx.arc(500,700, 200, 0, math.pi/2)
ctx.set_source_rgb(0,1,0)
ctx.stroke()

ctx.move_to(500, 500)
ctx.line_to(500, 900)
ctx.stroke()

ctx.move_to(300, 700)
ctx.line_to(700, 700)
ctx.stroke()


surface.write_to_png('final_test.png')