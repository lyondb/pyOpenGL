from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from geometry.sphereGeometry import SphereGeometry
from material.material import Material
from math import sin
from numpy import arange

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera  = Camera( aspectRatio=800/600 )
        self.camera.setPosition( [0, 0, 7] )

        ##Creación de un nuevo material a partir de funciones enviados a los shaders
        geometry = SphereGeometry(radius=3)
        ##la palabra in indica que esa variable del código será enviada por la aplicación
        #la palabra out indica que esa variable será enviada al shader de fragmentos por el shader de vértices.
        #los tipos uniform indican que se recibirán las matrices que contienen las coordenadas de la escena, la vista
        #y la perspectiva, las cuales son matrices de 4x4. La posición de los puntos se calcula en Vscode, los colores
        #se calculan en fsCode.
        vsCode = """ 
            in vec3 vertexPosition; 
            out vec3 position; 
            uniform mat4 modelMatrix; 
            uniform mat4 viewMatrix; 
            uniform mat4 projectionMatrix; 
            void main() 
            {
                vec4 pos = vec4(vertexPosition, 1.0);
                gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
                position = vertexPosition; 
            } """
        fsCode = """ 
            in vec3 position;
            out vec4 fragColor; 
            void main() 
            {
                vec3 color = mod(position, 1.0);
                fragColor = vec4(color, 1.0); } """
        material = Material(vsCode, fsCode)
        material.locateUniforms()
        ##FIN DE LA DEFINICION
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.scene.rotateY(0.0514)
        self.scene.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)
        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()