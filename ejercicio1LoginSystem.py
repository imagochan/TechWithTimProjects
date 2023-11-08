#pseudo codigo
# 1 crear un while que simule un menu y que salga al introducir 0
#, usar un case para que en cualquier otro caso se comporte normal
# luego 

#import sys
import json

option = 1
credenciales = {}

while option != 0:
    print("enter 1 for login, enter 2 for sign up, enter 3 to read credentials, enter 0 to exit")
    input_number_str = input()
    input_number_int = int(input_number_str)

    match input_number_str:
        case "0":
            #sys.exit()
            option = 0
        case "1":
            #print("login sin implementar")
            print("ingrese un nombre de usuario")
            nombre_de_usuario = input()
            print("ingrese una contraseña")
            contrasena = input()
            f = open("usuariosycontrasenas",mode="r")
            data = f.read()
            credenciales = json.loads(data)
            f.close()
            flagUsuarioExiste = False
            try:
                credenciales[nombre_de_usuario]
                flagUsuarioExiste = True
            except:
                print("no existe el usuario")
            if flagUsuarioExiste == True:
                if credenciales[nombre_de_usuario] == contrasena:
                    print("login exitoso!")
                else:
                    print("login fallido")
        case "2":
            #print("registro sin implementar")
            text_file = open("usuariosycontrasenas","w")
            print("ingrese un nombre de usuario")
            nombre_de_usuario = input()
            print("ingrese una contraseña")
            contrasena = input()
            credenciales[nombre_de_usuario] = contrasena
            print(credenciales)
            numero_de_caracteres_escritos = text_file.write(json.dumps(credenciales))
            # if numero_de_caracteres_escritos == len(nombre_de_usuario):
            #     print("exito al escribir archivo!")
            # else:
            #     print("fallo al escribir archivo")
            text_file.close()
        case "3":
            print("listar usuarios en archivo")
            f = open("usuariosycontrasenas",mode="r")
            data = f.read()
            print(type(data))
            print(data)
            credenciales = json.loads(data)
            print(type(credenciales))
            print(credenciales)
            f.close()