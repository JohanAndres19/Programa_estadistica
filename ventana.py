from tkinter import *  
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from Logica import *
from controladores import *
# ------>raiz o vemtana
class Raiz:
    def __init__(self,modelo):
        self._tk = Tk()
        self._tk.title("Ventana")
        self._tk.resizable(0, 0)
        self.ventanainicial = None         
       #Ventanainicial(self._tk)
        self.ventanaIngresar=None
        self.ventanaResultado=None
        self.ventanaOperaciones =None
        self.modelo =modelo
        #self._tk.mainloop()
   
    def Get_VentanaInicio(self):
        if self.ventanainicial == None: 
            self.ventanainicial = Ventanainicial(self._tk,self.modelo)
        return self.ventanainicial
   
    def Get_VentanaIngresar(self):
        if self.ventanaIngresar == None:
            self.ventanaIngresar = VentanaIngresarDatos(self._tk,self.modelo)
        return self.ventanaIngresar

    def Set_VentanaOperaciones(self,valor):
        self.ventanaOperaciones=valor

    def Get_VentanaOperaciones(self):
        if self.ventanaOperaciones == None:
            self.ventanaOperaciones = VentanaOperaciones(self._tk,self.modelo)
        
        return self.ventanaOperaciones
    
    def Set_VentanaResultado(self,valor):
        self.ventanaResultado=valor

    def Get_VentanaResultado(self):
        if self.ventanaResultado == None:
            self.ventanaResultado = VentanaResultados(self._tk,self.modelo)
        return self.ventanaResultado

class Visible:
    def __init__(self):
        self.visible=False

    def Set_visible(self,valor):
        self.visible=valor

    def Isvisibe(self):
        return self.visible 

# ----> Panel1 o panel inicial
class Ventanainicial(Frame,Visible):
    def __init__(self, master,modelo=None):
        super().__init__(master)
        self.config(bg="#06D14A")
        self.modelo=modelo
        self.controlador = controladorVentanaInicio(self)
        self.master = master
        self.componentes()

    def componentes(self):
        self.titulo= Label(self,text="Bienvenidos",font=("Comic Sans Ms", 24),bg="#06D14A",fg="white")
        self.titulo.grid(row=0,column=0,padx=60,pady=5,columnspan=2)
        self._boton = Button(self, text="Ingersar datos" + "\nmanualmente ", font=("Comic Sans Ms", 8), relief="raised", bd=7, bg="#2486FB", command=self.controlador.OnclikCambiar)
        self._boton.grid(row=1, column=0, padx=60, pady=45)
        self._boton2 = Button(self, text="Gargar archivo" + "\n excel", font=("Comic Sans Ms", 8),relief="raised", bd=7, bg="#2486FB", command=self.controlador.onclickCargarexcel)
        self._boton2.grid(row=1, column=1, padx=60, pady=45)
        self.pack()

    def Get_Modelo(self):
        return self.modelo
# ---------------------------------------
class VentanaIngresarDatos (Frame,Visible):
    def __init__(self, master,modelo=None):
        super().__init__(master)
        master.geometry("400x470")
        master.config(bg="#33D9FF")
        self.ventana=PanelDatos(master,self)
        self.master =master
        self.ventanainicio=0
        self.modelo = modelo
        self.config(bg="#33D9FF")
        self.controlador = controladoringresar(self)
        self.activo=True
        self.activoVariable1=True
        self.activoVariable2=True
        self.valor1=0
        self.valor2=0
        self.Componentes()

    def Componentes(self):
        self.titulo= Label(self,text="INGRESE LOS DATOS",font=("Comic Sans Ms",12),bg="#33D9FF")
        self.titulo.grid(row=0,column=0,columnspan=3,padx=20,pady=16)
        self.Valorvariable1 = Entry(self, width=8)
        self.Valorvariable1.grid(row=1, column=0, padx=35, pady=1)
        self.Valorvariable2 = Entry(self, width=8)
        self.Valorvariable2.grid(row=1, column=2, padx=35, pady=1)
        self.boton = Button(self,text="agregar",font=("Comic Sans Ms", 8),command=self.controlador.OnclickObtener)
        self.boton.grid(row=1, column=1, padx=42, pady=1)
        self.botonborrar1= Button(self,text="Borrar"+"\nVariable 1",font=("Comic Sans Ms", 8),state="disabled",command=self.controlador.OnclickBorrarvariable1)
        self.botonborrar1.grid(row=2,column=0,padx=35,pady=5)
        self.botonborrar2= Button(self,text="Borrar"+"\nVariable 2",font=("Comic Sans Ms", 8),state="disabled",command=self.controlador.OnclickBorrarvariable2)
        self.botonborrar2.grid(row=2,column=2,padx=35,pady=5)
        self.botonAtras =Button(self.master,text="Atras",font=("Comic Sans Ms", 12),command=self.controlador.OnclickAtras)
        self.botonAtras.place(x=171,y=420)
        self.pack(side="left", anchor="n", fill="x")
   
    def Is_activoboton1(self,opcion):
        if opcion==0:
            self.Valorvariable1.config(state="readonly")
            self.activoVariable1=False
        elif opcion==1:
            self.Valorvariable1.config(state="normal")
            self.activoVariable1=True   
            
    def Is_activoboton2(self,opcion):
        if opcion==0:
            self.Valorvariable2.config(state="readonly")
            self.activoVariable2=False
        elif opcion==1:
            self.Valorvariable2.config(state="normal")
            self.activoVariable2=True  
    
    def Organizar(self):
        self.pack()
        self.ventana.place(x=94, y=140)
        self.botonAtras.place(x=171,y=430)   
        self.master.geometry("400x470")
        self.master.config(bg="#33D9FF")

    def Get_Modelo(self):
        return self.modelo

    def Ocultar(self):
        self.ventana.place_forget()
        self.pack_forget()
        self.botonAtras.place_forget()
