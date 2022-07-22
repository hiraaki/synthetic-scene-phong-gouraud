from tkinter import *
from models.Vertex import Vertex
from models.Sphere import Sphere
from models.GeometricTransformation import GeometricTransformation as gt
from models.Scene import Scene


window = Tk()
window.title('Computação gráfica: modelagem de cenas')


sphere = Sphere(100, 3, 1)

# for vertex in sphere.vertexes:
#   print(vertex.coordinatesXYZ())
  # gt.translation(vertex, Vertex(400, 300, 1))

VRP = Vertex(0, 0, 200)
focalPoint = Vertex(0, 0, 100)
viewUp = Vertex(0, 1, 0)
dp = 200

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

# gt.calculateSRCVertexes(sphere.vertexes, VRP, focalPoint, viewUp)
# gt.calculateSRTVertexes(sphere.vertexes,minWindow, maxWindow, minView, maxView, focalPoint.z,dp)

# for edge in sphere.edges:
#   canvas.create_line(edge.startVertex.coordinatesXY(), edge.endVertex.coordinatesXY())
#   print(edge.startVertex.coordinatesXYZ(), edge.endVertex.coordinatesXYZ())

window.mainloop()

