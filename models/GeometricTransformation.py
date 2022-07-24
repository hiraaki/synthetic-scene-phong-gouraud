import math
from re import X
from tokenize import Double, String

from .Vertex import Vertex

class GeometricTransformation:
    @staticmethod
    def rotation(vertex: Vertex, angle: float, axel: String):
        sen = math.sin(math.radians(angle))
        cos = math.cos(math.radians(angle))
        
        if axel == "x" :
            vertex.y, vertex.z = (vertex.z * sen) + (vertex.y * cos) ,(vertex.z * cos) - (vertex.y * sen)

        if axel == "y":
            vertex.x, vertex.z = (vertex.x * cos) + (vertex.z * sen), (vertex.z * cos) - (vertex.x*sen)

        if axel == "z":
            vertex.y, vertex.x = (vertex.x * sen) + (vertex.y * cos), (vertex.x * cos) - (vertex.y * sen)

        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def translation(vertex: Vertex, dest: Vertex):
        vertex.x,vertex.y,vertex.z = dest.x - vertex.x, dest.y - vertex.y, dest.z - vertex.z    
        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def scale(vertex: Vertex, size: Double):
        vertex.x,vertex.y,vertex.z = vertex.x*size, vertex.y*size, vertex.z*size
        return Vertex(vertex.x, vertex.y, vertex.z)

    @staticmethod
    def calculateNormalVector(VRP:Vertex,focalPoint:Vertex):
        normal = Vertex(
            VRP.x - focalPoint.x,
            VRP.y - focalPoint.y,
            VRP.z - focalPoint.z
        )   
        
        normalModule = math.sqrt((pow(normal.x, 2) + pow(normal.y, 2) + pow(normal.z, 2)))
        
        return Vertex(
            normal.x / normalModule,
            normal.y / normalModule,
            normal.z / normalModule,
        )
    
    @staticmethod
    def calculateViewUpVector(normalVector, viewUp):
        scalarProduct = (normalVector.x * viewUp.x) + (normalVector.y * viewUp.y) + (normalVector.z * viewUp.z)

        scalarVector = Vertex(
            viewUp.x - (scalarProduct * normalVector.x), 
            viewUp.y - (scalarProduct * normalVector.y), 
            viewUp.z - (scalarProduct * normalVector.z)
        )
        
        scalarModule = math.sqrt((pow(scalarVector.x, 2) + pow(scalarVector.y, 2) + pow(scalarVector.z, 2)))
        
        return Vertex(
            scalarVector.x / scalarModule,
            scalarVector.y / scalarModule,
            scalarVector.z / scalarModule
        )

    @staticmethod
    def crossProduct(a: Vertex, b:Vertex):
        return Vertex(
            (a.y*b.z)-(a.z*b.y),
            (a.z*b.x)-(a.x*b.z),
            (a.x*b.y)-(a.y*b.x)
        )

    @staticmethod
    def distanceTwoVertexes(a: Vertex, b: Vertex):
        return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2)+math.pow(a.z-b.z,2))
    
    @staticmethod
    def dotProduct(a: Vertex, b: Vertex):
        return (a.x*b.x)+(a.y*b.y)+(a.z*b.z)
    
    @staticmethod
    def planeEquation(p1:Vertex, p2:Vertex, p3:Vertex):
        dp3p2x = p3.x - p2.x
        dp3p2y = p3.y - p2.y
        dp3p2z = p3.z - p2.z
        
        dp1p2x = p1.x - p2.x
        dp1p2y = p1.y - p2.y
        dp1p2z = p1.z - p2.z

        a = (dp3p2y * dp1p2z) - (dp1p2y * dp3p2z)
        b = (dp3p2z * dp1p2x) - (dp1p2z * dp3p2x)
        c = (dp3p2x * dp1p2y) - (dp1p2x * dp3p2y)
        
        return Vertex(a,b,c)
