import pygame
from pygame.locals import *
import sys
from aux_constantes import *
from gui_form_menu_main import FormMenuMain

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()

segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)

main_menu = FormMenuMain(name="main", master_surface = screen, imagen_background = PATH_RECURSOS + r"\background\Pradera0.png")

while True:
    
    delta_ms = clock.tick(FPS)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:       
            pygame.quit()
            sys.exit() 

    main_menu.update_form(lista_eventos, delta_ms, segundo, teclas_presionadas)
    pygame.display.flip()




    


  



