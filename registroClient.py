#Author: Fonseca Ramos Angel Gabriel
#UA: Ingeniería de Software
#Grupo: 3CV17
#ESCOM

import sys

class Cliente:
	def __init__(self, alias, nombre, apellidop, apellidom, razSocial, rfc, tel, mail):
		self.alias=alias
		self.nombre=nombre
		self.apellidop=apellidop
		self.apellidom=apellidom
		self.razSocial=razSocial
		self.rfc=rfc
		self.tel=tel
		self.mail=mail

clientes = []

def printCl(index):
	print("\n1. Alias: "+clientes[index].alias)
	print("2. Nombre: "+clientes[index].nombre)
	print("3. 1er apellido: "+clientes[index].apellidop)
	print("4. 2o apellido: "+clientes[index].apellidom)
	print("5. R. social: "+clientes[index].razSocial)
	print("6. RFC: "+clientes[index].rfc)
	print("7. Correo: "+clientes[index].mail)

def getName(cl):
	return cl.nombre

def agregar():
	print("\nAgregando")
	alias = input("Alias: ")
	nombre = input("Nombre: ")
	apellidop = input("Primer apellido: ")
	apellidom = input("Segundo apellido (opcional): ")
	razSocial = input("Razón social: ")
	rfc = input("RFC: ")
	tel = input("Teléfono: ")
	mail = input("Correo: ")
	cl = Cliente(alias, nombre, apellidop, apellidom, razSocial, rfc, tel, mail)
	clientes.append(cl)
	clientes.sort(key = getName)
	print("Cliente agregado correctamente\n")
	
def modificar():
	cl = input("Alias del cliente a modificar: ")
	index = 0
	for temp in clientes:
		if temp.alias == cl:

			printCl(index)
			elec = input("¿Qué desea modificar?\n>>")
			
			if elec=="1":
				nAlias = input("Nuevo alias: ")
				temp.alias = nAlias
			elif elec=="2":
				nNombre = input("Nuevo nombre: ")
				temp.nombre = nNombre
			elif elec=="3":
				nApellidop = input("Nuevo apellido: ")
				temp.apellidop = nApellidop
			elif elec=="4":
				nApellidom = input("Nuevo apellido: ")
				temp.apellidom = nApellidom
			elif elec=="5":
				nRazSocial = input("Nueva R. social: ")
				temp.razSocial = nRazSocial
			elif elec=="6":
				nRfc = input("Nuevo RFC: ")
				temp.rfc = nRfc
			elif elec=="7":
				nMail = input("Nuevo correo: ")
				temp.mail = nMail
			else:
				print("Op. invalida")
			
			printCl(index)
			break
		index+=1

def listar():
	print("\nCLIENTES")
	for temp in clientes:
		print("\nNombre: "+temp.nombre)
		print("Alias: "+temp.alias)
		
	
def eliminar():
	cl = input("Alias del cliente a eliminar: ")
	index = 0
	for temp in clientes:
		if temp.alias == cl:
			break
		else:
			index+=1
	clientes.pop(index)
		
print("REGISTRO DE CLIENTES")
while True:
	print("Por favor ingrese la clave: ")
	key = input()
	if key == "isw2021":
		break

#***Inserción de 3 clientes de prueba***
cl0 = Cliente("JuanOro","Juan","Perez","","JuanOro SA de CV","DTEY4YU34H","5584531","fdshib@fds.com")
cl1 = Cliente("Roda","Rodrigo","Ramírez","Reyes","Roda S en CS","HFDD000599HMX","558897398","rodasse@fds.com")
cl2 = Cliente("Sefran","Sergio","Reyes","","Sefran S de RL","RERO000589HDF","558897398","sefran@mail.com")
clientes.append(cl0)
clientes.append(cl1)
clientes.append(cl2)

cond = True
while cond:
	print("\nMENU")
	print("1. Agregar cliente\n2. Modificar cliente\n3. Eliminar cliente\n4. Listar clientes\n5. Salir")
	choose = input(">>")

	if choose == "1":
		agregar()
	elif choose == "2":
		modificar()
	elif choose == "3":
		eliminar()
	elif choose == "4":
		listar()
	elif choose == "5":
		cond = False
		print("Saliendo...")
	else:
		print("Op. invalida")
