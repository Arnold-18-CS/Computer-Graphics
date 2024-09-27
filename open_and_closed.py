import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.paint()

# Drawing lines
ctx.move_to(100, 100) # setting start coordinate
ctx. line_to(500, 300) # setting other coordinates
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke() # a it is a line use stroke

# Closed polygon
ctx.move_to(50, 100)  # A
ctx.line_to(200,50)   # B
ctx.line_to(250, 300) # C
ctx.line_to(100,200)  # D
ctx.close_path() # adds a line btn last point and first point in path
ctx.set_source_rgb(1,1,0)
ctx.set_line_width(10)
ctx.stroke()

# Open polygon - decorative dividers, symbols, arrows
ctx.move_to(50, 200)
ctx.line_to(100, 200)
ctx.line_to(150, 250)
ctx.line_to(250, 150)
ctx.line_to(350, 250)
ctx.line_to(450, 150)
ctx.line_to(500, 200)
ctx.line_to(550, 200)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(5)
ctx.stroke()


surface.write_to_png('open_and_closed.png')
