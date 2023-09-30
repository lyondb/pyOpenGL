from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from core.texture import Texture
from geometry.geometry import Geometry
from material.textureMaterial import TextureMaterial
from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry
from extras.movementRig import MovementRig

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera  = Camera( aspectRatio=800/600 )
        self.camera.setPosition( [0, 0, 7] )

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition([0, 1, 4])
        skyGeometry = SphereGeometry(radius=50)
        skyMaterial = TextureMaterial(Texture("imgs/sky1.jpg") )
        sky = Mesh(skyGeometry, skyMaterial)
        self.scene.add(sky)
        grassGeometry = RectangleGeometry(width=800,height=100)
        grassMaterial = TextureMaterial(Texture("imgs/grass.jpg") )
        grass = Mesh(grassGeometry, grassMaterial)
        grass.rotateX(-3.14 / 2)
        self.scene.add(grass)

    def update(self):
        ##self.mesh.rotateY(0.0514)
        ##self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)
        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()