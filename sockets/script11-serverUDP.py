import socket  # Importamos el módulo socket

def servidor_udp():
    # Configuración del servidor
    host = "0.0.0.0"  # Escucha en todas las interfaces de red disponibles
    puerto = 65432    # Puerto donde el servidor estará escuchando

    # Crear un socket UDP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Asociar el socket al host y puerto configurados
    servidor_socket.bind((host, puerto))
    print(f"Servidor UDP iniciado en {host}:{puerto}")

    try:
        while True:
            print("Esperando mensajes...")

            # Recibir datos del cliente
            # recvfrom devuelve los datos y la dirección del cliente
            datos, direccion_cliente = servidor_socket.recvfrom(1024)  # Tamaño máximo del buffer: 1024 bytes

            print(f"Mensaje recibido de {direccion_cliente[0]}:{direccion_cliente[1]}: {datos.decode()}")

            # Enviar una respuesta al cliente
            mensaje_respuesta = "¡Hola, cliente! Mensaje recibido correctamente.\n"
            servidor_socket.sendto(mensaje_respuesta.encode(), direccion_cliente)
            print(f"Respuesta enviada a {direccion_cliente[0]}:{direccion_cliente[1]}")
    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")
    finally:
        # Cerrar el socket del servidor
        servidor_socket.close()
        print("Servidor UDP apagado.")

# Ejecutar la función principal
if __name__ == "__main__":
    servidor_udp()
