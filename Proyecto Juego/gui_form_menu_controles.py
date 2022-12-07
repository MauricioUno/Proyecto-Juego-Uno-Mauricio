from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget



class FormControles(Form):
    def __init__(self, name, master_surface, x = 0, y = 0, w = ANCHO_VENTANA, h = ALTO_VENTANA, color_background = None, imagen_background = None, color_border= None, active = False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.valor = 0
        self.textos = ["[ A ] : ganar (sobre el portal)", "[ Z ] : disparar", "[ SPACE ] : saltar", "[LEFT & RIGHT] : moverse"]
        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, on_click_param="main",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.prev = Button(master=self, x= 300 ,y = 200, w = 75, h= 75, image_background= PATH_RECURSOS + r"\gui\prew.png",on_click=self.cambiar_valor, on_click_param=-1)
        self.next = Button(master=self, x= 1125 ,y = 200, w = 75, h= 75, image_background= PATH_RECURSOS + r"\gui\next.png",on_click=self.cambiar_valor, on_click_param=1)
        self.image = Widget (master=self, x = 375, y = 20, w = 750, h =450)
        self.text = Widget (master=self, x= 450, y = 500, w=600, h=150, image_background=PATH_RECURSOS + r"\gui\Table.png", text= " ", font_size= 40, font_color= COLOR_TEXTO_MENU)
        self.lista_widget = [self.image, self.text, self.back, self.next, self.prev]
        self.cambiar_valor(self.valor)


    def cambiar_valor(self, modificacion):
        self.valor += modificacion
        if self.valor > 3:
            self.valor = 0
        elif self.valor < 0:
            self.valor = 3

        self.actualizar_widgets(self.valor)
        self.play_efecto_sonido("click")


    def actualizar_widgets(self, valor):
        self.image.change_image_background(PATH_RECURSOS + r"\background\tutorial{0}.png".format(valor))
        try:
            self.text.text = self.textos[valor]
        except:
            self.text.text = "ERROR! NO DATA!"

    def retroceder(self, parametro):
        self.forms_dict.pop("controls")
        self.on_click_boton("options")