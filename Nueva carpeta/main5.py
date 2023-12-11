import  json
import requests 

def registrar():
    url = "https://larr.cl/larr.cl/json/post5.php"
    
    nombre =  input("ingrese nombre de artista")
    genero = input(" ingrese genero de musica")
    anio_debut = input("ingrese año debut ")
    n_albums = input("ingrese numero de albums: ")
    data = {"nombre": nombre, "genero": genero, "anio_debut": anio_debut, "n_albums": n_albums}


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
    url = "https://larr.cl/larr.cl/json/post5.json"

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        for p in data:
            print("--------")
            print(f"ID: {p['id']}")
            print(f"nombre: {p['nombre']}")
            print(f"genero: {p['genero']}")
            print(f"año debut: {p['anio_debut']}")
            print(f"numero de albums: {p['n_albums']}")
          
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
        print("1.- Registrar cantante")
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