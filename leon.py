from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from geometry.geometry import Geometry
from geometry.lineGeometry import LineGeometry
from material.lineMaterial import LineMaterial

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera  = Camera( aspectRatio=800/600 )
        self.camera.setPosition( [0, 0, 2] )

        geometry = LineGeometry(0 , 0.85 , 0 , -0.25, 0.95, 0)

        material = LineMaterial({"useVertexColors": True} )
        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )


    def update(self):
        ##self.mesh.rotateY(0.0514)
        ##self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)
        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()