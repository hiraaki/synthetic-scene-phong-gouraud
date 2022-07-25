from .Vertex import Vertex
from .Edge import Edge
from .Face import Face
from .GeometricTransformation import GeometricTransformation as gt
class Sphere:
  def __init__(self, radius:float, meridians:int, parallels:int, material:float):    
    self.meridians = meridians
    self.parallels = parallels
    self.radius = radius
    self.faces:list[Face] = []
    self.edges:list[Edge] = []
    self.vertexes:list[Vertex] = []
    self.material:float = material

    self.shapeSphere()

  def shapeSphere(self):
    radiusVertex = Vertex(0, self.radius, 0)

    meridianVertexes = self.createMeridian(radiusVertex)
    meridiansList:list[list[Vertex]] = []
    
    for i in range(self.meridians):
      meridiansList.append(self.rotateMeridian(meridianVertexes))
    
    for meridian in meridiansList:
      self.vertexes.extend(meridian)
    
    for m in range(len(meridiansList)-1):
      self.bodySide(meridiansList[m], meridiansList[m+1])
    
    self.bodySide(meridiansList[len(meridiansList)-1], meridiansList[0])
    
    top = Vertex(0, self.radius, 0)
    self.vertexes.append(top)
    self.topSide(meridiansList, top)
    self.topFace(meridiansList[self.meridians-1][0], meridiansList[0][0],top)
    
    botton = Vertex(0, -self.radius, 0)
    self.vertexes.append(botton)
    self.bottonSide(meridiansList, botton)
    
    self.bottonFace(meridiansList[0][self.parallels-1], meridiansList[self.meridians-1][self.parallels-1], botton)

  def createMeridian(self, radiusVertex):
    vertexesArray = []
    parallelAngle = 180 / (self.parallels + 1)

    for n in range(self.parallels):
      rotationVertex = gt.rotation(radiusVertex, parallelAngle, 'z')
      vertexesArray.append(rotationVertex)

    return vertexesArray
  
  def rotateMeridian(self, vetexes:'list[list[Vertex]]'):
    meridians = []
    meridianAngle = 360 / self.meridians + 1
    for v in vetexes:
      rotationVertex = gt.rotation(v, meridianAngle, 'y')
      meridians.append(rotationVertex)
      
    return meridians
  
  def bodySide(self, startMeridian:'list[Vertex]', endMeridian:'list[Vertex]'):
    mSize = len(startMeridian) -1

    for p in range(mSize):     
      faceEdges:list[Vertex] = []
      faceEdges.append(Edge(startMeridian[p], startMeridian[p+1]))
      faceEdges.append(Edge(startMeridian[p+1], endMeridian[p+1]))
      faceEdges.append(Edge(endMeridian[p+1], endMeridian[p]))
      faceEdges.append(Edge(endMeridian[p], startMeridian[p]))

      self.faces.append(Face(faceEdges,self.material))
      self.edges.extend(faceEdges)

  def topSide(self, meridianList: 'list[Vertex]', top:Vertex):
    size = self.meridians -1
    for p in range(size):
      self.topFace(meridianList[p][0], meridianList[p+1][0], top)
  
  def topFace(self, start:Vertex, end:Vertex, top:Vertex):
    faceEdges:list[Edge] = []
    faceEdges.append(Edge(top,start))
    faceEdges.append(Edge(start,end))
    faceEdges.append(Edge(end,top))

    self.faces.append(Face(faceEdges,self.material))
    self.edges.extend(faceEdges)
  
  def bottonSide(self, meridianList: 'list[list[Vertex]]', botton:Vertex):
    size = self.meridians -1
    last = self.parallels -1
    for p in range(size):
      self.bottonFace(meridianList[p+1][last],meridianList[p][last],botton)
  
  def bottonFace(self, start:Vertex, end:Vertex, botton:Vertex):    
    faceEdges:list[Edge] = []
    faceEdges.append(Edge(end,botton))
    faceEdges.append(Edge(botton,start))
    faceEdges.append(Edge(start,end))
    
    self.faces.append(Face(faceEdges,self.material))
    self.edges.extend(faceEdges)
  