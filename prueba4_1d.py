from core.base  import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera  import Camera
from core.mesh  import Mesh
from geometry.cylinderGeometry import CylinderGeometry
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

        ##Creación de un nuevo material a partir del tiempo
        ##geometry = SphereGeometry(radius=3,radiusSegments=168, heightSegments=64)
        geometry = CylinderGeometry()
        ##la palabra in indica que esa variable del código será enviada por la aplicación
        #la palabra out indica que esa variable será enviada al shader de fragmentos por el shader de vértices.
        #los tipos uniform indican que se recibirán las matrices que contienen las coordenadas de la escena, la vista
        #y la perspectiva, las cuales son matrices de 4x4. La posición de los puntos se calcula en Vscode, los colores
        #se calculan en fsCode.
        vsCode = """ 
            uniform mat4 modelMatrix; 
            uniform mat4 viewMatrix; 
            uniform mat4 projectionMatrix; 
            in vec3 vertexPosition; 
            in vec3 vertexColor; 
            out vec3 color; 
            uniform float time; 
            void main() 
            {
                float offset = 0.2 * sin(8.0 * vertexPosition.x + time); 
                vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
                gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(pos, 1);
                color = vertexColor; 
            } """
        fsCode = """ 
            in vec3 color; 
            uniform float time; 
            out vec4 fragColor; 
            void main() 
            {
                float r = abs(sin(time));
                vec4 c = vec4(r, -0.5*r, -0.5*r, 0.0);
                fragColor = vec4(color, 1.0) + c; 
            } """



        material = Material(vsCode, fsCode)
        material.addUniform("float", "time", 0)
        material.locateUniforms()
        self.time = 0;
        ##FIN DE LA DEFINICION
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        ##self.scene.rotateY(0.0514)
        ##self.scene.rotateX(0.0337)
        self.time += 1 / 60
        self.mesh.material.uniforms["time"].data = self.time
        self.renderer.render(self.scene, self.camera)

        # instantiate this class and run the program
Test(screenSize=[800, 600]).run()