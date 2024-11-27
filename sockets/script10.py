import socket

def obtener_informacion_dominio():
    # Solicitar al usuario que ingrese una dirección IP
    ip_address = input("Ingresa la dirección IP (por ejemplo, 8.8.8.8): ")

    try:
        # socket.gethostbyaddr(ip_address) devuelve una tupla con 3 valores:
        # 1. host_name: El nombre principal del dominio asociado a la IP.
        # 2. alias_list: Lista de alias adicionales para el dominio.
        # 3. ip_list: Lista de direcciones IP asociadas al dominio.
        host_name, alias_list, ip_list = socket.gethostbyaddr(ip_address)

        # Mostrar la información de manera estructurada
        print("\nInformación obtenida para la IP ingresada:")
        print(f"- Dirección IP: {ip_address}")
        print(f"- Nombre de dominio principal: {host_name}")

        # Mostrar alias si existen
        if alias_list:
            print("- Alias adicionales:")
            for alias in alias_list:
                print(f"  • {alias}")
        else:
            print("- Alias adicionales: Ninguno")

        # Mostrar las direcciones IP asociadas
        if ip_list:
            print("- Direcciones IP asociadas:")
            for ip in ip_list:
                print(f"  • {ip}")
        else:
            print("- Direcciones IP asociadas: Ninguna")

    except socket.herror as e:
        # Manejar errores de resolución inversa
        print(f"Error: No se pudo resolver el nombre de dominio para la IP '{ip_address}'. Detalles: {e}")
    except Exception as e:
        # Capturar otros errores inesperados
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutar el script
obtener_informacion_dominio()