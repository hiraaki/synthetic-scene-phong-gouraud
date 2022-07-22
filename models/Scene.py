from models.Face import Face
from models.GeometricTransformation import GeometricTransformation as gt
from models.Sphere import Sphere
from models.Vertex import Vertex

class Scene:
    def __init__(self,vertexMinWindow:Vertex, vertexMaxWindow:Vertex, vertexMinView:Vertex, vertexMaxView:Vertex, vrp:Vertex, focalPoint:Vertex, viewUp,dp, canvas):
        self.canvas = canvas
        self.vertexMinWindow = vertexMinWindow
        self.vertexMaxWindow = vertexMaxWindow 
        self.vertexMinView = vertexMinView
        self.vertexMaxView=vertexMaxView
        self.dp=dp
        self.faces = []
        self.edges = []
        self.vertexes = []
        self.viewUp = viewUp
        self.vrp = vrp
        self.focalPoint = focalPoint        
    
    def AddObject(self, object:Sphere):
        for f in object.faces:
            self.faces.append(f)

        for e in object.edges:
            self.edges.append(e)

        for v in object.vertexes:
            self.vertexes.append(v)

     # stru2srt composted matriz multiplication linearization
    # {{j1,0,0,j2},{0,j3,0,j4},{0,0,1,0},{0,0,0,1}}*{{1,0,0,0},{0,1,0,0},{0,0,p1,p2},{0,0,p3,p4}}*{{r1,r2,r3,r4},{r5,r6,r7,r8},{r9,r10,r11,r12},{0,0,0,1}}
    # j1 r1 + j2 p3 r9 | j1 r2 + j2 p3 r10 | j1 r3 + j2 p3 r11 | j1 r4 + j2 p3 r12 + j2 p4
    # j3 r5 + j4 p3 r9 | j3 r6 + j4 p3 r10 | j3 r7 + j4 p3 r11 | j3 r8 + j4 p3 r12 + j4 p4
    # p1 r9 | p1 r10 | p1 r11 | p1 r12 + p2
    # p3 r9 | p3 r10 | p3 r11 | p3 r12 + p4
    def sruToSrt(self, vertexes, n, v, u, vrpT):   
        r1,r2,r3 = u.coordinatesXYZ()
        r4 = -self.vrp.x
        r5,r6,r7 = v.coordinatesXYZ()
        r8 = -self.vrp.y
        r9,r10,r11 = n.coordinatesXYZ()
        r12 = -self.vrp.z

        p1,p2,p3,p4=1,0,-1/self.dp,1

        j1=(self.vertexMaxView.x-self.vertexMinView.x)/(self.vertexMaxWindow.x-self.vertexMinWindow.x)
        j2=(-self.vertexMinWindow.x*j1)+self.vertexMinView.x
        j3=(self.vertexMinView.y-self.vertexMaxView.y)/(self.vertexMaxWindow.y-self.vertexMinWindow.y)
        j4=(self.vertexMinWindow.y*j3)+self.vertexMinView.y

        for v in vertexes:            
            x = (((j1*r1) + (j2*p3*r9))*v.x) + (((j1*r2) + (j2*p3*r10))*v.y) + (((j1*r3) + (j2*p3*r11))*v.z) + ((j1*r4) + (j2*p3*r12) + (j2*p4))
            y = (((j3*r5) + (j4*p3*r9))*v.x) + (((j3*r6) + (j4*p3*r10))*v.y) + (((j3*r7) + (j4*p3*r11))*v.z) + ((j3*r8) + (j4*p3*r12) + (j4*p4))
            z = ((p1*r9)*v.x) + ((p1*r10)*v.y) + ((p1*r11)*v.z) + ((p1*r12) + p2)
            u = ((p3*r9)*v.x) + ((p3*r10)*v.y) + ((p3*r11)*v.z) + ((p3*r12) + p4)
            v.x,v.y,v.z=x/u,y/u,z/u
            

    def Draw(self):
        normal = gt.calculateNormalVector(self.vrp,self.focalPoint)
        viewUp = gt.calculateViewUpVector(normal,self.viewUp)
        projection = gt.crossProduct(viewUp, normal)
        vrpT = Vertex(gt.dotProduct(self.vrp,normal), gt.dotProduct(self.vrp,viewUp), gt.dotProduct(self.vrp,projection))

        self.sruToSrt(self.vertexes, n=normal, v=viewUp, u=projection, vrpT=vrpT)

        for v in self.vertexes:
            print(v.coordinatesXYZ())

        for e in self.edges:
            self.canvas.create_line(e.startVertex.coordinatesXY(), e.endVertex.coordinatesXY())                
            