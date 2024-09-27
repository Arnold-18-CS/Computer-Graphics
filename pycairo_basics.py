import cairo


# --------------------------- x-axis
# |
# |
# |
# |
# |
# |
# |
# y-axis

# Setting up a surface - first step
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600) 
# PARAMETERS: output type (ImageSurface == png)
# ,format, width, length

# Setup a brush aka context
context = cairo.Context(surface)
# takes the surface/canvas as argument
context.set_source_rgb(0.8, 0.8, 0.8)
# pick color of surface with rgb values
context.paint()
# set paint color on surface

# Draw an image
context.rectangle(50,50,100,240)
# give coordinates and dimensions
context.set_source_rgb(1,0,0)
# pick color of rectangle with rgb values
context.fill()
# set paint to fill rectangle

surface.write_to_png('basics_output.png')