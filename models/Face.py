from models.Vertex import Vertex
from .Edge import Edge
from .GeometricTransformation import GeometricTransformation as gt
class Face:
  def __init__(self, edges:list[Edge]):
    self.edges = edges
    self.vertexes:list[Vertex] = []
    for e in edges:
      self.vertexes.append(e.startVertex)

  def normal1(self) -> Vertex:
    return gt.planeEquation(self.vertexes[0], self.vertexes[1], self.vertexes[2])   
  
  def normal2(self) -> Vertex:
    if len(self.vertexes) >= 4:
      return gt.planeEquation(self.vertexes[1], self.vertexes[2], self.vertexes[3])
    return self.normal1()