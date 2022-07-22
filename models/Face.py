from .Edge import Edge
class Face:
  def __init__(self, edges):
    self.edges = edges
    self.vertexes = []
    for e in edges:
      self.vertexes.append([e.startVertex,e.endVertex])
