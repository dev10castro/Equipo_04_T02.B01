import Proyecto_TaskHub.models.db as db  # Importar el módulo db que está dentro de models para manejar la conexión a la base de datos


# Función para crear las tablas necesarias en la base de datos
def create_tables():
    """
    Crear las tablas de Usuarios si no existen en la base de datos.
    
    Se asegura de que la tabla 'usuarios' exista, de lo contrario la crea.
    """
    # Definir los comandos SQL que se ejecutarán para crear las tablas
    # Se usa 'CREATE TABLE IF NOT EXISTS' para evitar errores si la tabla ya existe
    
    # Campo 'email' como clave primaria
    # Campo 'nombre_usuario' obligatorio
    # Campo 'password' obligatorio
    commands = (
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            email VARCHAR(255) PRIMARY KEY,  
            nombre_usuario VARCHAR(255) NOT NULL,  
            password VARCHAR(255) NOT NULL  
        )
        """,
    )

    commands2 = (
        """
        create table if not exists Tarea(
        nombre varchar(255) primary key,
        description varchar(255),
        idUsuario VARCHAR(255) not null,
        activa boolean default true,
        FOREIGN KEY(idUsuario) references Usuarios(email) on delete cascade
        )
        """,
    )
    try:
        # Conectarse a la base de datos utilizando la función connect_db() del archivo db
        conn = db.connect_db()
        # Verificar si la conexión se realizó correctamente
        if conn is not None:  # Hacemos explícita la condición
            with conn.cursor() as cur:  # Usamos un cursor para ejecutar comandos SQL
                # Ejecutar cada comando dentro de la tupla 'commands'
                for command in commands:
                    cur.execute(command)  # Ejecuta el comando SQL
                conn.commit()  # Confirmar (guardar) los cambios en la base de datos
                print("Tablas usuario creada.")
            conn.close()  # Cerrar la conexión a la base de datos
        else:
            print("No se pudo conectar a la base de datos.")

        conn2 = db.connect_db()
        if conn2 is not None:
            with conn2.cursor() as cur2:

                for command2 in commands2:
                    cur2.execute(command2)
                conn2.commit()
                print("Tabla de tarea creada correctamente")
            conn2.close()
        else:
            print("No se pudo conectar a la base de datos.")

    except Exception as error:  # Capturar cualquier excepción que ocurra
        # Mostrar un mensaje de error si ocurre alguna excepción
        print(f"Error al crear las tablas: {error}")
# create_tables


# Función para insertar datos de ejemplo en la tabla 'usuarios'
def insert_data():
    """
    Insertar datos de ejemplo en la tabla 'usuarios' si no existen.
    
    Se insertan 3 usuarios de ejemplo y se utiliza 'ON CONFLICT' para evitar duplicados.
    """
    # Tupla que contiene los datos a insertar (email, nombre de usuario, contraseña)
    inserts = (
        ('antonio@gmail.com', 'antonio', 'usuario0?'),
        ('david@gmail.com', 'david', 'usuario0?'),
        ('pedro@gmail.com', 'pedro', 'usuario0?')
    )

    insertsTables = (
        ('Revisión de documentos', 'Revisar y corregir los documentos enviados por el cliente.', 'antonio@gmail.com',
         "TRUE"),
        ('Preparar presentación mensual', 'Crear presentación para la reunión mensual de resultados.',
         'antonio@gmail.com', "TRUE"),
        ('Actualizar base de datos', 'Actualizar la base de datos con los nuevos registros de clientes.',
         'antonio@gmail.com', "FALSE"),
        ('Reunión con el equipo', 'Coordinar reunión semanal con el equipo de desarrollo.', 'antonio@gmail.com', "TRUE"),
        ('Enviar reporte de ventas', 'Elaborar y enviar el reporte de ventas mensual al gerente.', 'antonio@gmail.com',
         "TRUE"),
        ('Investigación de mercado', 'Analizar las tendencias del mercado para ajustar la estrategia.',
         'antonio@gmail.com', "FALSE"),
        ('Responder correos pendientes', 'Revisar y responder los correos electrónicos recibidos en la semana.',
         'antonio@gmail.com', "TRUE"),
        ('Revisión de inventario', 'Revisar el inventario de productos en el almacén.', 'david@gmail.com', "TRUE"),
        ('Planificación de producción', 'Planificar las necesidades de producción para el próximo mes.',
         'david@gmail.com', "TRUE"),
        ('Capacitación del personal', 'Organizar una sesión de capacitación para el nuevo equipo.', 'david@gmail.com',
         "FALSE"),
        ('Análisis de costos', 'Analizar los costos de producción y buscar áreas de mejora.', 'david@gmail.com', "TRUE"),
        ('Actualización de precios', 'Actualizar los precios de los productos según los nuevos costos.',
         'david@gmail.com', "TRUE"),
        (
        'Contacto con proveedores', 'Revisar y confirmar las órdenes de compra con los proveedores.', 'david@gmail.com',
        "TRUE"),
        ('Elaboración de informe trimestral', 'Crear un informe con el desempeño del área en el trimestre.',
         'david@gmail.com', "FALSE"),
        ('Supervisión del proceso', 'Supervisar el proceso de ensamblaje en la planta.', 'david@gmail.com', "TRUE"),
        ('Diseño de campaña publicitaria', 'Crear el diseño de la nueva campaña de marketing digital.',
         'pedro@gmail.com', "TRUE"),
        ('Revisión de redes sociales', 'Analizar el rendimiento de las publicaciones en redes sociales.',
         'pedro@gmail.com', "FALSE"),
        ('Creación de contenido', 'Desarrollar contenido para el blog de la empresa.', 'pedro@gmail.com', "TRUE"),
        ('Revisión de SEO', 'Optimizar el SEO del sitio web de la empresa.', 'pedro@gmail.com', "TRUE"),
        ('Coordinación con diseñadores', 'Reunirse con el equipo de diseño para revisar avances.', 'pedro@gmail.com',
         "TRUE"),
        (
        'Análisis de métricas', 'Revisar las métricas de tráfico y conversión del sitio web.', 'pedro@gmail.com', "FALSE")

    )
    
    # Definir la consulta SQL para insertar los datos en la tabla 'usuarios'
    insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """  # Se usa 'ON CONFLICT' para evitar errores de inserción si ya existe un usuario con el mismo email.

    insert_query_tablas = """
        INSERT INTO Tarea (nombre, description, idUsuario, activa)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (nombre) DO NOTHING;
    """
    try:
        # Conectarse a la base de datos
        conn = db.connect_db()
        # Verificar si la conexión se realizó correctamente
        if conn is not None:  # Hacemos explícita la condición
            with conn.cursor() as cur:  # Crear un cursor para ejecutar comandos SQL
                # Iterar sobre los usuarios en la tupla 'inserts'
                for user in inserts:
                    cur.execute(insert_query, user)  # Ejecutar la consulta SQL para cada usuario
                conn.commit()  # Confirmar (guardar) los cambios en la base de datos
                print("Datos insertados correctamente.")
            conn.close()  # Cerrar la conexión a la base de datos
        else:
            print("No se pudo conectar a la base de datos.")

        conn2 = db.connect_db()
        if conn2 is not None:
            with conn2.cursor() as cur2:  # Crear un cursor para ejecutar comandos SQL

                for tablas in insertsTables:
                    cur2.execute(insert_query_tablas, tablas)
                conn2.commit()
                print("Datos insertados correctamente.")
            conn2.close()
        else:
            print("No se pudo conectar a la base de datos.")
    except Exception as error:  # Capturar cualquier excepción que ocurra
        # Mostrar un mensaje de error si ocurre alguna excepción
        print(f"Error al insertar datos: {error}")
# insert_data


# Función para inicializar la base de datos, creando tablas e insertando datos de ejemplo
def init_db():
    """
    Inicializar la base de datos llamando a las funciones de creación de tablas e inserción de datos.
    """
    create_tables()  # Llamar a la función que crea las tablas
    insert_data()  # Llamar a la función que inserta los datos de ejemplo
# init_db
