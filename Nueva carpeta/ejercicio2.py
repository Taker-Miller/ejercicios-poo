import json
import requests

def validar_patente(patente):
    return len(patente) == 6

def registrar():
    url = "https://larr.cl/larr.cl/json/post3.php"

    patente = input("Ingrese patente del vehiculo: ")
    if not validar_patente(patente):
        print("Patente inválida")
        return

    marca = input("Ingrese marca del vehiculo: ")
    modelo = input("Ingrese modelo del vehiculo: ")
    cilindrada = input("Ingrese cilindrada del vehiculo: ")
    anio = input("Ingrese el año del vehiculo: ")

    data = {"patente": patente, "marca": marca, "modelo": modelo, "cilindrada": cilindrada, "anio": anio}

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
    url = "https://larr.cl/larr.cl/json/post3.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for p in data:
            print("--------")
            print(f"ID: {p['id']}")
            print(f"Patente: {p['patente']}")
            print(f"Marca: {p['marca']}")
            print(f"Modelo: {p['modelo']}")
            print(f"Cilindrada: {p['cilindrada']}")
            print(f"Año: {p['anio']}")
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
        print("1.- Registrar vehiculo")
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


