from OpenGL.GL import *
import glfw
import math

from Modelo import *
from numpy import dtype
import glm


class CosasGameOver(Modelo):
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        
        
        self.vertices = np.array(
            [
                #FONDO
                -1,1,0.0,1.0,  0, 0, 0,1.0,  #izquierda, abajo
                -1,-1,0.0,1.0,     0, 0, 0,1.0, #arriba
                1,1,0.0,1.0,    0, 0, 0,1.0, #derecha
                1,-1,0.0,1.0,    0, 0, 0,1.0, #derecha

                #PALABRA GAME
                #G
                0.1 -0.5 , 0.1 + 0.5,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo
                0.1 -0.5, -0.2 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.13 -0.5, 0.1 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.13 -0.5, -0.2+ 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha

                #ROTADO
                -0.1 -0.3, 0.13 + 0.5,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo #4
                -0.1 -0.3, 0.1 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba # 1
                0.1 -0.3, 0.13 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 3
                0.1 -0.3, 0.1 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 2

        #             0.1, -0.1, 0.0) -0.1, 0.1
        # glVertex3f(0.1, 0.1, 0.0)   0.1, 0.1
        # glVertex3f(0.13, 0.1, 0.0) 0.1, 0.13
        # glVertex3f(0.13, -0.1, 0.0)  -0.1, 0.13

                #ROTADO
                -0.1 -0.3, 0.13 + 0.2,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo    
                -0.1 -0.3, 0.1 + 0.2,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.1 -0.3, 0.13 + 0.2,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.1 -0.3, 0.1 + 0.2,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha

                0.1 -0.32 , 0.06 + 0.4,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo
                0.1 -0.32, -0.1 + 0.4,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.13 -0.32, 0.06 + 0.4,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.13 -0.32, -0.1+ 0.4,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha

                #ROTADO
                -0.05 -0.27, 0.13 + 0.36,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo #4
                -0.05 -0.27, 0.1 + 0.36,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba # 1
                0.08 -0.27, 0.13 + 0.36,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 3
                0.08 -0.27, 0.1 + 0.36,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 2

                #A
                0.1 - 0.2, 0.1 + 0.5, 0.0, 1.0,     1.0, 0.0, 0.0,1.0,
                0.1 - 0.2, -0.2 + 0.5, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, 
                0.13 - 0.2, 0.1 + 0.5, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, 
                0.13 - 0.2, -0.2 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0,  

                0.1 - 0.03, 0.1 + 0.5, 0.0,  1.0,   1.0, 0.0, 0.0,1.0,
                0.1 - 0.03, -0.2 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, 
                0.13 - 0.03, 0.1 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, 
                0.13 - 0.03, -0.2 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0,  

                #ROTADO
                -0.1, 0.13 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                -0.1, 0.1 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.1, 0.13 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #derecha
                0.1, 0.1 + 0.5,0.0,1.0,      1.0, 0.0, 0.0,1.0, #derecha

                -0.1, 0.13 + 0.35,0.0,1.0,   1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                -0.1, 0.1 + 0.35,0.0,1.0,    1.0, 0.0, 0.0,1.0, #arriba
                0.1, 0.13 + 0.35,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.1, 0.1 + 0.35,0.0,1.0,     1.0, 0.0, 0.0,1.0, #derecha

                #M
                0.1 + 0.1, 0.1 + 0.5, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                0.1 + 0.1, -0.2 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #arriba
                0.13 + 0.1, 0.1 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #derecha
                0.13 + 0.1, -0.2 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #derecha

                #ROTADO
                -0.1 + 0.3, 0.13 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                -0.1 + 0.3, 0.1 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #arriba
                0.1 + 0.3, 0.13 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #derecha
                0.1 + 0.3, 0.1 + 0.5, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #derecha

                0.1 + 0.27, 0.1 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                0.1 + 0.27, -0.2 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #arriba
                0.13 + 0.27, 0.1 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #derecha
                0.13 + 0.27, -0.2 + 0.5, 0.0, 1.0, 1.0, 0.0, 0.0,1.0, #derecha

                0.1 + 0.19, 0.1 + 0.5, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                0.1 + 0.19, -0.2 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #arriba
                0.13 + 0.19, 0.1 + 0.5, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #derecha
                0.13 + 0.19, -0.2 + 0.5, 0.0, 1.0, 1.0, 0.0, 0.0,1.0, #derecha

                #E
                0.1 + 0.4, 0.1 + 0.5,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo
                0.1 + 0.4,  -0.2 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.13 + 0.4, 0.1 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.13 + 0.4, -0.2 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                
                #ROTADO
                -0.09 + 0.59, 0.13 +0.2,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo #4
                -0.09  + 0.59, 0.1 +0.2,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba # 1
                0.1 + 0.59, 0.13 +0.2,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 3
                0.1 + 0.59, 0.1 +0.2,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 2

                -0.03 + 0.55, 0.13 -0.15 + 0.5,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo #4
                -0.03  + 0.55, 0.1 -0.15 + 0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba # 1
                0.1 + 0.55, 0.13 -0.15 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 3
                0.1 + 0.55, 0.1 -0.15 + 0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 2

                -0.09 + 0.59, 0.13 +0.5,0.0,1.0,  1.0, 0.0, 0.0,1.0,  #izquierda, abajo #4
                -0.09  + 0.59, 0.1 +0.5,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba # 1
                0.1 + 0.59, 0.13 +0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 3
                0.1 + 0.59, 0.1 +0.5,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha # 2
                
                # LETRAS OVER
                #LETRA O
                0.1 - 0.47, 0.1, 0.0, 1.0,    1.0, 0.0, 0.0, 1.0, #izquierda, abajo
                0.1 - 0.47,  -0.2, 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #arriba
                0.13 - 0.47, 0.1, 0.0, 1.0,   1.0, 0.0, 0.0, 1.0, #derecha
                0.13 - 0.47, -0.2, 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #derecha

                0.1 - 0.3, 0.1 , 0.0, 1.0,    1.0, 0.0, 0.0, 1.0, #izquierda, abajo
                0.1 - 0.3,  -0.2 , 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #arriba
                0.13 - 0.3, 0.1 , 0.0, 1.0,   1.0, 0.0, 0.0, 1.0, #derecha
                0.13 - 0.3, -0.2 , 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #derecha

                #ROTADO
                -0.1 -0.27, 0.13, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                -0.1 -0.27, 0.1, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #arriba
                0.1 - 0.27, 0.13, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #derecha
                0.1 - 0.27, 0.1, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #derecha

                #ROTADO
                -0.1 - 0.27, 0.13 - 0.3, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #izquierda, abajo    
                -0.1 - 0.27, 0.1 - 0.3, 0.0, 1.0,   1.0, 00.0, 0.0,1.0, #arriba
                0.1 - 0.27, 0.13 - 0.3, 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #derecha
                0.1 - 0.27, 0.1 - 0.3, 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #derecha

                # LETRA V
                0.01 -0.14, 0.24 -0.1,0.0,1.0,       1.0, 0.0, 0.0,1.0,  #izquierda, abajo
                0.14 -0.14, -0.1 -0.1,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.04 -0.14, 0.25 -0.1,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                0.17 -0.14, -0.09 -0.1,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha

                0.01 + 0.11 , 0.25 -0.1,0.0,1.0,       1.0, 0.0, 0.0,1.0,  #izquierda, abajo
                -0.12 + 0.11, -0.09 -0.1,0.0,1.0,     1.0, 0.0, 0.0,1.0, #arriba
                0.04 + 0.11, 0.24 -0.1,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha
                -0.09 + 0.11, -0.1 -0.1,0.0,1.0,    1.0, 0.0, 0.0,1.0, #derecha

                #LETRA E
                0.1 + 0.1, 0.1 , 0.0, 1.0,    1.0, 0.0, 0.0,1.0, #izquierda, abajo
                0.1 + 0.1, -0.2 , 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #arriba
                0.13 + 0.1, 0.1 , 0.0, 1.0,   1.0, 0.0, 0.0,1.0, #derecha
                0.13 + 0.1, -0.2, 0.0, 1.0,  1.0, 0.0, 0.0,1.0, #derecha
                
                #ROTADO
                -0.09 + 0.29 , 0.13 - 0.3, 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #izquierda, abajo #4
                -0.09 + 0.29, 0.1 - 0.3, 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #arriba # 1
                0.1 + 0.29, 0.13 - 0.3, 0.0, 1.0,    1.0, 0.0, 0.0, 1.0, #derecha # 3
                0.1 + 0.29, 0.1 - 0.3, 0.0, 1.0,     1.0, 0.0, 0.0, 1.0, #derecha # 2

                -0.03 + 0.25, 0.13 - 0.15 , 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #izquierda, abajo #4
                -0.03  + 0.25, 0.1 - 0.15 , 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #arriba # 1
                0.1 + 0.25, 0.13 - 0.15, 0.0, 1.0,    1.0, 0.0, 0.0, 1.0, #derecha # 3
                0.1 + 0.25, 0.1 - 0.15, 0.0, 1.0,     1.0, 0.0, 0.0, 1.0, #derecha # 2

                -0.09 + 0.29, 0.13 , 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, #izquierda, abajo #4
                -0.09  + 0.29, 0.1, 0.0, 1.0,  1.0, 0.0, 0.0, 1.0, #arriba # 1
                0.1 + 0.29, 0.13 , 0.0, 1.0,   1.0, 0.0, 0.0, 1.0, #derecha # 3
                0.1 + 0.29, 0.1, 0.0, 1.0,     1.0, 0.0, 0.0, 1.0, #derecha # 2

                #R
                0.1 + 0.3, 0.1, 0.0, 1.0,     1.0, 1.0, 0.0,1.0,
                0.1 + 0.3, -0.2, 0.0, 1.0,    1.0, 1.0, 0.0,1.0, 
                0.13 + 0.3, 0.1, 0.0, 1.0,    1.0, 1.0, 0.0,1.0, 
                0.13 + 0.3, -0.2, 0.0, 1.0,   1.0, 1.0, 0.0,1.0,  

                0.1 + 0.47, 0.1, 0.0,  1.0,   1.0, 1.0, 0.0,1.0,
                0.1 + 0.47, -0.2, 0.0, 1.0,   1.0, 1.0, 0.0,1.0, 
                0.13 + 0.47, 0.1, 0.0, 1.0,   1.0, 1.0, 0.0,1.0, 
                0.13 + 0.47, -0.2, 0.0, 1.0,  1.0, 1.0, 0.0,1.0,  

                #ROTADO
                -0.1 + 0.5, 0.13, 0.0, 1.0,    1.0, 1.0, 0.0,1.0, #izquierda, abajo    
                -0.1 + 0.5, 0.1, 0.0, 1.0,     1.0, 1.0, 0.0,1.0, #arriba
                0.1 + 0.5, 0.13, 0.0, 1.0,     1.0, 1.0, 0.0,1.0, #derecha
                0.1 + 0.5, 0.1, 0.0, 1.0,      1.0, 1.0, 0.0,1.0, #derecha

                -0.1 + 0.5, 0.13 - 0.15, 0.0, 1.0,   1.0, 1.0, 0.0,1.0, #izquierda, abajo    
                -0.1 + 0.5, 0.1 - 0.15, 0.0, 1.0,    1.0, 1.0, 0.0,1.0, #arriba
                0.1 + 0.5, 0.13 - 0.15, 0.0, 1.0,    1.0, 1.0, 0.0,1.0, #derecha
                0.1 + 0.5, 0.1 - 0.15, 0.0, 1.0,     1.0, 1.0, 0.0,1.0, #derecha


                


                       
            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        # self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.translate(self.transformaciones,
        #         (-0.3, -0.2, 0.0))



    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        #LETRA G
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        #LETRA A
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        #LETRA M
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        #LETRA E
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 4)
        #LETRA O
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 4)
        #LETRA V
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 92, 4)
        #LETRA E
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 96, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 100, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 104, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 108, 4)
        #LETRA R
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 112, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 116, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 120, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 124, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 128, 4)


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()