from .Vertex import Vertex
class Edge:
  def __init__(self, startVertex:Vertex, endVertex:Vertex):
    self.startVertex = startVertex
    self.endVertex = endVertex

  def calculateM(self):
    self.m = ( self.endVertex.y - self.startVertex.y) / (self.endVertex.x - self.startVertex.x)
