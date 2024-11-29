import socket

def cliente_recibe_archivo():
    servidor_host = "127.0.0.1"  # Dirección IP del servidor (cambiar si el servidor está en otra máquina)
    servidor_puerto = 65432      # Puerto del servidor (debe coincidir con el del servidor)

    # Crear el socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        cliente_socket.connect((servidor_host, servidor_puerto))
        print(f"Conectado al servidor {servidor_host}:{servidor_puerto}")

        # Nombre del archivo donde se guardará lo recibido
        archivo_guardado = "archivo_recibido.txt"

        # Abrir un archivo en modo escritura binaria para guardar los datos recibidos
        with open(archivo_guardado, "wb") as archivo:
            print(f"Recibiendo archivo desde el servidor y guardándolo como '{archivo_guardado}'...")

            # Recibir datos en bloques de 1024 bytes
            while True:
                datos = cliente_socket.recv(1024)  # Recibir hasta 1024 bytes
                if not datos:  # Si no hay más datos, salir del bucle
                    break
                datos_mayusculas = datos.decode('utf-8', errors='ignore').upper().encode('utf-8')
                archivo.write(datos_mayusculas)  # Escribir los datos recibidos en el archivo

        print(f"Archivo recibido y guardado como '{archivo_guardado}'.")

    except ConnectionError as e:
        print(f"Error de conexión: {e}")

    finally:
        # Cerrar la conexión con el servidor
        cliente_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    cliente_recibe_archivo()
