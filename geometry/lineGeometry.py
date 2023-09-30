from geometry.geometry import Geometry

class LineGeometry(Geometry):
    def __init__(self, startX=0, startY=0, startZ=1, endX=1, endY=1, endZ=1):
        super().__init__()
        P0 = [startX, startY, startZ]
        P1 = [ endX, endY, endZ]
        C1 = [1, 1, 1]
        positionData = [P0, P1]
        colorData = [C1, C1]
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()