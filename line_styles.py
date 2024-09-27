import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.paint()

# Line caps
# Affect how the ends of the lines are drawn
# Either butt, square or round

# Setting up the line
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(20)

# Butt cap
ctx.move_to(100, 50)
ctx.line_to(500, 50)
ctx.set_line_cap(cairo.LINE_CAP_BUTT)
ctx.stroke()

# Square Cap
ctx.move_to(100, 100)
ctx.line_to(500, 100)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.stroke()

# Round cap
ctx.move_to(100, 150)
ctx.line_to(500, 150)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()


# Line joins
# Styles include miter, round, bevel

# Miter join >
ctx.move_to(100, 200)
ctx.line_to(180, 300)
ctx.line_to(50, 300)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.stroke()

# Round join )
ctx.move_to(240, 200)
ctx.line_to(370, 300)
ctx.line_to(240, 300)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

# Bevel join /
ctx.move_to(430, 200)
ctx.line_to(560, 300)
ctx.line_to(430, 300)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
ctx.stroke()

# Dashed lines
# Can be used for annotation

ctx. set_line_width(5)
ctx.move_to(100, 400)
ctx.line_to(500, 400)
ctx.set_dash([20])
ctx.stroke()


ctx.move_to(100, 420)
ctx.line_to(500, 420)
ctx.set_dash([20,10])
ctx.stroke()


ctx.move_to(50, 440)
ctx.line_to(550, 440)
ctx.set_dash([20,5,5,5])
ctx.stroke()

ctx.move_to(50, 460)
ctx.line_to(550, 460)
ctx.set_dash([5,5,10])
ctx.stroke()

ctx.set_line_cap(cairo.LINE_CAP_ROUND)

ctx.move_to(50, 480)
ctx.line_to(550, 480)
ctx.set_dash([0,20])
ctx.stroke()


surface.write_to_png('line_styles.png')
