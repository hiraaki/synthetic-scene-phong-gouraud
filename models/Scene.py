from models.GeometricTransformation import GeometricTransformation as gt

class Scene:
    def __init__(self, vertexMinWindow, vertexMaxWindow, vertexMinView, vertexMaxView, dp):
        self.vertexMinWindow = vertexMinWindow
        self.vertexMaxWindow = vertexMaxWindow 
        self.vertexMinView = vertexMinView
        self.vertexMaxView=vertexMaxView
        self.dp=dp
        self.objects
        
    def convertion(self, vertexes, n, v, u, vrpT):   
        r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12=n.coordinatesXYZ(),vrpT.x,v.coordinatesXYZ(),vrpT.y,u.coordinatesXYZ(),vrpT.z
        p1,p2,p3,p4=1,1,-(1/self.dp),0
        j1=(self.vertexMaxView.x-self.vertexMinView.x)/(self.vertexMaxWindow.x-self.vertexMinWindow.x)
        j2=(-self.vertexMinWindow.x*j1)+self.vertexMinView.x
        j3=(self.vertexMinView.y-self.vertexMaxView.y)/(self.vertexMaxWindow.y-self.vertexMinWindow.y)
        j4=(self.vertexMinWindow.y*j3)+self.vertexMinView.y
        
        for v in vertexes:
            u=p3*r10*v.y+p3*r11*v.z+p3*r12+p3*r9*v.x+p4
            v.x=v.x*(j1*r1+j2*p3*r9)+v.y*(j1*r2+j2*p3*r10)+v.z*(j1*r3+j2*p3*r11)+j1*r4+j2*p3*r12+j2*p4
            v.y=v.y*(j3*r6+j4*p3*r10)+v.z*(j3*r7+j4*p3*r11)+v.x*(j3*r5+j4*p3*r9)+j3*r8+j4*p3*r12+j4*p4
            v.z=p1*r10*v.y+p1*r11*v.z+p1*r12+p1*r9*v.x+p2
            
            

