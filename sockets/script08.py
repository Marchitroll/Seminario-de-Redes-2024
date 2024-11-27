import socket

# Obtener el nombre del host (nombre del equipo)
hostname = socket.gethostname()

# Obtener la dirección IP de la máquina (una dirección IPv4 principal)
ip_address = socket.gethostbyname(hostname)

# Obtener información detallada de las direcciones IP utilizando getaddrinfo()
addr_info = socket.getaddrinfo(hostname, None)

# Imprimir el nombre del equipo y la dirección IP principal
print(f"Nombre de tu equipo: {hostname}")
print(f"Dirección IP principal de tu equipo: {ip_address}")

# Iterar sobre la información obtenida para mostrar todas las direcciones IP
print("\nOtras direcciones IP disponibles:")
for addr in addr_info:
    # Obtener la dirección IP y el tipo de familia
    ip_address = addr[4][0]
    family = addr[1]
    
    # Verificar y mostrar la dirección según su tipo
    if family == socket.AF_INET:
        print(f"IPv4: {ip_address}")
    elif family == socket.AF_INET6:
        print(f"IPv6: {ip_address}")

