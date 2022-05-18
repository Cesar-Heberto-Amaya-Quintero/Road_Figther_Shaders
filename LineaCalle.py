from OpenGL.GL import *
import glfw
import math

from Modelo import *
from numpy import dtype
import glm


class LineaCalle(Modelo):
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        
        
        self.vertices = np.array(
            [
                -0.015, 0.1, 0.0, 1.0,  215/255, 216/255, 217/255, 1.0,  #izquierda, abajo
                -0.015,-0.1, 0.0, 1.0,     215/255, 216/255, 217/255, 1.0, #arriba
                0.015,0.1, 0.0, 1.0,    215/255, 216/255, 217/255, 1.0,   #derecha
                0.015,-0.1,0.0, 1.0,      215/255, 216/255, 217/255, 1.0,

                -0.015, 0.1 + 1, 0.0, 1.0,  215/255, 216/255, 217/255, 1.0,  #izquierda, abajo
                -0.015,-0.1 + 1, 0.0, 1.0,     215/255, 216/255, 217/255, 1.0, #arriba
                0.015,0.1 + 1, 0.0, 1.0,    215/255, 216/255, 217/255, 1.0,   #derecha
                0.015,-0.1 + 1,0.0, 1.0,      215/255, 216/255, 217/255, 1.0,

                       
            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def actualizar(self, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        self.posicion.y = self.posicion.y - cantidad_movimiento
        
        self.posicion.y = self.posicion.y - (0.01 * tiempo_delta)

        if self.posicion.y < -1:
            self.posicion.y = 1
        
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)


    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()