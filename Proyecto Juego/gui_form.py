import pygame
from aux_constantes import *

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect(x = x, y = y)
        self.active = active
        
        if imagen_background != None:
            self.image_background  = pygame.image.load(imagen_background).convert_alpha()
            self.image_background  = pygame.transform.scale(self.image_background, (self.w, self.h)).convert_alpha()
        else:
            self.image_background = None

        self.lista_widget = []
        

    def on_click_boton(self, parametro):
        self.set_active(parametro)


    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True


    def update_form(self, lista_eventos, delta_ms, segundo, teclas_presionadas):
        for aux_form in self.forms_dict.values():
            if aux_form.active:
                aux_form.update(lista_eventos, delta_ms, segundo)
                aux_form.draw(lista_eventos, delta_ms, teclas_presionadas)
                break

    

    def render(self):
        if(self.color_background != None):
            self.surface.fill(self.color_background)

        if(self.image_background != None):
            self.surface.blit(self.image_background, (0,0))

        if self.color_border != None:
            pygame.draw.rect(self.surface, self.color_border, self.surface.get_rect(), 2)


    def update(self, lista_eventos, delta_ms, segundo):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)


    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        self.master_surface.blit(self.surface,self.slave_rect)
        self.render()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
            
        
        
        
        
        


