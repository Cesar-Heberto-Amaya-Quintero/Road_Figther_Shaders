from OpenGL.GL import *
import glfw
import math

from Modelo import *
from numpy import dtype
import glm


class CosasFondoEstaticas(Modelo):
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        
        
        self.vertices = np.array(
            [
                #CALLE
                -0.41,1.0,0.0,1.0,  64/255, 64/255, 64/255,1.0,  #izquierda, abajo
                -0.41,-1.0,0.0,1.0,     64/255, 64/255, 64/255,1.0, #arriba
                0.41,1.0,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha
                0.41,-1.0,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha

                -0.4,1.0,0.0,1.0,  93/255, 97/255, 94/255,1.0,  #izquierda, abajo
                -0.4,-1.0,0.0,1.0,     93/255, 97/255, 94/255,1.0, #arriba
                0.4,1.0,0.0,1.0,    93/255, 97/255, 94/255,1.0, #derecha
                0.4,-1.0,0.0,1.0,    93/255, 97/255, 94/255,1.0, #derecha

                # #AGUA
                -1,1,0.0,1.0,  41/255, 171/255, 226/255,1.0,  #izquierda, abajo
                -1,-1,0.0,1.0,     41/255, 171/255, 226/255,1.0, #arriba
                -0.6,1,0.0,1.0,    41/255, 171/255, 226/255,1.0, #derecha
                -0.6,-1,0.0,1.0,    41/255, 171/255, 226/255,1.0, #derecha

                #BARDA PARA EL AGUA
                -0.6,1,0.0,1.0,  64/255, 64/255, 64/255,1.0,  #izquierda, abajo
                -0.6,-1,0.0,1.0,     64/255, 64/255, 64/255,1.0, #arriba
                -0.56,1,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha
                -0.56,-1,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha

                #PARTE DE LA BARDA DEL AGUA
                -0.6,1,0.0, 1.0,       61/255, 61/255, 56/255,1.0,  #izquierda, abajo
                -0.6,-1,0.0,1.0,     61/255, 61/255, 56/255,1.0, #arriba
                -0.52,1,0.0,1.0,   61/255, 61/255, 56/255,1.0, #derecha
                -0.52,-1,0.0,1.0,    61/255, 61/255, 56/255,1.0, #derecha

                -0.55,1,0.0, 1.0,       1, 1, 1,1.0,  #izquierda, abajo
                -0.55,0.55,0.0,1.0,     1, 1, 1,1.0, #arriba
                -0.6,1,0.0,1.0,         1, 1, 1,1.0, #derecha
                -0.6,0.55,0.0,1.0,      1, 1, 1,1.0, #derecha

                -0.53,1,0.0, 1.0,       161/255, 161/255, 161/255,1.0,  #izquierda, abajo
                -0.53,0.55,0.0,1.0,     161/255, 161/255, 161/255,1.0, #arriba
                -0.55,1,0.0,1.0,         161/255, 161/255, 161/255,1.0, #derecha
                -0.55,0.55,0.0,1.0,      161/255, 161/255, 161/255,1.0, #derecha

                -0.55,1 -0.77,0.0, 1.0,       1, 1, 1,1.0,  #izquierda, abajo
                -0.55,0.55 -0.77,0.0,1.0,     1, 1, 1,1.0, #arriba
                -0.6,1 -0.77,0.0,1.0,         1, 1, 1,1.0, #derecha
                -0.6,0.55 -0.77,0.0,1.0,      1, 1, 1,1.0, #derecha

                -0.53 ,1 -0.77,0.0, 1.0,       161/255, 161/255, 161/255,1.0,  #izquierda, abajo
                -0.53,0.55 -0.77,0.0,1.0,     161/255, 161/255, 161/255,1.0, #arriba
                -0.55,1 -0.77,0.0,1.0,         161/255, 161/255, 161/255,1.0, #derecha
                -0.55,0.55 -0.77,0.0,1.0,      161/255, 161/255, 161/255,1.0, #derecha

                -0.55,1 -1.55,0.0, 1.0,       1, 1, 1,1.0,  #izquierda, abajo
                -0.55,0.55 -1.55,0.0,1.0,     1, 1, 1,1.0, #arriba
                -0.6,1 -1.55,0.0,1.0,         1, 1, 1,1.0, #derecha
                -0.6,0.55 -1.55,0.0,1.0,      1, 1, 1,1.0, #derecha

                -0.53,1 -1.55,0.0, 1.0,       161/255, 161/255, 161/255,1.0,  #izquierda, abajo
                -0.53,0.55 -1.55,0.0,1.0,     161/255, 161/255, 161/255,1.0, #arriba
                -0.55,1 -1.55,0.0,1.0,         161/255, 161/255, 161/255,1.0, #derecha
                -0.55,0.55 -1.55,0.0,1.0,      161/255, 161/255, 161/255,1.0, #derecha

                       
            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)



    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()