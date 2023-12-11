import json
import requests

def registrar():
    url = "https://larr.cl/larr.cl/json/post7.json"
    numero = input(" ingrese numero de alumnos ")
    tipo = input("ingrese capacidad de la sala")
    ataque = input("ingrese capacidad de la sala")
    defensa = input("ingrese capacidad de la sala")
    puntos_salud = input("ingrese capacidad de la sala")
    data = {"numero": numero, "tipo": tipo, "ataque": ataque, "defensa": defensa, "puntos_salud": puntos_salud}

    try:
        response = requests.post(url, data)
        response.raise_for_status()
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
    url = "https://larr.cl/larr.cl/json/post7.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for p in data:
            print("--------")
            print(f"ID: {p['id']}")
            print(f"nombre: {p['nombre']}")
            print(f"numero: {p['numero']}")
            print(f"capacidad: {p['capacidad']}")
    except requests.exceptions.HTTPError as errh:
        print("Error HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error de Conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("Error de Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Error", err)

def main():
    termino = False

    while not termino:
        print("1.- Registrar sala")
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


