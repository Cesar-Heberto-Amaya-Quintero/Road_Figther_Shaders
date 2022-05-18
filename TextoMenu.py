from OpenGL.GL import *
import glfw
import math

from Modelo import *
from numpy import dtype
import glm


class TextoMenu(Modelo):
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        
        self.vertices = np.array(
            [
                #LETRA E
                0.1, 0.1, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                0.1, -0.2, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #arriba
                0.13, 0.1, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.13, -0.2, 0.0, 1.0,     1.0, 1.0, 1.0,1.0, #derecha

                #ROTADO
                -0.09 + 0.2 , 0.13 -0.3, 0.0, 1.0,        1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.2 , 0.1 -0.3, 0.0, 1.0,          1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.2, 0.13 - 0.3 , 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.2, 0.1 - 0.3, 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 2

                -0.03 + 0.15, 0.13 - 0.15 , 0.0, 1.0,  1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.03 + 0.15, 0.1 - 0.15 , 0.0, 1.0,  1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.15, 0.13 - 0.15, 0.0, 1.0,    1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.15, 0.1 - 0.15, 0.0, 1.0,     1.0, 1.0, 1.0, 1.0, #derecha # 2

                -0.09 + 0.19, 0.13 , 0.0, 1.0,        1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.19, 0.1, 0.0, 1.0,          1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.19, 0.13 , 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.19, 0.1, 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 2

                #LETRA N
                0.1 + 0.21, 0.13, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                0.1 + 0.21, -0.2, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #arriba
                0.13 + 0.21, 0.13, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.13 + 0.21, -0.2, 0.0, 1.0,     1.0, 1.0, 1.0,1.0, #derecha 

                0 + 0.31, 0.25 -0.13, 0.0,1.0,       1.0, 1.0, 1.0,1.0,  #izquierda, abajo
                0.12 + 0.31, -0.07 -0.13, 0.0,1.0,     1.0, 1.0, 1.0,1.0, #arriba
                0.03 + 0.31, 0.26 -0.13, 0.0,1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.15 + 0.31, -0.06 -0.13, 0.0,1.0,    1.0, 1.0, 1.0,1.0, #derecha

                0.1 + 0.33, 0.13, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                0.1 + 0.33, -0.2, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #arriba
                0.13 + 0.33, 0.13, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.13 + 0.33, -0.2, 0.0, 1.0,     1.0, 1.0, 1.0,1.0, #derecha

                #LETRA T 
                0.1 + 0.45, 0.13, 0.0, 1.0,         1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                0.1 + 0.45, -0.2, 0.0, 1.0,       1.0, 1.0, 1.0,1.0, #arriba 
                0.13 + 0.45, 0.13, 0.0, 1.0,        1.0, 1.0, 1.0,1.0, #derecha 
                0.13 + 0.45, -0.2, 0.0, 1.0,      1.0, 1.0, 1.0,1.0, #derecha

                -0.09 + 0.56 , 0.13, 0.0, 1.0,        1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.56, 0.1, 0.0, 1.0,          1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.56, 0.13 , 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.56, 0.1, 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 2

                # LETRA E
                0.1 + 0.57, 0.1, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                0.1 + 0.57, -0.2, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #arriba
                0.13 + 0.57, 0.1, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.13 + 0.57, -0.2, 0.0, 1.0,     1.0, 1.0, 1.0,1.0, #derecha

                #ROTADO
                -0.09 + 0.77 , 0.13 -0.3, 0.0, 1.0,        1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.77 , 0.1 -0.3, 0.0, 1.0,          1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.77, 0.13 - 0.3 , 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.77, 0.1 - 0.3, 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 2

                -0.03 + 0.72, 0.13 - 0.15 , 0.0, 1.0,  1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.03 + 0.72, 0.1 - 0.15 , 0.0, 1.0,  1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.72, 0.13 - 0.15, 0.0, 1.0,    1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.72, 0.1 - 0.15, 0.0, 1.0,     1.0, 1.0, 1.0, 1.0, #derecha # 2

                -0.09 + 0.76, 0.13 , 0.0, 1.0,        1.0, 1.0, 1.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.76, 0.1, 0.0, 1.0,          1.0, 1.0, 1.0, 1.0, #arriba # 1
                0.1 + 0.76, 0.13 , 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 3
                0.1 + 0.76, 0.1, 0.0, 1.0,            1.0, 1.0, 1.0, 1.0, #derecha # 2

                #A
                0.1 - 0.2, 0.1 + 0.5, 0.0, 1.0,     1.0, 1.0, 1.0,1.0,
                0.1 - 0.2, -0.2 + 0.5, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, 
                0.13 - 0.2, 0.1 + 0.5, 0.0, 1.0,    1.0, 1.0, 1.0,1.0, 
                0.13 - 0.2, -0.2 + 0.5, 0.0, 1.0,   1.0, 1.0, 1.0,1.0,  

                0.1 - 0.03, 0.1 + 0.5, 0.0,  1.0,   1.0, 1.0, 1.0,1.0,
                0.1 - 0.03, -0.2 + 0.5, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, 
                0.13 - 0.03, 0.1 + 0.5, 0.0, 1.0,   1.0, 1.0, 1.0,1.0, 
                0.13 - 0.03, -0.2 + 0.5, 0.0, 1.0,  1.0, 1.0, 1.0,1.0,  

                #ROTADO
                -0.1, 0.13 + 0.5,0.0,1.0,    1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                -0.1, 0.1 + 0.5,0.0,1.0,     1.0, 1.0, 1.0,1.0, #arriba
                0.1, 0.13 + 0.5,0.0,1.0,     1.0, 1.0, 1.0,1.0, #derecha
                0.1, 0.1 + 0.5,0.0,1.0,      1.0, 1.0, 1.0,1.0, #derecha

                -0.1, 0.13 + 0.35,0.0,1.0,   1.0, 1.0, 1.0,1.0, #izquierda, abajo    
                -0.1, 0.1 + 0.35,0.0,1.0,    1.0, 1.0, 1.0,1.0, #arriba
                0.1, 0.13 + 0.35,0.0,1.0,    1.0, 1.0, 1.0,1.0, #derecha
                0.1, 0.1 + 0.35,0.0,1.0,     1.0, 1.0, 1.0,1.0, #derecha

            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.scale(self.transformaciones,
                (0.7, 0.7, 0.0))



    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        #LETRA E
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        #LETRA N
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        #LETRA T 
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        #LETRA E
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()