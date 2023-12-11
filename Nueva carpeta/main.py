import  json
import requests 

def registrar():
    url = "https://larr.cl/larr.cl/json/post2.php"
    patente = input("Ingrese patente del vehiculo: ")
    marca = input("Ingrese marca del vehiculo: ")
    modelo = input("Ingrese modelo del vehiculo: ")
    cilindrada = input("Ingrese cilindrada del vehiculo: ")
    anio = input("Ingrese el año del vehiculo: ")

    data = {"patente": patente, "marca": marca, "modelo": modelo, "cilindrada": cilindrada, "anio": anio}

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
    url = "https://larr.cl/larr.cl/json/post2.json"

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        for p in data:
            print("--------")
            print(f"ID: {p['id']}")
            print(f"Patente: {p['patente']}")
            print(f"Marca: {p['marca']}")
            print(f"Modelo: {p['modelo']}")
            print(f"Cilindrada: {p['cilindrada']}")
            print(f"Año: {p['anio']}")
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