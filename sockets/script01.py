import socket  # Importamos el módulo socket para trabajar con conexiones en red

def conectar_google_simple():
    try:
        # Crear un socket TCP/IP
        # SOCK_STREAM -> TCP
        # SOCK_DGRAM -> UDP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Dirección y puerto del servidor al que queremos conectarnos
        host = "www.ulima.edu.pe"  # Dirección del servidor
        puerto = 80              # Puerto estándar para conexiones HTTP

        print(f"Intentando conectar a {host} en el puerto {puerto}...")
        
        # Establecer conexión con el servidor
        cliente_socket.connect((host, puerto))
        print("Conexión establecida correctamente.")  # Mensaje de confirmación

    except socket.error as e:
        # Capturamos cualquier error relacionado con el socket y lo mostramos
        print(f"Error al intentar conectar: {e}")

    finally:
        # Cerramos el socket para liberar los recursos
        cliente_socket.close()
        print("Conexión cerrada.")  # Mensaje confirmando el cierre del socket

# Ejecutar la función
if __name__ == "__main__":
    conectar_google_simple()