# -------------------------------
class VentanaOperaciones(Frame,Visible):

    def __init__(self, master,modelo=None):
        super().__init__(master,width=500,height=450)
        self.datos1=[]
        self.datos2=[]
        self.modelo=modelo 
        self.posicion=0
        self.controlador = controladoroperaciones(self)
        master.geometry("550x450")
        master.config(bg="#9AFF10")
        self.config(bg="#9AFF10")
        self.comboactivo=False
        self.textactivo=False
    
    def Componentes(self):
        self.label=Label(self,text="    Datos Ingresados",font=("Comic Sans Ms",12),bg="#9AFF10")
        self.label.grid(row=0,column=0,columnspan=2,pady=20,padx=40)
        self.paneldatos= PanelMostrarDatos(self,self.datos1,self.datos2)
        self.botonWilcoxon= Button(self,text="Suma de rangos"+"\nde Wilcoxon",font=("Comic Sans Ms",8),command=self.OnclickWilcoxon)
        self.botonMannw=Button(self,text="Prueba U de "+"\nMann–Whitney",font=("Comic Sans Ms",8),command=self.OnclickMann_Whitney) 
        self.botonatras= Button(self,text="Atras")
        if len(self.datos1)<=len(self.datos2):
            self.maximo = len(self.datos2)
            self.botonWilcoxon.grid(row=len(self.datos2)+1,column=0,padx=40,pady=15)
            self.botonMannw.grid(row=len(self.datos2)+1,column=1,padx=40,pady=15)
        else:
            self.maximo=len(self.datos1)
            self.botonWilcoxon.grid(row=len(self.datos1)+1,column=0,padx=40,pady=15)
            self.botonMannw.grid(row=len(self.datos1)+1,column=1,padx=40,pady=15)
        self.botonatras.grid(row=self.maximo+1,column=0,columnspan=2,pady=15)
        self.pack(fill="y", expand=1)  

    def OnclickWilcoxon(self):
        if self.textactivo==True:
            if self.posicion==0:
             self.labelcombo2.grid_forget()   
             self.entrada_alpha.grid_forget()
             self.botoncalcular.grid_forget()
            else:
             self.labelcombo2.place_forget()     
             self.entrada_alpha.place_forget()
             self.botoncalcular.place_forget()
            self.Is_activoTextField(0)    
        self.comboopciones = ttk.Combobox(self,state="readonly",width=15)
        self.Opciones()
        self.Is_activoCombo(1)
        self.bototonopcion.config(command=self.OnclikObteneropcionW)
    
    def Opciones(self):
        self.labelcombo= Label(self,text="Hipotesis alternativa",font=("Comic Sans Ms",8))
        self.labelcombo2= Label(self, font=("Comic Sans Ms",8))
        self.comboboxhipoalter = ttk.Combobox(self,state="readonly",width=20)
        self.comboboxhipoalter["values"]=["seleccione una opcion","μ1<μ2","μ1>μ2","μ1≠μ2"]
        self.comboboxhipoalter.current(0)
        self.bototonopcion = Button(self,text="Obtener opcion ",font=("Comic Sans Ms",8))
        self.botoncalcular=Button(self,text="calcular",command=self.controlador.calcular)
        if (self.maximo)<=5:
            self.labelcombo.grid(row=self.maximo+2,column=0,sticky="n",pady=5)
            self.comboboxhipoalter.grid(row=self.maximo+3,column=0,padx=10)
            self.bototonopcion.grid(row=self.maximo+3,column=1,pady=5)
        else:
            self.paneldatos.grid_configure(columnspan=1)
            self.label.grid_configure(columnspan=3,column=0)
            self.botonWilcoxon.grid(columnspan=2)
            self.botonMannw.grid(columnspan=2)
            self.botonatras.grid(columnspan=1)
            self.bototonopcion.grid(row=1,column=2)
            self.comboboxhipoalter.grid(row=1,column=1,padx=10)
            if self.maximo <=7:
                self.labelcombo.grid(row=1,column=1,sticky="n")
            else:
                ejey=(self.maximo//2)*30+10
                ejex=(195+10)
                self.labelcombo.place(x=ejex,y=ejey)  
            self.posicion=1

    def OnclikObteneropcionW(self):
        if self.comboboxhipoalter.get() != "seleccione una opcion":
            if self.comboboxhipoalter.get()=="μ1<μ2" or self.comboboxhipoalter.get()== "μ1>μ2":
               self.comboopciones["values"]=[" ","0.001","0.01","0.025","0.05"]
               self.labelcombo2.config(text="Valor de alpha para una cola ")
            elif self.comboboxhipoalter.get() == "μ1≠μ2":
               self.comboopciones["values"]=[" ","0.002","0.02","0.05","0.1"]        
               self.labelcombo2.config(text="Valor de alpha para dos colas ") 
            if self.posicion==0:
                self.labelcombo2.grid(row=self.maximo+4,column=0)
                self.comboopciones.grid(row=self.maximo+5,column=0) 
                self.botoncalcular.grid(row=self.maximo+5,column=1)
            elif self.posicion ==1:
                ejey=(self.maximo//2)*35+90
                self.labelcombo2.place(x=(180+10),y=ejey)
                self.comboopciones.place(x=(195+10),y=(ejey+30))
                self.botoncalcular.place(x=((195+10)+150),y=(ejey+30))
            self.comboopciones.current(0)    

    def OnclickMann_Whitney(self):
        if self.comboactivo==True:
            if self.posicion==0:
                self.botoncalcular.grid_forget()
                self.comboopciones.grid_forget()
                self.labelcombo2.grid_forget()
            else:
                self.labelcombo2.place_forget()
                self.comboopciones.place_forget()
                self.botoncalcular.place_forget()
            self.Is_activoCombo(0)        
        self.entrada_alpha = Entry(self,width=15)
        self.Opciones()
        self.Is_activoTextField(1)
        self.bototonopcion.config(command=self.OnclickObtenerMann)
        self.botoncalcular.config(command=self.controlador.calcularMann)

    def OnclickObtenerMann(self):
        if self.comboboxhipoalter.get() != "seleccione una opcion":
            if self.comboboxhipoalter.get()=="μ1<μ2" or self.comboboxhipoalter.get()== "μ1>μ2":
               self.labelcombo2.config(text="Valor de alpha para una cola ")
            elif self.comboboxhipoalter.get() == "μ1≠μ2":
               self.labelcombo2.config(text="Valor de alpha para dos colas ") 
            if self.posicion==0:
                self.labelcombo2.grid(row=self.maximo+4,column=0)
                self.entrada_alpha.grid(row=self.maximo+5,column=0) 
                self.botoncalcular.grid(row=self.maximo+5,column=1) 
            elif self.posicion==1: 
                ejey=(self.maximo//2)*35+90
                self.labelcombo2.place(x=(180+10),y=ejey)
                self.entrada_alpha.place(x=(195+10),y=(ejey+30))
                self.botoncalcular.place(x=((195+10)+150),y=(ejey+30))        
                    
    def Is_activoCombo(self,opcion):
        if opcion==0:
            self.comboactivo=False
        elif opcion==1:
            self.comboactivo=True

    def Is_activoTextField(self,opcion):
        if opcion==0:
            self.textactivo=False
        elif opcion ==1 :
            self.textactivo=True            

    def Get_botonatras(self):
        return self.botonatras 

    def Get_Modelo(self):
        return self.modelo

    def Set_Datos1(self,lista):
        self.datos1=lista

    def Set_Datos2(self,lista):
        self.datos2=lista

    def Get_Datos1(self):
      return self.datos1

    def Get_Datos2(self):
      return self.datos2  

    def Get_combohipoalter(self):
        return self.comboboxhipoalter

    def Get_comboopcione(self):
        return self.comboopciones

    def Get_JtextDato(self):
        return self.entrada_alpha
#-------------------------------------------  
class VentanaResultados(Frame,Visible):
    def __init__(self, master,modelo=None):
        super().__init__(master)
        self.modelo=modelo
        self.opcion=0
        self.uaux=None
        self.controlador = controladorResultado(self)
        self.listarespuesta=[]
        self.config(bg="#9AFF10")
        self.boton_atras =Button(self,text="Atras")
 
    def Componentes(self,resultado):
        self.Set_listarespuesta(resultado)
        self.labeHipotesis=Label(self,text="HIPOTESIS NULA: μ1=μ2",font=("Comic Sans Ms",10),bg="#9AFF10")
        self.hipotesistalternativa = Label(self,text="HIPOTESIS ALTERNATIVA: "+resultado[1],font=("Comic Sans Ms",10),bg="#9AFF10")
        self.uaux= Label(self,text="Valor de "+(resultado[0])[1]+" : "+str((resultado[0])[0]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.uaux.grid(row=5,column=0,pady=10)        
        self.w1=Label(self,text="Valor de W1 "+str(resultado[2]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.w2=Label(self,text="Valor de W2 "+str(resultado[3]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.u = Label(self,text="Valor de U (tabla) "+str(resultado[4]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.analisis= Label(self,text="Al comparar el valor "+(resultado[0])[1]+"  con el valor de la tabla  para"+"\nevaluar  la Hipotesis nula podemos ver que: "+"\n"+str((resultado[0])[0])+" ≤ "+str(resultado[4]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.respuesta=Label(self,text="Por lo tanto se puede concluir que "+"\n"+str(resultado[5]),font=("Comic Sans Ms",10),bg="#9AFF10")
        self.labeHipotesis.grid(row=0,column=0,pady=10)
        self.hipotesistalternativa.grid(row=1,column=0,pady=10)
        self.w1.grid(row=2,column=0,pady=10)
        self.w2.grid(row=3,column=0,pady=10)
        self.u.grid(row=4,column=0,pady=10)    
        self.analisis.grid(row=6,column=0,pady=10)
        self.respuesta.grid(row=7,column=0,pady=10)
        self.boton_atras.grid(row=8,column=0)
        self.boton_atras.config(command=self.controlador.OnclickAtras)
        self.pack(side=TOP) 
    
    def ComponentesMann(self,resultado):
        self.Set_listarespuesta(resultado)
        if len(resultado)==7:
          self.hipo_nula=Label(self,text="HIPOTESIS NULA: μ1=μ2",font=("Comic Sans Ms",9),bg="#9AFF10")  
          self.hipo_alter=Label(self,text="HIPOTESIS ALTERNATIVA: "+resultado[len(resultado)-1],font=("Comic Sans Ms",9),bg="#9AFF10")
          self.labelu=Label(self,text="El valor de U es "+str(resultado[0]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.labelu0=Label(self,text="El valor de U0 (valor de la tabla) es "+str(resultado[2]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.labelw1=Label(self,text="Valor de W1 es: "+str(resultado[1]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.label_alpha=Label(self,text="Valor de alpha ingresado: "+str(resultado[4]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.label_alphaprox=Label(self,text="Valor aproximado de alpha (valor de tabla): "+str(resultado[3]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.analisis = Label(self,text="Al comparar  el valor de U con U0 para evaluar la Hipotesis Nula se obtiene que"+"\n"+str(resultado[0])+"≤"+str(resultado[2]),font=("Comic Sans Ms",9),bg="#9AFF10")
          self.solucion = Label(self,text="Por lo  tanto se puede concluir que"+"\n"+resultado[len(resultado)-2],font=("Comic Sans Ms",9,),bg="#9AFF10")        
        else:
            if resultado[len(resultado)-1]=="μ1<μ2":
                self.hipo_nula=Label(self,text="HIPOTESIS NULA: μ1=μ2",bg="#9AFF10",font=("Comic Sans Ms",9))  
                self.hipo_alter=Label(self,text="HIPOTESIS ALTERNATIVA: "+resultado[len(resultado)-1],font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelu=Label(self,text="El valor de U es "+str(resultado[0]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelu0=Label(self,text="El valor de U0 (valor de la tabla) es "+str(resultado[2]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelw1=Label(self,text="Valor de W1 es: "+str(resultado[1]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.label_alpha=Label(self,text="Valor de alpha ingresado: "+str(resultado[5]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.label_alphaprox=Label(self,text="Valor aproximado de alpha (valor de tabla): "+str(resultado[4]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.analisis = Label(self,text="Al comparar  el valor de U con  (N1*N2)-U0 para evaluar la Hipotesis Nula se obtiene que "+"\n"+str(resultado[0])+" ≥ "+str(resultado[3]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.solucion = Label(self,text="Por lo  tanto se puede concluir que"+"\n"+resultado[len(resultado)-2],font=("Comic Sans Ms",9),bg="#9AFF10")          
            else:
                self.hipo_nula=Label(self,text="HIPOTESIS NULA: μ1=μ2",font=("Comic Sans Ms",9),bg="#9AFF10")  
                self.hipo_alter=Label(self,text="HIPOTESIS ALTERNATIVA: "+resultado[len(resultado)-1],font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelu=Label(self,text="El valor de U es "+str(resultado[0]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelu0=Label(self,text="El valor de U0 (valor de la tabla) es "+str(resultado[2]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.labelw1=Label(self,text="Valor de W1 es: "+str(resultado[1]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.label_alpha=Label(self,text="Valor de alpha ingresado: "+str(resultado[5]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.label_alphaprox=Label(self,text="Valor aproximado de alpha (valor de tabla): "+str(resultado[4]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.analisis = Label(self,text="Al comparar  el valor de U con U0 y  (N1*N2)-U0 para evaluar la Hipotesis Nula se obtiene que "+"\n"+str(resultado[0])+" ≥ "+str(resultado[3])+" o "+str(resultado[0])+"≤"+str(resultado[2]),font=("Comic Sans Ms",9),bg="#9AFF10")
                self.solucion = Label(self,text="Por lo  tanto se puede concluir que"+"\n"+resultado[len(resultado)-2],font=("Comic Sans Ms",9),bg="#9AFF10")          
        self.hipo_nula.grid(row=0,column=0,pady=8)
        self.hipo_alter.grid(row=1,column=0,pady=8)
        self.labelu.grid(row=2,column=0,pady=8)
        self.labelu0.grid(row=3,column=0,pady=8)
        self.labelw1.grid(row=4,column=0,pady=8)
        self.label_alpha.grid(row=5,column=0,pady=8)
        self.label_alphaprox.grid(row=6,column=0,pady=8)
        self.analisis.grid(row=7,column=0,pady=8)  
        self.solucion.grid(row=8,column=0,pady=8)
        self.boton_atras.grid(row=9,column=0)
        self.boton_atras.config(command=self.controlador.OnclickAtras1) 
        self.pack(side=TOP)                  

    def Get_Modelo(self):
        return self.modelo

    def Set_listarespuesta(self,valor):
        self.listarespuesta=valor

    def Get_listarespuesta(self):
        return self.listarespuesta

class PanelDatos(PanedWindow):
    def __init__(self, master,ventana):
        super().__init__(master)
        self.ventana=ventana
        self.config(bg="#86E2A3")
        self.agregar = True
        self.opcion =(0,0)
        self.Contenido()

    def Contenido(self):
        self.Lista1=[]
        self.Lista2=[]
        self.aux1=0
        self.aux2=0
        for row in range(1):
            for column in range(2):
                label = Label(self, text="Variable : " + str(column+1),bg="#86E2A3",fg="white")
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew",padx=1, pady=1)
                self.grid_columnconfigure(column, weight=1)
        self.place(x=94, y=140)
    
    def ConstruirTabla(self,valor1, valor2):
        if self.verificar():
            self.Agregar(1,valor1)
            self.Agregar(2,valor2)
            self.botonenviar= Button(self,text="Enviar datos",command=self.OnclickEnviarDatos)
            if valor1 <= valor2:
               self.botonenviar.grid(row=valor2+1,column=0,columnspan=2,pady=2)
            else:
               self.botonenviar.grid(row=valor1+1,column=0,columnspan=2,pady=2)    
        else:
            if valor2==0:
                if self.Get_Agregar() :
                  self.Agregar(1,valor1)
                else:
                  self.Borar(1,valor1)        
            elif valor1==0:
                if self.Get_Agregar() :
                  self.Agregar(2,valor2)
                else:
                  self.Borar(2,valor2)  
            elif valor1 !=0 and valor2!=0:
                if self.Get_Opcion()==(1,1):
                    self.Agregar(1,valor1)
                    self.Agregar(2,valor2)
                elif self.Get_Opcion()==(0,0):
                    self.Borar(1,valor1) 
                    self.Borar(2,valor2)  
                elif self.Get_Opcion()==(0,1):
                    self.Borar(1,valor1)
                    self.Agregar(2,valor2)
                elif self.Get_Opcion()==(1,0):
                    self.Agregar(1,valor1)
                    self.Borar(2,valor2)
            if len(self.Lista1)<= len(self.Lista2):
                self.botonenviar.grid(row=len(self.Lista2)+1,column=0,columnspan=2,pady=2)
            else:
                self.botonenviar.grid(row=len(self.Lista1)+1,column=0,columnspan=2,pady=2)
    
    def Agregar(self,opcion,cantidad):
        if opcion ==1:
            tamaño = cantidad-len(self.Lista1)
            for i in range(tamaño):
                entrada = Entry(self,width=15)
                entrada.grid(row=(len(self.Lista1)+1), column=0, padx=1, pady=1)
                self.Lista1.append(entrada)
        elif opcion ==2:            
            tamaño = cantidad-len(self.Lista2)
            for i in range(tamaño):
                entrada = Entry(self,width=15)
                entrada.grid(row=(len(self.Lista2)+1), column=1, padx=1, pady=1)
                self.Lista2.append(entrada)

    def Borar(self,opcion,cantidad):
        if opcion == 1:
            inicio=len(self.Lista1)-1
            for i in range(inicio,cantidad-1,-1):
               aux=self.Lista1.pop(i)
               aux.grid_forget()
        elif opcion ==2: 
            inicio = len(self.Lista2)-1 
            for i in range(inicio,cantidad-1,-1):
                aux=self.Lista2.pop(i)
                aux.grid_forget()    

    def verificar(self):
        if len(self.Lista1)==0 and len(self.Lista2)==0:
            return True
        else:
            return False    
    
    def OnclickEnviarDatos(self):
        try:
            self.variable1=[]
            self.variable2=[]
            for i in  self.Lista1:
                numero = i.get()
                if numero.find(".")== -1:
                    self.variable1.append(int(numero))
                else:
                    self.variable1.append(float(numero))
            
            for j in  self.Lista2:
                numero = j.get()
                if numero.find(".")== -1:
                    self.variable2.append(int(numero))
                else:
                    self.variable2.append(float(numero))
            
            self.ventana.controlador.CambiarVentana()                                              
        except:
            messagebox.showwarning("Advertencia","Por favor ingrese valores validos"+"\n y utilize un punto ( . ) para las cifras decimales ")  
    
    def Get_Agregar(self):
        return self.agregar

    def Get_Variable1(self):
        return self.variable1

    def Get_Variable2(self):
        return self.variable2    

    def Get_Opcion(self):
        return self.opcion

    def Get_BotonEnviar(self):
        return self.botonenviar

    def Set_Agregar(self,valor):
        self.agregar=valor

    def Set_opcion(self,valor):
        self.opcion=valor

class PanelMostrarDatos(PanedWindow):
    
    def __init__(self, master,datos1,datos2):
        super().__init__(master,)
        self.variable1=datos1
        self.variable2=datos2
        self.Componentes()

    def Componentes(self):
        for row in range(1):
            for column in range(2):
                label = Label(self, text="Variable : " + str(column+1),bg="#ECC337")
                label.config(font=('Arial', 12))
                label.grid(row=row, column=column, sticky="nsew",padx=1, pady=1)
                self.grid_columnconfigure(column, weight=1)

        for i in range(len(self.Get_Variable1())):
            label = Label(self, text=str(self.Get_Variable1()[i]),bg="#ECC337")
            label.config(font=('Arial', 12))
            label.grid(row=i+1, column=0, sticky="nsew",padx=1, pady=1)

        for j in range(len(self.Get_Variable2())):
            label = Label(self, text=str(self.Get_Variable2()[j]),bg="#ECC337")
            label.config(font=('Arial', 12))
            label.grid(row=j+1, column=1, sticky="nsew",padx=1, pady=1) 
        
        self.grid(row=1,column=0,columnspan=2)

    def Get_Variable1(self):
       return self.variable1

    def Get_Variable2(self):
       return self.variable2   
#-------------------------------------