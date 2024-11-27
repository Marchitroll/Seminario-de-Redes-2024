import ipaddress
# https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network

def obtener_parametros_red(cidr):
    try:
        # Crear un objeto IPv4Network a partir de la red CIDR proporcionada
        # La variable 'cidr' debe estar en formato de red con máscara CIDR, como por ejemplo "192.168.1.0/24".
        # El parámetro 'strict=False' permite crear una red aunque la dirección final del CIDR no sea una dirección de red exacta.
        red = ipaddress.IPv4Network(cidr, strict=False)
        
        # Mostrar los parámetros de la red

        # Muestra la dirección de la red (la primera dirección de la red)
        print(f"Red: {red.network_address}")  # Ejemplo: 192.168.1.0

        # Muestra la máscara de subred asociada con la red CIDR
        print(f"Máscara de subred: {red.netmask}")  # Ejemplo: 255.255.255.0

        # Muestra la dirección de broadcast para la red
        print(f"Dirección de broadcast: {red.broadcast_address}")  # Ejemplo: 192.168.1.255

        # Muestra el rango de direcciones válidas para hosts (excluye la dirección de red y la dirección de broadcast)
        # El método 'hosts()' devuelve un generador con las direcciones IP disponibles para hosts.
        print(f"Rango de direcciones válidas para hosts: {list(red.hosts())[0]} - {list(red.hosts())[-1]}")
        # Ejemplo: Rango de direcciones válidas para hosts: 192.168.1.1 - 192.168.1.254

        # Muestra la dirección de red (es lo mismo que red.network_address)
        print(f"Dirección de red: {red.network_address}")  # Ejemplo: 192.168.1.0

        # Muestra la dirección del primer host disponible en la red
        print(f"Dirección de primer host: {list(red.hosts())[0]}")  # Ejemplo: 192.168.1.1

        # Muestra la dirección del último host disponible en la red
        print(f"Dirección de último host: {list(red.hosts())[-1]}")  # Ejemplo: 192.168.1.254

        # Muestra la cantidad de direcciones disponibles para hosts, excluyendo la dirección de red y la de broadcast
        # El total de direcciones disponibles es 'red.num_addresses - 2' (restamos 2 por la dirección de red y la de broadcast)
        print(f"Cantidad de direcciones de host disponibles: {red.num_addresses - 2}")  # Ejemplo: 254 hosts

        # Muestra la máscara CIDR de la red (el número que sigue al '/' en el formato CIDR)
        print(f"Dirección de red CIDR: /{red.prefixlen}")  # Ejemplo: /24

        # Verifica si la red es pública
        print(f"Red pública: {'Sí' if red.is_global else 'No'}")  # Ejemplo: Red pública: Sí para una red pública

        # Verifica si la red es privada
        print(f"Red privada: {'Sí' if red.is_private else 'No'}")  # Ejemplo: Red privada: Sí para 192.168.x.x

        # Verifica si la red es de enlace local (link-local), usada para la comunicación dentro de una red sin enrutamiento
        print(f"Red de enlace local: {'Sí' if red.is_link_local else 'No'}")  # Ejemplo: No para redes públicas

    except ValueError as e:
        # Captura el error si la red CIDR no es válida y muestra un mensaje de error
        print(f"Error: La red CIDR '{cidr}' no es válida. Por favor ingresa una red CIDR válida.")

if __name__ == "__main__":
    # Solicitar al usuario la red CIDR
    # Ejemplo de entrada válida: "192.168.1.0/24"
    cidr = input("Introduce una red IPv4 en formato CIDR (por ejemplo, 192.168.1.0/24): ")
    
    # Llamar a la función para obtener los parámetros de la red
    obtener_parametros_red(cidr)
