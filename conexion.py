import mysql.connector

class Comunicacion():

    def __init__(self):    
        self.conexion = mysql.connector.connect(user = 'root', password =  '12345',
                                            host='localHost',
                                            database = 'inventario',
                                            port = '3306')
                                            

    def insertar_productos(self, nombre, cantidad, restaurante):
        cur = self.conexion.cursor()
        sql = ''' INSERT INTO product (NAME, QUANTITY,RESTAURANT)
        VALUES('{}', '{}', '{}')'''.format(nombre, cantidad, restaurante)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def insertar_restaurante(self, nombre):
        cur = self.conexion.cursor()
        sql = ''' INSERT INTO restaurant (NAME)
        VALUES('{}')'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_restaurantes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM restaurant"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def eliminar_productos(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM product WHERE NOMBRE= {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def eliminar_restaurante(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM restaurant WHERE NAME= {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()