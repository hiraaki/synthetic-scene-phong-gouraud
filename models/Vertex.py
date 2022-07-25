import math


class Vertex:
  def __init__(self, x:float, y:float, z:float):
    self.x = x
    self.y = y 
    self.z = z

  def coordinatesXY(self):
    return self.x,self.y

  def coordinatesXYZ(self):
    return self.x,self.y, self.z
  
  def module(self):
    return math.sqrt((pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)))

  def unit(self):
    mod = self.module()
    self.unit = Vertex(self.x/mod, self.y/mod, self.z/mod)
    return self.unit