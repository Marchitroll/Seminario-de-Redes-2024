import socket  # Importamos el módulo socket

def cliente_udp():
    # Configuración del servidor al que nos conectaremos
    host = "127.0.0.1"  # Dirección del servidor (local en este caso)
    puerto = 65432      # Puerto del servidor (debe coincidir con el del servidor UDP)

    try:
        # Crear un socket UDP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Mensaje que se enviará al servidor
        mensaje = "Hola desde el cliente UDP"
        print(f"Enviando mensaje al servidor {host}:{puerto}: {mensaje}")
        
        # Enviar el mensaje al servidor
        cliente_socket.sendto(mensaje.encode(), (host, puerto))

        # Recibir la respuesta del servidor
        # recvfrom devuelve los datos y la dirección del servidor que los envió
        respuesta, direccion_servidor = cliente_socket.recvfrom(1024)  # Tamaño máximo del buffer: 1024 bytes
        print(f"Respuesta recibida del servidor {direccion_servidor[0]}:{direccion_servidor[1]}: {respuesta.decode()}")

    except socket.error as e:
        print(f"Error al comunicarse con el servidor: {e}")

    finally:
        # Cerrar el socket
        cliente_socket.close()
        print("Conexión cerrada.")

# Ejecutar la función principal
if __name__ == "__main__":
    cliente_udp()
