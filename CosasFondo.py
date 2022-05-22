from Modelo import *
import glm
import math

import numpy as np

class CosasFondo(Modelo):

    velocidad = 0.003
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.vertices = np.array(
            [   #BANQUETA
                0.41,0.1,0.0,1.0,  214/255, 162/255, 90/255,1.0,  #izquierda, abajo
                0.41,-0.1,0.0,1.0,     214/255, 162/255, 90/255,1.0, #arriba
                1.0,0.1,0.0,1.0,    214/255, 162/255, 90/255,1.0, #derecha
                1.0,-0.1,0.0,1.0,    214/255, 162/255, 90/255,1.0, #derecha

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

                #LINEAS AGUA
                -0.7,0.9,0.0,1.0,  166/255, 222/255, 237/255,1.0,  #izquierda, abajo
                -0.7,-1.5,0.0,1.0,     166/255, 222/255, 237/255,1.0, #arriba
                -0.68,0.9,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha
                -0.68,-1.5,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha

                -0.9,0,0.0,1.0,  166/255, 222/255, 237/255,1.0,  #izquierda, abajo
                -0.9,-1.8,0.0,1.0,     166/255, 222/255, 237/255,1.0, #arriba
                -0.88,0,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha
                -0.88,-1.8,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha

                -0.95,1.5,0.0,1.0,  166/255, 222/255, 237/255,1.0,  #izquierda, abajo
                -0.95,0.5,0.0,1.0,     166/255, 222/255, 237/255,1.0, #arriba
                -0.93,1.5,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha
                -0.93,0.5,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha

                -0.7,2.7,0.0,1.0,  166/255, 222/255, 237/255,1.0,  #izquierda, abajo
                -0.7,1.5,0.0,1.0,     166/255, 222/255, 237/255,1.0, #arriba
                -0.68,2.7,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha
                -0.68,1.5,0.0,1.0,    166/255, 222/255, 237/255,1.0, #derecha

                #TIERRA
                0.45, -0.15,0.0,1.0,  214/255, 162/255, 90/255,1.0,  #izquierda, abajo
                0.45, -0.75,0.0,1.0,     214/255, 162/255, 90/255,1.0, #arriba
                0.67,-0.15,0.0,1.0,    214/255, 162/255, 90/255,1.0, #derecha
                0.67, -0.75,0.0,1.0,    214/255, 162/255, 90/255,1.0, #derecha

                #BANCA
                0.52, -0.2,0.0,1.0,  82/255, 42/255, 19/255,1.0,  #izquierda, abajo
                0.52, -0.55,0.0,1.0,     82/255, 42/255, 19/255,1.0, #arriba
                0.62,-0.2,0.0,1.0,    82/255, 42/255, 19/255,1.0, #derecha
                0.62, -0.55,0.0,1.0,    82/255, 42/255, 19/255,1.0, #derecha

                0.5, -0.212,0.0,1.0,  82/255, 42/255, 19/255,1.0,  #izquierda, abajo
                0.5, -0.54,0.0,1.0,     82/255, 42/255, 19/255,1.0, #arriba
                0.6,-0.212,0.0,1.0,    82/255, 42/255, 19/255,1.0, #derecha
                0.6, -0.54,0.0,1.0,    82/255, 42/255, 19/255,1.0, #derecha

                #BOTE
                0.52, -0.58,0.0,1.0,  58/255, 58/255, 58/255,1.0,  #izquierda, abajo
                0.52, -0.7,0.0,1.0,     58/255, 58/255, 58/255,1.0, #arriba
                0.62,-0.58,0.0,1.0,    58/255, 58/255, 58/255,1.0, #derecha
                0.62, -0.7,0.0,1.0,    58/255, 58/255, 58/255,1.0, #derecha

                #BARDA PARA EL AGUA
                -0.6,1,0.0,1.0,  64/255, 64/255, 64/255,1.0,  #izquierda, abajo
                -0.6,-1,0.0,1.0,     64/255, 64/255, 64/255,1.0, #arriba
                -0.56,1,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha
                -0.56,-1,0.0,1.0,    64/255, 64/255, 64/255,1.0, #derecha

                #TRONCO
                -0.85, -0.3,0.0, 1.0,  0.32, 0.2, 0.11,1.0,  #izquierda, abajo
                -0.85, -0.5,0.0,1.0,     0.32, 0.2, 0.11,1.0, #arriba
                -0.95,-0.3,0.0,1.0,   0.32, 0.2, 0.11,1.0, #derecha
                -0.95, -0.5,0.0,1.0,    0.32, 0.2, 0.11,1.0, #derecha

                -0.88, -0.33, 0.0,1.0,       28/255, 23/255, 21/255,1.0,  #izquierda, abajo
                -0.88, -0.47,0.0,1.0,     28/255, 23/255, 21/255,1.0, #arriba
                -0.888,-0.33,0.0,1.0,   28/255, 23/255, 21/255,1.0, #derecha
                -0.888, -0.47,0.0,1.0,    28/255, 23/255, 21/255,1.0, #derecha

                -0.91, -0.33,0.0, 1.0,       28/255, 23/255, 21/255,1.0,  #izquierda, abajo
                -0.91, -0.45,0.0,1.0,     28/255, 23/255, 21/255,1.0, #arriba
                -0.918,-0.33,0.0,1.0,   28/255, 23/255, 21/255,1.0, #derecha
                -0.918, -0.45,0.0,1.0,    28/255, 23/255, 21/255,1.0, #derecha

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

                -0.53,1 -0.77,0.0, 1.0,       161/255, 161/255, 161/255,1.0,  #izquierda, abajo
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

        #HOJA
        for angulo in range(0, 359, 5):
            componente_x = 0.05 * math.cos(angulo * math.pi / 180) + 0.5 -1.3
            componente_y = 0.05 * math.sin(angulo * math.pi / 180) - 0.25 -0.6

            # self.vertices.insert([componente_x, component_y, 0.0 , 1.0, 
            #                         31/255, 31/255, 31/255, 1.0 ])

            self.vertices = np.append(self.vertices, 
            np.array([componente_x, componente_y, 0.0 , 1.0, 
                            44/255, 147/255, 3/255, 1.0 ], dtype="float32"))

        #ARBOL 1
        for angulo in range(0, 359, 5):
            componente_x = 0.08 * math.cos(angulo * math.pi / 180) + 0.8
            componente_y = 0.15 * math.sin(angulo * math.pi / 180) + 0.8

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.13 * math.cos(angulo * math.pi / 180) + 0.8
            componente_y = 0.1 * math.sin(angulo * math.pi / 180) + 0.8

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))

        #ARBOL 2
        for angulo in range(0, 359, 5):
            componente_x = 0.08 * math.cos(angulo * math.pi / 180) + 0.85
            componente_y = 0.15 * math.sin(angulo * math.pi / 180) - 0.3

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.13 * math.cos(angulo * math.pi / 180) + 0.85
            componente_y = 0.1 * math.sin(angulo * math.pi / 180) - 0.3

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))

        #ARBOL 3
        for angulo in range(0, 359, 5):
            componente_x = 0.08 * math.cos(angulo * math.pi / 180) + 0.6
            componente_y = 0.15 * math.sin(angulo * math.pi / 180) + 0.4

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.13 * math.cos(angulo * math.pi / 180) + 0.6
            componente_y = 0.1 * math.sin(angulo * math.pi / 180) + 0.4

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                            17/255, 46/255, 16/255, 1.0 ], dtype="float32"))

        #TORTUGA
        for angulo in range(0, 359, 5):
            componente_x = 0.015 * math.cos(angulo * math.pi / 180) + 0.38 -1.6
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.3 + 0.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            8/255, 58/255, 17/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.015 * math.cos(angulo * math.pi / 180) + 0.42 -1.6
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.3 + 0.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            8/255, 58/255, 17/255, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.4 -1.6
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.19 + 0.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            8/255, 58/255, 17/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.06 * math.cos(angulo * math.pi / 180) + 0.4 -1.6
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.25 + 0.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            8/255, 58/255, 17/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) + 0.4 -1.6
            componente_y = 0.05 * math.sin(angulo * math.pi / 180) - 0.25 + 0.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            44/255, 147/255, 3/255, 1.0 ], dtype="float32"))

        #PATO
        
        self.vertices = np.append(self.vertices, np.array(
            [
                -1.32 * 0.7, 0.37 * 0.7, 0, 1.0,  196/255, 96/255, 8/255, 1.0,  #izquierda, abajo
                -1.3 * 0.7, 0.4 * 0.7, 0, 1.0,     196/255, 96/255, 8/255, 1.0, #arriba
                -1.28 * 0.7, 0.37 * 0.7, 0, 1.0,    196/255, 96/255, 8/255, 1.0,   #derecha                         
            ], dtype="float32"
        ))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.4 - 1.7 
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.19 + 0.55

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            226/255, 193/255, 0.0, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.06 * math.cos(angulo * math.pi / 180) + 0.4 - 1.7
            componente_y = 0.02 * math.sin(angulo * math.pi / 180) - 0.25 + 0.55

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            226/255, 193/255, 0.0, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) + 0.4 - 1.7
            componente_y = 0.05 * math.sin(angulo * math.pi / 180) - 0.25 + 0.55

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.7, componente_y * 0.7, 0.0 , 1.0, 
                            226/255, 193/255, 0.0, 1.0 ], dtype="float32"))

        #FLOR 1

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 + 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 0, 148/255, 1.0 ], dtype="float32"))
        
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 + 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 0, 148/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 0, 148/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 0, 148/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32")) 
        
        #FLOR 2
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 + 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            255/255, 111/255, 0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 + 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            255/255, 111/255, 0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            255/255, 111/255, 0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            255/255, 111/255, 0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 -1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32"))

        #FLOR 3
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 + 1.8

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            186/255, 15/255, 15/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 + 1.8

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            186/255, 15/255, 15/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.8

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            186/255, 15/255, 15/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.8

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            186/255, 15/255, 15/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 1.8

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32"))

        #FLOR 4
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 + 0.1

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            15/255, 93/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 + 0.1

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            15/255, 93/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.1

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            15/255, 93/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.1

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            15/255, 93/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 + 0.1

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32"))

        #FLOR 5
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 - 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            139/255, 15/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 - 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            139/255, 15/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            139/255, 15/255, 153/255, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            139/255, 15/255, 153/255, 1.0 ], dtype="float32"))
                            
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 0.6

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32"))

        #FLOR 6
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.23 - 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            1, 1, 1, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.17 - 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            1, 1, 1, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.33 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            1, 1, 1, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.27 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            1, 1, 1, 1.0 ], dtype="float32"))
                            
        for angulo in range(0, 359, 5):
            componente_x = 0.02 * math.cos(angulo * math.pi / 180) + 0.3 - 1.08
            componente_y = 0.025 * math.sin(angulo * math.pi / 180) - 0.2 - 1.2

            self.vertices = np.append(self.vertices, np.array([componente_x * 0.6, componente_y * 0.6, 0.0 , 1.0, 
                            247/255, 227/255, 0, 1.0 ], dtype="float32"))

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)



    def actualizar(self, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        self.posicion.y = self.posicion.y - cantidad_movimiento

        self.velocidad = self.velocidad + (0.03 * tiempo_delta)

        if self.posicion.y < -2.5:
            self.posicion.y = 2

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
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 4)
        # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 92, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 164, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 236, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 308, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 380, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 452, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 524, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 596, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 668, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 740, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 812, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 884, 72)
        gl.glDrawArrays(gl.GL_TRIANGLES, 956, 3)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 959, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1031, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1103, 72)

        #FLORES
        #FLOR 1
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1175, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1247, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1319, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1391, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1463, 72)

        #FLOR 2
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1535, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1607, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1679, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1751, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1823, 72)

        #FLOR 3
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1895, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 1967, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2039, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2111, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2183, 72)

        #FLOR 4
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2255, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2327, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2399, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2471, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2543, 72)

        #FLOR 5
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2615, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2687, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2759, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2831, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2903, 72)

        #FLOR 6
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 2975, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 3047, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 3119, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 3191, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 3263, 72)




        gl.glBindVertexArray(0)
        self.shader.liberar_programa()


