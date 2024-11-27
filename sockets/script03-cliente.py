import socket  # Importamos el módulo socket

def cliente_simple():
    # Configuración del servidor al que nos conectaremos
    host = "127.0.0.1"  # Dirección del servidor (local en este caso)
    puerto = 65432      # Puerto del servidor (debe coincidir con el del servidor)

    try:
        # Crear un socket TCP/IP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Conectando al servidor {host}:{puerto}...")
        # Conectar al servidor
        cliente_socket.connect((host, puerto))
        print("Conexión establecida.")

        # Recibir el mensaje del servidor
        # recv(1024) le indica al cliente que reciba hasta 1024 bytes de datos desde el servidor. 
        # Es importante entender que el tamaño del búfer no significa necesariamente la cantidad exacta 
        # de datos que se recibirán.

        # Si el servidor envía más de 1024 bytes, el cliente tendrá que llamar a recv() 
        # varias veces para recibir todos los datos.
        saludo = cliente_socket.recv(1024)  # Tamaño del búfer en bytes
        print(f"Mensaje recibido del servidor: {saludo.decode()}")  # Decodificamos los bytes recibidos a texto

    except socket.error as e:
        print(f"Error al conectar con el servidor: {e}")

    finally:
        # Cerrar la conexión
        cliente_socket.close()
        print("Conexión cerrada.")

# Ejecutar la función principal
if __name__ == "__main__":
    cliente_simple()
