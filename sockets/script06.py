import ipaddress

def obtener_informacion_ip():
    """
    Solicita una dirección IP al usuario y muestra información detallada sobre la IP ingresada.
    """
    # Solicitar al usuario que ingrese una dirección IP
    direccion_ip = input("Por favor, ingrese una dirección IP: ")

    # Convertir la dirección IP ingresada a un objeto de tipo IPv4Address
    ip = ipaddress.IPv4Address(direccion_ip)

    # Mostrar información relevante sobre la dirección IP
    print("\nInformación sobre la IP ingresada:\n")
    
    # Mostrar el número máximo de bits en la máscara de subred para la IP.
    # Por ejemplo, para una IP como 192.168.1.1, la salida será "Bits en la IP: 32"
    print(f"Bits en la IP: {ip.max_prefixlen}")
    
    # Verificar si la dirección IP es una dirección multicast.
    # Ejemplo: para una IP como 224.0.0.1, la salida será "¿Es multicast?: True"
    print(f"¿Es multicast?: {ip.is_multicast}")
    
    # Verificar si la dirección IP es privada.
    # Ejemplo: para una IP como 192.168.1.1, la salida será "¿Es privada?: True"
    print(f"¿Es privada?: {ip.is_private}")
    
    # Verificar si la dirección IP es pública.
    # Ejemplo: para una IP como 8.8.8.8 (Google), la salida será "¿Es pública?: True"
    print(f"¿Es pública?: {ip.is_global}")
    
    # Verificar si la dirección IP es no especificada (se usa para indicar que no se ha asignado una IP).
    # Ejemplo: para una IP como 0.0.0.0, la salida será "¿Es no especificada?: True"
    print(f"¿Es no especificada?: {ip.is_unspecified}")
    
    # Verificar si la dirección IP es reservada para fines especiales.
    # Ejemplo: para una IP como 240.0.0.1, la salida será "¿Es reservada?: True"
    print(f"¿Es reservada?: {ip.is_reserved}")
    
    # Verificar si la dirección IP es una dirección de loopback (usada para la comunicación interna del equipo).
    # Ejemplo: para una IP como 127.0.0.1, la salida será "¿Es loopback?: True"
    print(f"¿Es loopback?: {ip.is_loopback}")
    
    # Verificar si la dirección IP es una IP local (usada para la comunicación dentro de una red).
    # Ejemplo: para una IP como 169.254.1.1, la salida será "¿Es local (usada para comunicación dentro de una red)?: True"
    print(f"¿Es local (usada para comunicación dentro de una red | APIPA )?: {ip.is_link_local}")

    # Calcular y mostrar las IPs anteriores y siguientes
    ip_siguiente = ip + 1
    ip_anterior = ip - 1
    # Ejemplo: si la IP es 192.168.1.1, la salida será:
    # La siguiente IP es: 192.168.1.2
    # La IP anterior es: 192.168.1.0
    print(f"\nLa siguiente IP es: {ip_siguiente}")
    print(f"La IP anterior es: {ip_anterior}")

    # Comparar las IPs siguiente y anterior
    # Ejemplo: si la IP siguiente es 192.168.1.2 y la anterior es 192.168.1.0,
    # la salida será: ¿La siguiente IP (192.168.1.2) es mayor que la anterior (192.168.1.0)?: True
    print(f"¿La siguiente IP ({ip_siguiente}) es mayor que la anterior ({ip_anterior})?: {ip_siguiente > ip_anterior}")

# Ejecutar la función para obtener y mostrar la información de la IP
if __name__ == "__main__":
    obtener_informacion_ip()
