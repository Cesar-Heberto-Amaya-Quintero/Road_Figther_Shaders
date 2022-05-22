from OpenGL.GL import *
import glfw
import math

from Modelo import *
from numpy import dtype
import glm


class Pajaro(Modelo):
    angulo= 10
    fase = 90

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
       
        
        self.vertices = np.array(
            [
                (0.44 * 0.2) + 0.41, (-0.26 * 0.2) -0.2, 0.0, 1.0,  196/255, 96/255, 8/255, 1.0,  #izquierda, abajo
                (0.43 * 0.2) + 0.41, (-0.2 * 0.2) -0.2, 0.0, 1.0,     196/255, 96/255, 8/255, 1.0, #arriba
                (0.53 * 0.2) + 0.41, (-0.26 * 0.2) -0.2, 0.0, 1.0,    196/255, 96/255, 8/255, 1.0,   #derecha

                0.44 -0.08, -0.26 -0.022, 0.0, 1.0,  255/255, 255/255, 255/255, 1.0,  #izquierda, abajo
                0.45 -0.08, -0.2 -0.022, 0.0, 1.0,     255/255, 255/255, 255/255, 1.0, #arriba
                0.53 -0.08, -0.26 -0.022, 0.0, 1.0,    255/255, 255/255, 255/255, 1.0,   #derecha

                       
            ], dtype="float32"
        )

        for angulo in range(0, 359, 5):
            componente_x = 0.024 * math.cos(angulo * math.pi / 180) + 0.48 
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.25

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            255/255, 255/255, 255/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.05 * math.cos(angulo * math.pi / 180) + 0.43 
            componente_y = 0.03 * math.sin(angulo * math.pi / 180) - 0.25

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            255/255, 255/255, 255/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.43  
            componente_y = 0.07 * math.sin(angulo * math.pi / 180) - 0.25

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            255/255, 255/255, 255/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x =0.025 * math.cos(angulo * math.pi / 180) + 0.4 + 0.41
            componente_y =0.025 * math.sin(angulo * math.pi / 180) - 0.25  -0.19

            self.vertices = np.append(self.vertices, np.array([(componente_x * 0.2) + 0.33, (componente_y * 0.2) -0.16 , 0.0 , 1.0, 
                            0/255, 0/255, 0/255, 1.0 ], dtype="float32"))


        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def actualizar(self, tiempo_delta):

        cantidad_movimiento = 0.6 * tiempo_delta
        self.posicion.x = self.posicion.x + (math.cos((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )
        self.posicion.y = self.posicion.y + (math.sin((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )

        # posicion_pajaros[1][0] = posicion_pajaros[1][0] + (math.cos((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )
        # posicion_pajaros[1][1] = posicion_pajaros[1][1] - (math.sin((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )

        self.angulo = self.angulo + 0.2

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)


    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 3, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 6, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 78, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 150, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 222, 72)
        


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()