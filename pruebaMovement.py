from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from math import pi
from extras.movementRig import MovementRig
from extras.axesHelper import AxesHelper
from extras.gridHelper import GridHelper

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera  = Camera( aspectRatio=800/600 )
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0.5, 1, 5])
        self.scene.add(self.rig)
        axes = AxesHelper(axisLength=2)
        self.scene.add(axes)
        grid = GridHelper(size=20, gridColor=[1, 1, 1],
                          centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        self.scene.add(grid)

    def update(self):
        ##self.scene.rotateY(0.0514)
        ##self.scene.rotateX(0.0337)
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)

        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()