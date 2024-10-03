import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

coordinates = []
points = int(input("vertices: "))
og_points = points

while(points>0):
    x = int(input("x: "))
    y = int(input("y: "))
    print()
    A = [x,y]
    coordinates.append(A)
    points-=1

print(coordinates)

ctx.move_to(*coordinates[0])
print(*coordinates[0])
i = 1
while(og_points-1 > 0):
    ctx.line_to(*coordinates[i])
    i+=1
    og_points-=1

ctx.close_path()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png("polygon.png")
