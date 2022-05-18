from OpenGL.GL import *
# from glew_wish import *
import glfw
import math

from numpy import dtype
from Modelo import *
import glm

from random import randint, random, seed, choice

seed(1)


class Enemigo(Modelo):

    contador_tiempo = 0.0


    posibles_posiciones = [-0.3, -0.25,-0.1, 0, 0.1, 0.25, 0.3]
    posibles_colores_enemigos = [[245/255, 215/255, 66/255], [66/255, 149/255, 245/255], [36/255, 171/255, 56/255], [72/255, 35/255, 122/255], [240/255, 41/255, 41/255]]

    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id, x, y, z, velocidad, direccion, activos, colorR, colorG, colorB):
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_superior = 0.09
        self.extremo_inferior = 0.09
        self.activos = activos
        self.direccion = direccion
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB
        self.posicion = glm.vec3(0,0,0)
        self.posicion.x = x
        self.posicion.y = y
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
                -0.04 ,0.055 ,0.0, 1.0,  self.colorR, self.colorG, self.colorB, 1.0,  #izquierda, abajo
                -0.04 ,-0.1 ,0.0, 1.0,     self.colorR, self.colorG, self.colorB, 1.0, #arriba
                0.04 ,0.055 , 0.0, 1.0,    self.colorR, self.colorG, self.colorB, 1.0,   #derecha
                0.04 ,-0.1 ,0.0, 1.0,      self.colorR, self.colorG, self.colorB, 1.0,
                        
            ], dtype="float32"
        ))

        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) 
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) +.04 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        self.colorR, self.colorG, self.colorB, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) 
            componente_y = 0.04 * math.sin(angulo * math.pi / 180) -.1 

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        self.colorR, self.colorG, self.colorB, 1.0 ], dtype="float32"))

        self.vertices = np.append(self.vertices, np.array(
            [
                -0.027 ,0.0001 * 0.4 , 0, 1.0,  15/255, 13/255, 9/255, 1.0,  #izquierda, abajo
                -0.034 ,+ 0.07 * 0.4 , 0, 1.0,     15/255, 13/255, 9/255, 1.0, #arriba
                0.027 ,0.0001 * 0.4 , 0, 1.0,    15/255, 13/255, 9/255, 1.0,   #derecha
                0.034 ,+0.07 * 0.4 , 0, 1.0,      15/255, 13/255, 9/255, 1.0                         
            ], dtype="float32"
        ))

        self.vertices = np.append(self.vertices, np.array(
            [
                -0.027 ,-0.01996 -0.03 , 0, 1.0,  15/255, 13/255, 9/255, 1.0,  #izquierda, abajo
                -0.034 ,- 0.048 -0.03 , 0, 1.0,     15/255, 13/255, 9/255, 1.0, #arriba
                0.027 ,-0.01996 -0.03 , 0, 1.0,    15/255, 13/255, 9/255, 1.0,   #derecha
                0.034 ,- 0.048 -0.03 , 0, 1.0,      15/255, 13/255, 9/255, 1.0                          
            ], dtype="float32"
        ))



        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id, x, y ,z, velocidad)

    def actualizar(self, tiempo_delta):

        self.contador_tiempo = self.contador_tiempo + tiempo_delta
        if self.contador_tiempo >= 1:
            self.contador_tiempo = self.contador_tiempo - 1.0
            self.velocidad = self.velocidad + 0.03

        
        if self.activos:
            cantidad_movimiento =self.velocidad * tiempo_delta
            if self.direccion == 0:
                self.posicion.y = self.posicion.y - cantidad_movimiento
                if self.posicion.y <= -2:
                    self.posicion.y = 1.2
                    posicion = self.posibles_posiciones[randint(0,6)]
                    self.posicion.x = posicion

                    # posible_color = randint(0,4)
                    colorR = self.posibles_colores_enemigos[randint(0,4)][0]
                    colorG = self.posibles_colores_enemigos[randint(0,4)][1]
                    colorB = self.posibles_colores_enemigos[randint(0,4)][2]
                    
                    self.colorR = colorR
                    self.colorG = colorG
                    self.colorB = colorB

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


    

