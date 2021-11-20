#Reto 5
op=1
lista=[]

def searchFil(lista):
    resultado=[]
    print("Digite la letra por la que empiezan los beneficiarios:")
    letra=input()
    for i in range (0,len(lista)):
        if i == 0 or (i % 3) == 0:
            if str((lista[i][:1])).lower() == letra.lower():
                resultado.append(lista[i])
                resultado.append(lista[i+1])
                resultado.append(lista[i+2])
            print("Listado filtrado de beneficiarios:")
            return resultado

def addUser(lista):
    if len(lista) <= 10:
        print("Digite la información del beneficiario a agregar:")
        nombre=str(input())
        cedula=int(input())
        celular=int(input())
        lista.append(nombre)
        lista.append(cedula)
        lista.append(celular)
        print("El beneficiario ha sido agregado")
    
def searchUser(lista):
    print("Digite el nombre y apellido del beneficiario a buscar:")
    nombre=input()
    for i in range (0,len(lista)):
        if i == 0 or (i % 3) == 0:
            if str(lista[i]).lower() == nombre.lower():
                return print(f"{lista[i]}\n{lista[i+1]}\n{lista[i+2]}")


def Delete(lista):
    print("Digite la cedula del beneficiario a borrar:")
    cedula=int(input())
    if cedula in lista:
        pos=lista.index(cedula)
        lista.pop(pos+1)
        lista.pop(pos)
        lista.pop(pos-1)
        print("El usuario ha sido eliminado del listado")
    

while op != 6:
    print("Menu Principal")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    print("6. Salir")

    op=int(input())
    if op == 1:
        print("Listado de beneficiarios")
        for a in lista:
            print(a)
    elif op == 2:
        for i in searchFil(lista):
            print(i)
    elif op == 3:
        addUser(lista)
    elif op == 4:
        searchUser(lista)
    elif op == 5:
        Delete(lista)
    elif op == 6:
        print("Hasta pronto")

agenda=open('agenda.txt','w',encoding='utf8')
for elemento in lista:
    agenda.write((str(elemento))+"\n")
agenda.close()