class Vertex:
  def __init__(self, x:float, y:float, z:float):
    self.x = x
    self.y = y 
    self.z = z
  
  def coordinatesXY(self):
    return self.x,self.y

  def coordinatesXYZ(self):
    return self.x,self.y, self.z
  
