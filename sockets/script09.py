import socket

def obtener_ip():
    # Solicitar al usuario que ingrese una URL o dominio
    url = input("Ingresa la URL o dominio (por ejemplo, www.google.com): ")

    try:
        # Obtener la dirección IP correspondiente al nombre de dominio
        ip_address = socket.gethostbyname(url)
        print(f"La dirección IP de {url} es {ip_address}")

    except socket.gaierror as e:
        print(f"Error: No se pudo resolver el dominio '{url}'. Detalles: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para obtener la IP
obtener_ip()
