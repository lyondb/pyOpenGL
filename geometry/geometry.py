from core.attribute import Attribute

class Geometry(object):
    def __init__(self):
        # Store Attribute objects,
        #  indexed by name of associated variable in shader.
        # Shader variable associations set up later
        #  and stored in vertex array object in Mesh.
        self.attributes = {}
        # number of vertices
        self.vertexCount = None

    def addAttribute(self, dataType, variableName, data):
        self.attributes[variableName] = Attribute(dataType, data)

    def countVertices(self):
        # number of vertices may be calculated from
        #  the length of any Attribute object's array of data
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)

    # transform the data in an attribute using a matrix
    def applyMatrix(self, matrix, variableName="vertexPosition"):
        oldPositionData = self.attributes[variableName].data
        newPositionData = []
        for oldPos in oldPositionData:
            # avoid changing list references
            newPos = oldPos.copy()
            # add homogeneous fourth coordinate
            newPos.append(1)
            # multiply by matrix
            newPos = matrix @ newPos
            # remove homogeneous coordinate
            newPos = list(newPos[0:3])
            # add to new data list
            newPositionData.append(newPos)
        self.attributes[variableName].data =  newPositionData
        # new data must be uploaded
        self.attributes[variableName].uploadData()

    # merge data from attributes of other geometry into this object;
    # requires both geometries to have attributes with same names

    def merge(self, otherGeometry):
        for variableName, attributeObject in self.attributes.items():
            attributeObject.data += otherGeometry.attributes[variableName].data
            # new data must be uploaded
            attributeObject.uploadData()
        # update the number of vertices
        self.countVertices()