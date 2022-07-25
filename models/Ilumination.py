from .GeometricTransformation import GeometricTransformation as gt
from models.Vertex import Vertex


class Ilumination:
    # ka ambient coefficient, kd difision coefficient, ks specular coefficient 
    def __init__(self, lightSource:Vertex, lightIntensity:float, ambient_light:float, ka:float, kd:float, ks:float, vrp:Vertex):
        self.lightSource = lightSource
        self.lightIntensity = lightIntensity
        self.ka = ka
        self.kd = kd
        self.ks= ks
        self.ambient_light = 120 - ambient_light
        self.vrp = vrp
    
    def unitVector(self, vertex:Vertex) -> Vertex:
        l = gt.vector(vertex, self.lightSource)
        return l.unit()

    def diffuse(self, lightUnit:Vertex, normal:Vertex) -> float:
        angle = gt.dotProduct(normal,lightUnit)
        if angle < 0:
            return 0

        return self.lightIntensity*self.kd*angle

    def specular(self, lightUnit:Vertex, center:Vertex, normal:Vertex):
        product = 2*(gt.dotProduct(lightUnit,normal))
        xReflection = (product*normal.x)-lightUnit.x
        yReflection = (product*normal.y)-lightUnit.y
        zReflection = (product*normal.z)-lightUnit.z
        reflection = Vertex(xReflection, yReflection, zReflection)

        specular = gt.vector(center,self.vrp)
        specularReflection = gt.dotProduct(reflection,specular.unit())
        if specularReflection < 0:
            return 0
        
        return self.lightIntensity*self.ks*specularReflection
    
    def total(self, normal:Vertex, vertex:Vertex):
        light_vector = self.unitVector(vertex)
        diffuse_light = self.diffuse(light_vector, normal)
        specular_light = self.specular(light_vector,vertex, normal)
        
        return self.ambient_light+diffuse_light+specular_light
