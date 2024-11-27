import socket  # Importamos el módulo socket

def servidor_simple():
    # Configuración del servidor
    host = "0.0.0.0"  # Escucha en todas las interfaces de red disponibles
    puerto = 65432     # Puerto donde el servidor estará escuchando

    # Crear un socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Asociar el socket al host y puerto configurados
    servidor_socket.bind((host, puerto))
    print(f"Servidor iniciado en {host}:{puerto}")
    
    # Escuchar conexiones entrantes
    servidor_socket.listen(1)  # Permitir hasta 1 conexión en cola
    print("Esperando conexiones...")

    try:
        while True:
            # Aceptar una nueva conexión. Este método detiene la ejecución del programa hasta 
            # que un cliente intente conectarse al servidor.
            """
            Cuando un cliente se conecta, el método devuelve:
            conexion: Un nuevo socket específico para la comunicación con ese cliente.
            direccion_cliente: Una tupla que contiene:
                La dirección IP del cliente.
                El puerto que el cliente está usando para comunicarse con el servidor.
            """
            conexion, direccion_cliente = servidor_socket.accept()

            print(f"Cliente conectado desde {direccion_cliente[0]}:{direccion_cliente[1]}")

            # Enviar un saludo al cliente
            mensaje = "¡Hola, cliente! Bienvenido al servidor.\n"
            conexion.sendall(mensaje.encode())  # Codificar el mensaje como bytes

            # Cerrar la conexión con el cliente
            conexion.close()
            print(f"Conexión cerrada con {direccion_cliente[0]}:{direccion_cliente[1]}")
    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")
    finally:
        # Cerrar el socket del servidor
        servidor_socket.close()
        print("Servidor apagado.")

# Ejecutar la función principal
if __name__ == "__main__":
    servidor_simple()
