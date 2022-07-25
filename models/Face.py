from models.Ilumination import Ilumination
from models.Vertex import Vertex
from .Edge import Edge
from .GeometricTransformation import GeometricTransformation as gt
class Face:
  def __init__(self, edges:list[Edge], material:float):
    self.edges = edges
    self.vertexes:list[Vertex] = []
    self.material = material

    for e in edges:
      self.vertexes.append(e.startVertex)
    
    self.centroid()    
    
  def normal(self) -> Vertex:
    return gt.planeEquation(self.vertexes[0], self.vertexes[1], self.vertexes[2])
  
  def centroid(self):
    max:Vertex = Vertex(self.vertexes[0].x,self.vertexes[0].y,self.vertexes[0].z)
    min:Vertex = Vertex(self.vertexes[0].x,self.vertexes[0].y,self.vertexes[0].z)
    
    for v in self.vertexes:
      if v.x > max.x:
        max.x = v.x
      
      if v.y > max.y:
        max.y = v.y
      
      if v.z > max.z:
        max.z = v.z
        
      if v.x < min.x:
        min.x = v.x
      
      if v.y < min.y:
        min.y = v.y
      
      if v.z < min.z:
        min.z = v.z

    self.center = Vertex((max.x+min.x)/2,(max.y+min.y)/2,(max.z+min.z)/2)
  
  def central_ilumination(self, ilumination:Ilumination, vrp:Vertex):
    normal = self.normal()
    self.ambient_light = ilumination.ambient_light
    self.light_vector = ilumination.unitVector(self.center)
    self.diffuse_light = ilumination.diffuse(self.light_vector, normal)
    self.specular_light = ilumination.specular(self.light_vector,self.center, normal)
    