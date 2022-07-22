from tkinter import *
from models.Vertex import Vertex
from models.Sphere import Sphere
from models.GeometricTransformation import GeometricTransformation as gt
from models.Scene import Scene


window = Tk()
window.title('Computação gráfica: modelagem de cenas')


sphere = Sphere(200, 8, 8)

# for vertex in sphere.vertexes:
#   print(vertex.coordinatesXYZ())
  # gt.translation(vertex, Vertex(400, 300, 1))

VRP = Vertex(0, 0, 250)
focalPoint = Vertex(0, 0, 245)
viewUp = Vertex(0, 1, 0)
dp = 295

# minWindow=Vertex(-400, -300, 1)
# maxWindow=Vertex(400, 300, 1)
# minView=Vertex(0, 0, 0)
# maxView=Vertex(800, 600, 1)

minWindow=Vertex(-400, -300, 1)
maxWindow=Vertex(400, 300, 1)
minView=Vertex(0, 0, 0)
maxView=Vertex(800, 600, 0)

canvas = Canvas(window, width=maxView.x, height= maxView.y)
canvas.pack()
# vertexMinWindow, vertexMaxWindow, vertexMinView, vertexMaxView, vrp, focalPoint, viewUp,dp, canvas
scene = Scene(minWindow,maxWindow,minView,maxView,VRP,focalPoint,viewUp,dp,canvas)

scene.AddObject(sphere)

scene.Draw()

window.mainloop()