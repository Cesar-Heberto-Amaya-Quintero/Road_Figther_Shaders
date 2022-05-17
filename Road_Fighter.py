from pickle import GLOBAL
import OpenGL.GL as gl
import glfw
import numpy as np
from Carro import *
from Shader import *
from Modelo import *
from Triangulo import Triangulo
from LineaCalle import *
from CosasFondo import *
from CosasFondoEstaticas import * 
from Pajaro import * 
from Pajaro2 import * 
from Enemigo import * 

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 880

modelo = None
lineaCalle = None
cosasFondo = None
pajaro = None
pajaro2 = None
enemigo = None
cosasFondoEstaticas = None
window = None

enemigos = []

tiempo_anterior = 0.0

posiciones_enemigos = [
    [-0.3, 1.3, 0.0],
    [0.0, 2.1, 0.0], 
    [0.3, 2.9, 0.0],
    [0.2, 1.8, 0.0],
    [0.1, 2.5, 0.0]]

colores_enemigos = [
    [245/255, 215/255, 66/255],
    [66/255, 149/255, 245/255], 
    [245/255, 215/255, 66/255],
    [72/255, 35/255, 122/255],
    [240/255, 41/255, 41/255]]

velocidades_enemigos = [1, 1, 1, 1, 1]
direcciones_enemigos = [0,0,0,0,0]
activos_enemigos = [1,1,1,1,1]

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def inicializar_enemigos(shader, posicion_id, color_id, transformaciones_id):
    for i in range(5):
        posicion_x = posiciones_enemigos[i][0]
        posicion_y = posiciones_enemigos[i][1]
        direccion = direcciones_enemigos[i]
        velocidad = velocidades_enemigos[i]
        activos = activos_enemigos[i]
        colorR = colores_enemigos[i][0]
        colorG = colores_enemigos[i][1]
        colorB = colores_enemigos[i][2]
        enemigos.append(Enemigo(shader, posicion_id, color_id, transformaciones_id,posicion_x, posicion_y, 0.0, velocidad, direccion, activos, colorR, colorG, colorB))

def actualizar():
    global window
    global modelo
    global lineaCalle
    global cosasFondo
    global tiempo_anterior
    global enemigo

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecución actual y la inmediata anterior de este función
    tiempo_delta = tiempo_actual - tiempo_anterior

    modelo.actualizar(window, tiempo_delta)
    lineaCalle.actualizar()
    cosasFondo.actualizar(tiempo_delta)
    pajaro.actualizar(tiempo_delta)
    pajaro2.actualizar(tiempo_delta)

    tiempo_anterior = tiempo_actual

    for enemigo in enemigos:
        if enemigo.colisionando(modelo):
            print("chocastess")
    for enemigo in enemigos:
        enemigo.actualizar(tiempo_delta)

def dibujar():
    global modelo
    global lineaCalle
    global cosasFondo
    global cosasFondoEstaticas
    global pajaro
    global pajaro2
    global enemigo

    cosasFondoEstaticas.dibujar()
    cosasFondo.dibujar()
    
    lineaCalle.dibujar()
    modelo.dibujar()
    pajaro.dibujar()
    pajaro2.dibujar()
    
    for enemigo in enemigos:
        enemigo.dibujar()
    
    

def main():
    global modelo
    global window
    global lineaCalle
    global cosasFondo
    global cosasFondoEstaticas
    global pajaro
    global pajaro2
    global enemigo
    
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")
    
    modelo = Carro(shader, 
            posicion_id, color_id, transformaciones_id)

    lineaCalle = LineaCalle(shader, 
            posicion_id, color_id, transformaciones_id)

    cosasFondo = CosasFondo(shader, 
            posicion_id, color_id, transformaciones_id)
    
    cosasFondoEstaticas = CosasFondoEstaticas(shader, 
            posicion_id, color_id, transformaciones_id)
    
    pajaro = Pajaro(shader, 
            posicion_id, color_id, transformaciones_id)
    
    pajaro2 = Pajaro2(shader, 
            posicion_id, color_id, transformaciones_id)
    
    inicializar_enemigos(shader, posicion_id, color_id, transformaciones_id)
    
    # enemigo = Enemigo(shader, 
    #         posicion_id, color_id, transformaciones_id)

    

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(69/255, 145/255, 2/255,1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    lineaCalle.borrar()
    cosasFondo.borrar()
    cosasFondoEstaticas.borrar()
    pajaro.borrar()
    pajaro2.borrar()
    shader.borrar()

    

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

