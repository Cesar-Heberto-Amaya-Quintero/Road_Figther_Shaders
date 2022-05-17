from Modelo import *
import glm

class Triangulo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.vertices = np.array(
            [
                -0.45,-0.1,0.0,1.0,  1.0,0.8,0.0,1.0,  #izquierda, abajo
                0.0,0.5,0.0,1.0,     0.0,1.0,0.0,1.0, #arriba
                0.5,-0.5,0.0,1.0,    0.0,0.0,1.0,1.0 #derecha
            ], dtype="float32"
        )
        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        # cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.ARRIBA:
            self.posicion.y = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

