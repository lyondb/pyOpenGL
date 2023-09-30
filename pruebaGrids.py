from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from extras.axesHelper import AxesHelper
from extras.gridHelper import GridHelper
from math import pi

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera  = Camera( aspectRatio=800/600 )
        self.camera.setPosition( [0, 0, 7] )

        self.camera.setPosition([0.5, 1, 5])
        axes = AxesHelper(axisLength=2)
        self.scene.add(axes)
        grid = GridHelper(size=20, gridColor=[1, 1, 1],
                          centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        self.scene.add(grid)

    def update(self):
        ##self.scene.rotateY(0.0514)
        ##self.scene.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)

        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()