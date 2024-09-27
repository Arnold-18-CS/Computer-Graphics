import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.paint()

# Red rectangle - fill only
ctx.rectangle(50, 50, 150, 250)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

# Green rectangle - stroke only
ctx.rectangle(250, 50, 250, 150)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(5) # need to set a line width if using stoke
ctx.stroke()

# Blue square - fill and stroke
ctx. rectangle(550, 50, 100, 100)
ctx.set_source_rgb(0,0,1)
ctx.fill_preserve() # set to fill preserve to have fill then describe the stroke 
ctx.set_source_rgb(0,0,0) # set color for stroke separately
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('fillNstroke.png')