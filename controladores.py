from ventana import *
from tkinter import *
from tkinter import messagebox

class controladoringresar():
    
    def __init__(self,ventana):
        self.ventanaingresar= ventana
    

    def OnclickObtener(self):
       self.ventanaingresar.Get_Modelo().Tablaingresardatos()  
    
    def OnclickBorrarvariable1(self):
        self.ventanaingresar.Is_activoboton1(1)
        self.ventanaingresar.Valorvariable1.delete(0,END)
        if self.ventanaingresar.activoVariable2 == False:
            self.ventanaingresar.ventana.Get_BotonEnviar().grid_forget()

    def OnclickAtras(self):
       self.ventanaingresar.Get_Modelo().CambioVentana(1)

    def OnclickBorrarvariable2(self):
        self.ventanaingresar.Is_activoboton2(1)
        self.ventanaingresar.Valorvariable2.delete(0,END)
        if self.ventanaingresar.activoVariable1 == False:
            self.ventanaingresar.ventana.Get_BotonEnviar().grid_forget()

    def CambiarVentana(self):
        self.ventanaingresar.Get_Modelo().CambioVentana(3)

class controladorVentanaInicio:
    def __init__(self,ventana) :
        self.ventanaInicio =ventana
    
    def OnclikCambiar(self):
       self.ventanaInicio.Get_Modelo().CambioVentana(1)

    def onclickCargarexcel(self):
        self.ventanaInicio.Get_Modelo().onclickCargarexcelinterface()
        
class  controladoroperaciones:

    def __init__(self,ventana):
        self.ventanaoperacion =ventana
    
    def calcular(self):
        self.ventanaoperacion.Get_Modelo().CalcularWilcoxon()  

    def calcularMann(self):
        self.ventanaoperacion.Get_Modelo().CalcularMann_Whitney()      

    def Boton_Atras(self):
        self.ventanaoperacion.Get_Modelo().CambioVentana(3)

    def Boton_AtrasI(self):
        self.ventanaoperacion.Get_Modelo().CambioVentana(2)

class controladorResultado:
    def __init__(self,ventana):
        self.ventana_resultado =ventana

    def OnclickAtras(self):
        self.ventana_resultado.Get_Modelo().CambioVentana(4)

    def OnclickAtras1(self):
        self.ventana_resultado.Get_Modelo().CambioVentana(5)    