# variables

mi_variable="mi variables de string"
print(mi_variable)

mi_int_vatiable=5
print(mi_int_vatiable)
print(type(mi_int_vatiable))

mi_int_str_variable= str(mi_int_vatiable)
print(mi_int_str_variable)
print(type(mi_int_str_variable))

mi_bool_variable=False
print(mi_variable)

#concadenacion de variables se usa la , en el print
print(mi_variable,mi_int_vatiable,mi_bool_variable)

#funciones del sistema: len() dice cuanto caracteres tiene la variable
print(len(mi_variable))

#variable en una sola linea
nombre,apellido,alias,edad="Rosa","Garcia","rg",12
print("mi alias es",alias,"mi edad es",edad,"mi nombre y apellido es",nombre,apellido)

#para que te pida los datos por consola y esos datos se guarde en variables
"""
nombre= input ("¿Cual es tu nombre?")
apellido= input ("¿cual es tu apellido?")
"""
print("Tu nombre es:", nombre,"tu apellido es",apellido)

#cambio de tipo
nombre= 35
edad = "rosa"
print(nombre,edad)

#forzamos tipo que sea string
direccion: str = "Mi direccion"
print(direccion)
direccion=32
print(type(direccion))