from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# ------>raiz o vemtana
class Raiz:
    def __init__(self):
        self._tk = Tk()
        self._tk.title("Ventana")
        self._tk.resizable(0, 0)
        Ventanainicial(self._tk)
        self._tk.mainloop()
# ----> Panel1 o panel inicial
class Ventanainicial(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#06D14A")
        self.master = master
        self.componentes()

    def componentes(self):
        self._boton = Button(self, text="Ingersar datos" + "\nmanualmente ", font=("Comic Sans Ms", 8), relief="raised", bd=7, bg="#2486FB", command=self.OnclikCambiar)
        self._boton.grid(row=0, column=0, padx=60, pady=85)
        self._boton2 = Button(self, text="Gargar archivo" + "\n excel", font=("Comic Sans Ms", 8),relief="raised", bd=7, bg="#2486FB", command=self.onclickCargarexcel)
        self._boton2.grid(row=0, column=1, padx=60, pady=85)
        self.pack()

    def onclickCargarexcel(self):
        self.filename = filedialog.askopenfilename(title="select a file", filetypes=(
            ("xlsx files", "*.xlsx"), ("all files", "*.*")))
        print(self.filename)

    def OnclikCambiar(self):
        self.pack_forget()
        VentanaIngresarDatos(self.master)
# ---------------------------------------
class VentanaIngresarDatos (Frame):
    def __init__(self, master):
        super().__init__(master)
        self.ventana=PanelDatos(master,self)
        master.geometry("400x450")
        master.config(bg="#33D9FF")
        self.master =master
        self.config(bg="#33D9FF")
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
        self.boton = Button(self,text="agregar",font=("Comic Sans Ms", 8),command=self.OnclickObtener)
        self.boton.grid(row=1, column=1, padx=42, pady=1)
        self.botonborrar1= Button(self,text="Borrar"+"\nVariable 1",font=("Comic Sans Ms", 8),state="disabled",command=self.OnclickBorrarvariable1)
        self.botonborrar1.grid(row=2,column=0,padx=35,pady=5)
        self.botonborrar2= Button(self,text="Borrar"+"\nVariable 2",font=("Comic Sans Ms", 8),state="disabled",command=self.OnclickBorrarvariable2)
        self.botonborrar2.grid(row=2,column=2,padx=35,pady=5)
        self.pack(side="left", anchor="n", fill="x")
    
    def OnclickObtener(self):
        try:
            if self.activo:
                self.valor1=int(self.Valorvariable1.get())
                self.valor2=int(self.Valorvariable2.get())            
                if self.valor1 in range(1,11) and self.valor2 in range(1,11):
                    print("valor 1:",self.valor1,"valor 2:",self.valor2)
                    self.ventana.ConstruirTabla(self.valor1,self.valor2)
                    self.Is_activoboton1(0)
                    self.Is_activoboton2(0)
                    self.activo=False
                    self.botonborrar1.config(state="active")
                    self.botonborrar2.config(state="active")
                else:
                    messagebox.showwarning("Advertencia","Por favor ingrese valores validos"+"\n y que esten en el rango de 1 a 10")        
            else:
                if self.activoVariable1==True and self.activoVariable2==False:
                    aux= int(self.Valorvariable1.get())
                    if aux in range(1,11):
                        if aux > self.valor1:
                            self.ventana.Set_Agregar(True) 
                            self.ventana.ConstruirTabla(aux,0)
                        elif aux <self.valor1:
                            self.ventana.Set_Agregar(False) 
                            self.ventana.ConstruirTabla(aux,0)
                    else:
                        raise Exception('')        
                elif self.activoVariable2==True and self.activoVariable1==False:
                    aux= int(self.Valorvariable2.get())
                    if aux in range(1,11):
                        if aux > self.valor2:
                            self.ventana.Set_Agregar(True) 
                            self.ventana.ConstruirTabla(0,aux)
                        elif aux <self.valor2:
                            self.ventana.Set_Agregar(False) 
                            self.ventana.ConstruirTabla(0,aux)
                    else:
                        raise Exception('')       
                elif self.activoVariable2==True and self.activoVariable1==True:
                    pass    
        except: 
            e = sys.exc_info()[1]
            print(e.args[0])    
            messagebox.showwarning("Advertencia","Por favor ingrese valores validos"+"\n y que esten en el rango de 1 a 10")  

    def OnclickBorrarvariable1(self):
        self.Is_activoboton1(1)
        self.Valorvariable1.delete(0,END)
        if self.activoVariable2 == False:
            self.ventana.Get_BotonEnviar().grid_forget()

         
    def OnclickBorrarvariable2(self):
        self.Is_activoboton2(1)
        self.Valorvariable2.delete(0,END)
        if self.activoVariable1 == False:
            self.ventana.Get_BotonEnviar().grid_forget()

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
    
    def CambiarVentana(self):
        self.ventana.place_forget()
        self.pack_forget()
        VentanaOperaciones(self.master,self.ventana.Get_Variable1(),self.ventana.Get_Variable2())
# -------------------------------
class VentanaOperaciones(Frame):

    def __init__(self, master,datos1,datos2):
        super().__init__(master,width=500,height=450)
        self.datos1=datos1
        self.datos2=datos2
        master.geometry("500x450")
        self.config(bg="pink") 
        self.Componentes()
    
    def Componentes(self):
        self.label=Label(self,text="Datos Ingresados",font=("Comic Sans Ms",12))
        self.label.grid(row=0,column=0,columnspan=2,pady=20,padx=40)
        self.paneldatos= PanelMostrarDatos(self,self.datos1,self.datos2)
        self.botonWilcoxon= Button(self,text="Suma de rangos"+"\nde Wilcoxon",font=("Comic Sans Ms",8))
        self.botonMannw=Button(self,text="Prueba U de "+"\nMann–Whitney",font=("Comic Sans Ms",8)) 
        if len(self.datos1)<=len(self.datos2):
            self.botonWilcoxon.grid(row=len(self.datos2)+1,column=0,padx=40,pady=15)
            self.botonMannw.grid(row=len(self.datos2)+1,column=1,padx=40,pady=15)
        else:
            self.botonWilcoxon.grid(row=len(self.datos1)+1,column=0,padx=40,pady=15)
            self.botonMannw.grid(row=len(self.datos1)+1,column=1,padx=40,pady=15)
        self.pack(fill="y", expand=1)  
#-------------------------------------------
class VentanaResultados(Frame):
    def __init__(self, master):
        super().__init__(master)

class PanelDatos(PanedWindow):
    def __init__(self, master,ventana):
        super().__init__(master)
        self.ventana=ventana
        self.config(bg="#86E2A3")
        self.agregar = True
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
                  self.Borar(1,valor2)   
            elif valor1!=0 and valor2!=0:
                pass   
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
        if opcion ==1:
            tamaño = len(self.Lista1)
            for i in range(tamaño-1,cantidad,-1):
               aux=self.Lista1.pop(i)
               aux.grid_forget()
        elif opcion ==2: 
            tamaño = len(self.Lista2)-cantidad           
            for i in range(tamaño-1,cantidad,-1):
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
            print("datos obtenidos con exito")               
            self.ventana.CambiarVentana()                 
        except:
            messagebox.showwarning("Advertencia","Por favor ingrese valores validos"+"\n y utilize un punto ( . ) para las cifras decimales ")  
    
    def Get_Agregar(self):
        return self.agregar

    def Get_Variable1(self):
        return self.variable1

    def Get_Variable2(self):
        return self.variable2    

    def Get_BotonEnviar(self):
        return self.botonenviar

    def Set_Agregar(self,valor):
        self.agregar=valor

class PanelMostrarDatos(PanedWindow):
    
    def __init__(self, master,datos1,datos2):
        super().__init__(master,)
        self.variable1=datos1
        self.variable2=datos2
        self.Componentes()

    def Componentes(self):
        for row in range(1):
            for column in range(2):
                label = Label(self, text="Variable : " + str(column+1),bg="#86E2A3",fg="white")
                label.config(font=('Arial', 12))
                label.grid(row=row, column=column, sticky="nsew",padx=1, pady=1)
                self.grid_columnconfigure(column, weight=1)

        for i in range(len(self.Get_Variable1())):
            label = Label(self, text=str(self.Get_Variable1()[i]),bg="#86E2A3",fg="white")
            label.config(font=('Arial', 12))
            label.grid(row=i+1, column=0, sticky="nsew",padx=1, pady=1)

        for j in range(len(self.Get_Variable2())):
            label = Label(self, text=str(self.Get_Variable2()[j]),bg="#86E2A3",fg="white")
            label.config(font=('Arial', 12))
            label.grid(row=j+1, column=1, sticky="nsew",padx=1, pady=1) 
        self.grid(row=1,column=0,columnspan=2)



    def Get_Variable1(self):
       return self.variable1

    def Get_Variable2(self):
       return self.variable2   

#-------------------------------------

if __name__ == "__main__":  
    Raiz()
  
  

 
