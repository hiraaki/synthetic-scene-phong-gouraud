from tkinter import *
from models.Vertex import Vertex
from models.Sphere import Sphere
from models.GeometricTransformation import GeometricTransformation as gt
from models.Scene import Scene


window = Tk()
window.title('Computação gráfica: modelagem de cenas')


sphere = Sphere(150, 18, 18)

for vertex in sphere.vertexes:  
  gt.rotation(vertex, 45, "x")

VRP = Vertex(0, 0, 200)
focalPoint = Vertex(0, 0, 300)
viewUp = Vertex(0, 1, 0)
dp = focalPoint.z - gt.distanceTwoVertexes(VRP,focalPoint)/2

minWindow=Vertex(-400, -300, 1)
maxWindow=Vertex(400, 300, 1)
minView=Vertex(0, 0, 0)
maxView=Vertex(800, 600, 0)

canvas = Canvas(window, width=maxView.x, height= maxView.y)
canvas.pack()
# vertexMinWindow, vertexMaxWindow, vertexMinView, vertexMaxView, vrp, focalPoint, viewUp,dp, canvas
scene = Scene(minWindow,maxWindow,minView,maxView,VRP,focalPoint,viewUp,dp,canvas)

scene.AddObject(sphere)

# scene.DrawWireframe();
scene.DrawWireframeWithOclusion()

window.mainloop()