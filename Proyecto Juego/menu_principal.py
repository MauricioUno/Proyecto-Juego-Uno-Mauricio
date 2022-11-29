import pygame
from pygame.locals import *
import sys
from aux_constantes import *
from gui_form_menu_nivel import FormMenuNiveles
from gui_form_menu_main import FormMenuMain
from gui_form_menu_opciones import FormMenuOpciones
from gui_form_menu_sonido import FormSonido
from gui_form_menu_pausa import FormPausa
from gui_form_menu_win import FormWin
from gui_form_menu_lose import FormLose
from gui_form_nivel import FormNivel

pygame.init()

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()
segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)

main_menu = FormMenuMain(name="main", master_surface = screen, imagen_background = PATH_RECURSOS + r"\background\Pradera0.png")
levels_menu = FormMenuNiveles(name="levels",master_surface = screen, imagen_background =PATH_RECURSOS + r"\background\Pradera1.png")
options_menu = FormMenuOpciones(name="options",master_surface = screen, imagen_background =PATH_RECURSOS + r"\background\Pradera2.png")
sound_menu = FormSonido(name="sound", master_surface = screen, imagen_background =PATH_RECURSOS + r"\background\Pradera3.png")
pause = FormPausa(name="pause", master_surface=screen, x = 600, y=180, w=300, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaV.png")
win = FormWin(name="win", master_surface=screen, x = 375, y = 135, w = 750, h =450, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
lose = FormLose(name="lose", master_surface=screen, x = 550, y = 180, w = 400, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
level_one = FormNivel(name="level_1", master_surface= screen)
level_two = FormNivel(name="level_2", master_surface= screen)    
while True:

    delta_ms = clock.tick(FPS)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:       
            pygame.quit()
            sys.exit() 

    #print(delta_ms)
    
    if(main_menu.active):
        main_menu.draw(delta_ms, lista_eventos)
        
    elif(levels_menu.active):
        levels_menu.draw(delta_ms, lista_eventos)

    elif(options_menu.active):
        options_menu.draw(delta_ms, lista_eventos)

    elif(sound_menu.active):
        sound_menu.draw(delta_ms, lista_eventos)

    elif(level_one.active):
        level_one.update(lista_eventos, delta_ms, segundo)
        level_one.draw(lista_eventos, delta_ms, teclas_presionadas)

    elif(level_two.active):
         level_two.update(lista_eventos, delta_ms, segundo)
         level_two.draw(lista_eventos, delta_ms, teclas_presionadas)
            
    elif(pause.active):
        pause.draw(delta_ms, lista_eventos)

    elif(win.active):
        win.draw(delta_ms, lista_eventos)

    elif(lose.active):
        lose.draw(delta_ms, lista_eventos)
        
    pygame.display.flip()




    


  



