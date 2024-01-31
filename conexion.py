# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='bd_inventario', 
                                            user = 'root',
                                            password ='admin',
                                            port = '3306')



    def inserta_producto(self,marca, modelo, nombre_pc, actfijo, fecha, serie, rut, responsable, dotacion):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (marca, nombre_pc, modelo, actfijo, fecha, serie, rut, responsable, dotacion) 
        VALUES('{}', '{}','{}', '{}','{}','{}', '{}','{}', '{}')'''.format(marca, nombre_pc, modelo, actfijo, fecha, serie, rut, responsable, dotacion)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_pc):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_pc)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  
