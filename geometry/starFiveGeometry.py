from geometry.geometry import Geometry

class StarFiveGeometry(Geometry):
    def __init__(self,starLine = True, data = [ [0, 1, 0], [0.24, 0.26, 0],
                                [1, 0, 0], [0.29, -0.26, 0],
                                [0.69, -0.98, 0], [0, -0.58, 0],
                                [-0.69, -1, 0], [-0.4, -0.3, 0],
                                [-1.0, 0, 0], [-0.39, 0.31, 0]]):
        super().__init__()
        
        if len(data) < 10:
            raise Exception( "Faltan vertices") 
        if len(data) > 10:
            raise Exception( "Sobran vertices")
        
        C1 = [1, 0.1, 0]
        C2 = [0.8, 1, 0]
        C3 = [0, 0.4, 1]
        positionData = []
        colorData = []
        
        if starLine == True:
            positionData = [data[0], data[1], data[2],
                            data[3], data[4], data[5],
                            data[6], data[7], data[8],
                            data[9]]
            colorData = [C1, C2, C3,
                         C2, C1, C2,
                         C3, C2, C1,
                         C2]
        else :
            positionData = [data[9], data[0], data[1],
                            data[1], data[2], data[3],
                            data[3], data[4], data[5],
                            data[5], data[6], data[7],
                            data[7], data[8], data[9],
                            data[9], data[5], data[7],
                            data[9], data[3], data[5],
                            data[9], data[1], data[3]]
            colorData = [C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3,
                         C1, C2, C3]
        
        self.addAttribute("vec3","vertexPosition", positionData)
        self.addAttribute("vec3","vertexColor",colorData)
        self.countVertices()
        
        
        
        