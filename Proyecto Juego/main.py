import pygame
import sys
from aux_constantes import *
from gui_form_main import FormMenuMain
from aux_json import importar_lista
from manager_data import crear_archivo_DB

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()

segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)

crear_archivo_DB()
main_menu = FormMenuMain(name="main", master_surface = screen, imagen_background = PATH_RECURSOS + r"\background\Pradera0.png")
main_menu.crear_efectos_de_sonido(importar_lista(PATH_JSON.format("sonidos"), "sounds"))
while True:
    
    delta_ms = clock.tick(FPS)
    print(delta_ms)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:       
            pygame.quit()
            sys.exit() 
    
    main_menu.update_form(lista_eventos, delta_ms, segundo, teclas_presionadas) 
    pygame.display.flip()




    


  



