import  json
import requests 

def registrar():
    url = "https://larr.cl/larr.cl/json/post4.php"
    
    nombre =  input("ingrese nombre de animal")
    especie = input(" ingrese especie del animal")
    habitat = input("ingrese habitat")
    data = {"nombre": nombre, "especie": especie, "habitat": habitat,}


    try:
        r = requests.post(url, data)
        r.raise_for_status()
        print("Vehículo registrado con éxito.")
    except requests.exceptions.HTTPError as errh:
        print("Error HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error de Conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("Error de Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Error", err)

def mostrar():
    url = "https://larr.cl/larr.cl/json/post4.json"

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        for p in data:
            print("--------")
            print(f"ID: {p['id']}")
            print(f"nombre: {p['nombre']}")
            print(f"especie: {p['especie']}")
            print(f"habitat: {p['habitat']}")
          
    except requests.exceptions.HTTPError as errh:
        print("Error", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error de Conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("Error", errt)
    except requests.exceptions.RequestException as err:
        print("Error", err)

def main():
    termino = False

    while not termino:
        print("1.- Registrar animal")
        print("2.- Mostrar todo")
        print("3.- Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
            termino = True
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()