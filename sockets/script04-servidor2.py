import socket

def servidor_envia_archivo():
    host = "0.0.0.0"  # El servidor escuchará en todas las interfaces de red
    puerto = 65432     # Puerto donde el servidor escuchará las conexiones

    # Crear el socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asociar el socket al host y puerto
    servidor_socket.bind((host, puerto))
    print(f"Servidor iniciado en {host}:{puerto}")

    # Escuchar conexiones entrantes
    servidor_socket.listen(1)
    print("Esperando conexiones...")

    # Aceptar la conexión de un cliente
    conexion, direccion_cliente = servidor_socket.accept()

    # Mostrar en consola la IP y el puerto del cliente
    print(f"Cliente conectado desde {direccion_cliente[0]}:{direccion_cliente[1]}")

    # Nombre del archivo que se enviará
    archivo_nombre = "archivo_enviado.txt"

    # Abrir el archivo y escribir en él antes de enviarlo
    archivo = open(archivo_nombre, "w")
    archivo.write(f"Conexión establecida con el cliente: {direccion_cliente[0]}:{direccion_cliente[1]}\n")
    archivo.write("Este archivo fue preparado por el servidor.\n")
    extra = input("Ingrese un mensaje extra: ")
    archivo.write(extra)
    archivo.close()  # Cerrar el archivo después de escribir

    # Enviar el archivo al cliente
    archivo = open(archivo_nombre, "rb")  # Abrir el archivo en modo lectura binaria para enviarlo
    archivo_data = archivo.read(1024)    # Leer el primer bloque de hasta 1024 bytes

    # Bucle para enviar todo el archivo al cliente en bloques
    while archivo_data:  # Mientras haya datos en el archivo
        conexion.send(archivo_data)  # Enviar el bloque leído al cliente
        archivo_data = archivo.read(1024)  # Leer el siguiente bloque de hasta 1024 bytes

    # Cerrar el archivo después de enviarlo
    archivo.close()

    print(f"Archivo enviado y registrado en {archivo_nombre}.")

    # Cerrar la conexión
    conexion.close()
    print(f"Conexión cerrada con {direccion_cliente[0]}:{direccion_cliente[1]}")

if __name__ == "__main__":
    servidor_envia_archivo()
