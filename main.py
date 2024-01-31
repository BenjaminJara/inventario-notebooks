
import tkinter as Tk
from PIL import Image, ImageTk

from tkcalendar import Calendar,DateEntry


from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END, PhotoImage
# from conexion import*



class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='Red3')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='Red3')
        self.frame4.grid(column=0, row=2)

        self.nombre_pc = StringVar()
        self.marca = StringVar()
        self.modelo = StringVar()
        self.actfijo = StringVar()
        self.fecha = StringVar()
        self.cal = DateEntry()
        self.serie = StringVar()
        self.rut = StringVar()
        self.responsable = StringVar()
        self.dotacion = StringVar()

        self.buscar = StringVar()


        # self.base_datos = Registro_datos()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'Inventario Notebooks',bg='Red3',fg='white', font=('Orbitron',20,'bold')).grid(column=0, row=0)
        
        # imagen correos
        # Cargar la imagen con Pillow
        ruta_imagen = "logocorreos2.jpg"
        imagen_pillow = Image.open(ruta_imagen)
        self.imagen_pillow = ImageTk.PhotoImage(imagen_pillow)

        # Label para la imagen
        label_imagen = Label(self.frame2, image=self.imagen_pillow, bg='white')
        label_imagen.grid(column=0, row=0, padx=40)

        # Label(self.frame2, text = 'Agregar Dispositivos',fg='white', bg ='Red3', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Marca',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=8 )
        Label(self.frame2, text = 'Modelo',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=8)
        Label(self.frame2, text = 'Activo Fijo',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=8)
        Label(self.frame2, text = 'Fecha', fg='white',bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=8)
        Label(self.frame2, text = 'Serie',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=8)
        Label(self.frame2, text = 'Rut',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=8)
        Label(self.frame2, text = 'Responsable',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=8)
        Label(self.frame2, text = 'Dotación',fg='white', bg ='Red3', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=8)


        Entry(self.frame2,textvariable=self.marca , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.modelo , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.actfijo , font=('Arial',12)).grid(column=1,row=3)

        ##CALENDARIO
        cal = DateEntry(self.frame2, width=30, year=2024, date_pattern='dd/mm/yyyy', locale='es_ES')
        cal.grid(column=1, row=4, padx=4)
        self.cal.bind('<<TreeviewSelect>>', self.obtener_fila)
        ##------------------------------------

        Entry(self.frame2,textvariable=self.serie , font=('Arial',12)).grid(column=1,row=5)
        Entry(self.frame2,textvariable=self.rut , font=('Arial',12)).grid(column=1,row=6)
        Entry(self.frame2,textvariable=self.responsable , font=('Arial',12)).grid(column=1,row=7)
        Entry(self.frame2,textvariable=self.dotacion , font=('Arial',12)).grid(column=1,row=8)


       
        # Label(self.frame4, text = 'Control',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='white').grid(column=0,row=1, pady=5, padx=4)
        ## ACTUALIZAR
        Button(self.frame4,command = self.limpiar_datos, text='ACTUALIZAR', font=('Arial',10,'bold'), bg='white').grid(column=1,row=1, padx=5)        
        Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',10,'bold'), bg='white').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial',8,'bold'), bg='white').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.buscar , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='Ver plantilla', font=('Arial',10,'bold'), bg='white').grid(columnspan=3,column=0,row=3, pady=5)


        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Marca', 'Modelo', 'Activo Fijo', 'Fecha', 'Serie', 'Rut', 'Responsable', 'Dotación')

        self.tabla.column('#0', minwidth=80, width=100, anchor='center')
        self.tabla.column('Marca', minwidth=80, width=100 , anchor='center')
        self.tabla.column('Modelo', minwidth=80, width=100, anchor='center' )
        self.tabla.column('Activo Fijo', minwidth=80, width=100 , anchor='center')
        self.tabla.column('Fecha', minwidth=80, width=100, anchor='center')
        self.tabla.column('Serie', minwidth=80, width=100, anchor='center')
        self.tabla.column('Rut', minwidth=80, width=100, anchor='center')
        self.tabla.column('Responsable', minwidth=80, width=100, anchor='center')
        self.tabla.column('Dotación', minwidth=80, width=100, anchor='center')

        self.tabla.heading('#0', text='Nombre PC', anchor ='center')
        self.tabla.heading('Marca', text='Marca', anchor ='center')
        self.tabla.heading('Modelo', text='Modelo', anchor ='center')
        self.tabla.heading('Activo Fijo', text='Activo Fijo', anchor ='center')
        self.tabla.heading('Fecha', text='Fecha', anchor ='center')
        self.tabla.heading('Serie', text='Serie', anchor ='center')
        self.tabla.heading('Rut', text='Rut', anchor ='center')
        self.tabla.heading('Responsable', text='Responsable', anchor ='center')
        self.tabla.heading('Dotación', text='Dotación', anchor ='center')



        estilo = ttk.Style(self.frame3)
        estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='black')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    def agregar_datos(self):
        self.tabla.get_children()
        nombre_pc = self.nombre_pc.get()
        marca = self.marca.get()
        modelo = self.modelo.get()
        actfijo = self.actfijo.get()
        fecha = self.fecha.get()
        serie = self.serie.get()
        rut = self.rut.get()
        responsable = self.responsable.get()
        dotacion = self.dotacion.get()
        datos = (nombre_pc, marca, modelo, actfijo, fecha, serie, rut, responsable, dotacion)
        if nombre_pc and marca and modelo and actfijo and fecha and serie and rut and responsable !='':        
            self.tabla.insert('',0, text = nombre_pc, values=datos)
            self.base_datos.inserta_producto(nombre_pc, marca, modelo, actfijo, fecha, serie, rut, responsable, dotacion)

    ## CAMBIAR A ACTUALIZAR FILA
    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.nombre_pc.set('')
        self.marca.set('')
        self.modelo.set('')
        self.actfijo.set('')
        self.fecha.set('')
        self.serie.set('')
        self.rut.set('')
        self.responsable.set('')
        self.dotacion .set('')

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])


    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_productos(nombre)


    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]

   

def main():
    ventana = Tk()
    ventana.wm_title("Inventario Notebooks Correos de Chile")


    #LOGO
    icono = ImageTk.PhotoImage(file="logo.jpg")
    # Establecerlo como ícono de la ventana.
    ventana.iconphoto(True, icono)

    #BG
    ventana.config(bg='Red3')
    ventana.geometry('1334x550')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

    

if __name__=="__main__":
    main()        

