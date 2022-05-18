from OpenGL.GL import *
# from glew_wish import *
import glfw
import math

from numpy import dtype
from Modelo import *
import glm


class Carro(Modelo):

    x = 0.0
    y = -0.8
    z = 0.0
    velocidad = 0.8
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4

        

        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_superior = 0.10
        self.extremo_inferior = 0.10
        self.vertices = np.array(
            [
                        
            ], dtype="float32"
        )

        #LLANTAS
        for angulo in range(0, 359, 5):
            componente_x = 0.01 * math.cos(angulo * math.pi / 180) -0.039
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) -.09

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        31/255, 31/255, 31/255, 1.0 ], dtype="float32")) 

        # self.vertices = np.append(self.vertices, np.array([0.0, 0.0, 0.0 , 1.0, 
        #                                                 31/255, 31/255, 31/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.01 * math.cos(angulo * math.pi / 180)  + 0.039
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) -.09

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        31/255, 31/255, 31/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.01 * math.cos(angulo * math.pi / 180)  - 0.039
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) -.08 + 0.11

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        31/255, 31/255, 31/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.01 * math.cos(angulo * math.pi / 180)  + 0.039
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) -.08 + 0.11

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        31/255, 31/255, 31/255, 1.0 ], dtype="float32"))

        #CUERPO DEL CARRO 

        self.vertices = np.append(self.vertices, np.array(
            [
                -0.04,0.055,0.0, 1.0,  140/255, 0/255, 0/255, 1.0,  #izquierda, abajo
                -0.04,-0.1,0.0, 1.0,     140/255, 0/255, 0/255, 1.0, #arriba
                0.04,0.055, 0.0, 1.0,    140/255, 0/255, 0/255, 1.0,   #derecha
                0.04,-0.1,0.0, 1.0,      140/255, 0/255, 0/255, 1.0,
                        
            ], dtype="float32"
        ))

        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180)
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) +.04

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        140/255, 0/255, 0/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) 
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) -.1

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        140/255, 0/255, 0/255, 1.0 ], dtype="float32"))

        self.vertices = np.append(self.vertices, np.array(
            [
                -0.027,0.0001 * 0.4, 0, 1.0,  15/255, 13/255, 9/255, 1.0,  #izquierda, abajo
                -0.034,+ 0.07 * 0.4, 0, 1.0,     15/255, 13/255, 9/255, 1.0, #arriba
                0.027,0.0001 * 0.4, 0, 1.0,    15/255, 13/255, 9/255, 1.0,   #derecha
                0.034,+0.07 * 0.4, 0, 1.0,      15/255, 13/255, 9/255, 1.0                         
            ], dtype="float32"
        ))

        self.vertices = np.append(self.vertices, np.array(
            [
                -0.027,-0.01996 -0.03, 0, 1.0,  15/255, 13/255, 9/255, 1.0,  #izquierda, abajo
                -0.034,- 0.048 -0.03, 0, 1.0,     15/255, 13/255, 9/255, 1.0, #arriba
                0.027,-0.01996 -0.03, 0, 1.0,    15/255, 13/255, 9/255, 1.0,   #derecha
                0.034,- 0.048 -0.03, 0, 1.0,      15/255, 13/255, 9/255, 1.0                          
            ], dtype="float32"
        ))



        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)

        
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id, self.x, self.y ,self.z, self.velocidad)
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def mover(self, direccion, tiempo_delta):
        cantidad_movimiento = glm.vec3(0,0,0)
        cantidad_movimiento = self.velocidad * tiempo_delta
        if direccion == self.ARRIBA:
            self.posicion.y = self.posicion.y + cantidad_movimiento
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - cantidad_movimiento
        elif direccion == self.DERECHA:
            self.posicion.x = self.posicion.x + cantidad_movimiento
        elif direccion == self.IZQUIERDA:
            self.posicion.x = self.posicion.x - cantidad_movimiento

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        # self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.translate(self.transformaciones,
        #         (0.0, -0.8, 0.0))
        

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        

        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 72, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 144, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 216, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 288, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 292, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 364, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 436, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 440, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def actualizar(self, window, tiempo_delta):
        

        estado_arriba = glfw.get_key(window, glfw.KEY_UP)
        estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
        estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

        if estado_arriba == glfw.PRESS:
            self.mover(self.ARRIBA, tiempo_delta)
        if estado_abajo == glfw.PRESS:
            self.mover(self.ABAJO, tiempo_delta)
        if estado_derecha == glfw.PRESS:
            self.mover(self.DERECHA, tiempo_delta)
        if estado_izquierda == glfw.PRESS:
            self.mover(self.IZQUIERDA, tiempo_delta)

        if self.posicion.x >= 0.35:
            self.posicion.x = 0.35

        if self.posicion.x <= -0.35:
            self.posicion.x = -0.35
        
        if self.posicion.y <= -0.90:
            self.posicion.y = -0.90

        if self.posicion.y >= 0.90:
            self.posicion.y = 0.90