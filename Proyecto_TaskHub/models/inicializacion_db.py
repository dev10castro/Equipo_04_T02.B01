import models.db as db  # Importar el módulo db que está dentro de models para manejar la conexión a la base de datos


# Función para crear las tablas necesarias en la base de datos
import models.db as db  # Importar el módulo db que está dentro de models para manejar la conexión a la base de datos

# Función para crear las tablas necesarias en la base de datos
def create_tables():
    """
    Crear las tablas de Usuarios si no existen en la base de datos.
    
    Se asegura de que la tabla 'usuarios' exista, de lo contrario la crea.
    """
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
        CREATE TABLE IF NOT EXISTS Tarea (
            nombre VARCHAR(255) PRIMARY KEY,
            description VARCHAR(255),
            idUsuario VARCHAR(255) NOT NULL,
            activa BOOLEAN DEFAULT TRUE,
            estado VARCHAR(50) DEFAULT 'Pendiente',
            FOREIGN KEY (idUsuario) REFERENCES Usuarios (email) ON DELETE CASCADE
        );
        """,
    )
    try:
        # Conexión para la tabla usuarios
        conn = db.connect_db()
        if conn is not None:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("Tabla usuarios creada.")
            conn.close()
        else:
            print("No se pudo conectar a la base de datos.")

        # Conexión para la tabla tareas
        conn2 = db.connect_db()
        if conn2 is not None:
            with conn2.cursor() as cur2:
                for command2 in commands2:
                    cur2.execute(command2)
                conn2.commit()
                print("Tabla de tarea creada correctamente.")
            conn2.close()
        else:
            print("No se pudo conectar a la base de datos.")

    except Exception as error:
        print(f"Error al crear las tablas: {error}")



# Función para insertar datos de ejemplo en la tabla 'usuarios'
# Función para insertar datos de ejemplo en la base de datos
def insert_data():
    """
    Insertar datos de ejemplo en las tablas de usuarios y tareas.
    """
    inserts = (
        ('antonio@gmail.com', 'antonio', 'usuario0?'),
        ('david@gmail.com', 'david', 'usuario0?'),
        ('pedro@gmail.com', 'pedro', 'usuario0?')
    )

    insertsTables = (
        ('Revisión de documentos', 'Revisar y corregir los documentos enviados por el cliente.', 'antonio@gmail.com', "TRUE", "Pendiente"),
        ('Preparar presentación mensual', 'Crear presentación para la reunión mensual de resultados.', 'antonio@gmail.com', "TRUE", "En proceso"),
        ('Actualizar base de datos', 'Actualizar la base de datos con los nuevos registros de clientes.', 'antonio@gmail.com', "FALSE", "Finalizado"),
        ('Reunión con el equipo', 'Coordinar reunión semanal con el equipo de desarrollo.', 'antonio@gmail.com', "TRUE", "Pendiente"),
        ('Enviar reporte de ventas', 'Elaborar y enviar el reporte de ventas mensual al gerente.', 'antonio@gmail.com', "TRUE", "Finalizado"),
        ('Investigación de mercado', 'Analizar las tendencias del mercado para ajustar la estrategia.',
         'antonio@gmail.com', "FALSE", "Finalizado"),
        ('Responder correos pendientes', 'Revisar y responder los correos electrónicos recibidos en la semana.',
         'antonio@gmail.com', "TRUE", "Pendiente"),
        ('Revisión de inventario', 'Revisar el inventario de productos en el almacén.', 'david@gmail.com', "TRUE", "Pendiente"),
        ('Planificación de producción', 'Planificar las necesidades de producción para el próximo mes.',
         'david@gmail.com', "TRUE", "Pendiente"),
        ('Capacitación del personal', 'Organizar una sesión de capacitación para el nuevo equipo.', 'david@gmail.com',
         "FALSE", "Finalizado"),
        ('Análisis de costos', 'Analizar los costos de producción y buscar áreas de mejora.', 'david@gmail.com', "TRUE", "Pendiente"),
        ('Actualización de precios', 'Actualizar los precios de los productos según los nuevos costos.',
         'david@gmail.com', "TRUE", "En proceso"),
        ('Contacto con proveedores', 'Revisar y confirmar las órdenes de compra con los proveedores.', 'david@gmail.com',
         "TRUE", "Pendiente"),
        ('Elaboración de informe trimestral', 'Crear un informe con el desempeño del área en el trimestre.',
         'david@gmail.com', "FALSE", "Finalizado"),
        ('Supervisión del proceso', 'Supervisar el proceso de ensamblaje en la planta.', 'david@gmail.com', "TRUE", "Pendiente"),
        ('Diseño de campaña publicitaria', 'Crear el diseño de la nueva campaña de marketing digital.',
         'pedro@gmail.com', "TRUE", "Pendiente"),
        ('Revisión de redes sociales', 'Analizar el rendimiento de las publicaciones en redes sociales.',
         'pedro@gmail.com', "FALSE", "Finalizado"),
        ('Creación de contenido', 'Desarrollar contenido para el blog de la empresa.', 'pedro@gmail.com', "TRUE", "En proceso"),
        ('Revisión de SEO', 'Optimizar el SEO del sitio web de la empresa.', 'pedro@gmail.com', "TRUE", "Pendiente"),
        ('Coordinación con diseñadores', 'Reunirse con el equipo de diseño para revisar avances.', 'pedro@gmail.com',
         "TRUE", "Pendiente"),
        ('Análisis de métricas', 'Revisar las métricas de tráfico y conversión del sitio web.', 'pedro@gmail.com', "FALSE", "Finalizado")
    )

    insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
    """

    insert_query_tablas = """
        INSERT INTO Tarea (nombre, description, idUsuario, activa, estado)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (nombre) DO NOTHING;
    """
    try:
        conn = db.connect_db()
        if conn is not None:
            with conn.cursor() as cur:
                for user in inserts:
                    cur.execute(insert_query, user)
                conn.commit()
                print("Datos de usuarios insertados correctamente.")
            conn.close()
        else:
            print("No se pudo conectar a la base de datos.")

        conn2 = db.connect_db()
        if conn2 is not None:
            with conn2.cursor() as cur2:
                for tablas in insertsTables:
                    cur2.execute(insert_query_tablas, tablas)
                conn2.commit()
                print("Datos de tareas insertados correctamente.")
            conn2.close()
        else:
            print("No se pudo conectar a la base de datos.")
    except Exception as error:
        print(f"Error al insertar datos: {error}")


# Función para inicializar la base de datos, creando tablas e insertando datos de ejemplo
def init_db():
    """
    Inicializar la base de datos llamando a las funciones de creación de tablas e inserción de datos.
    """
    create_tables()  # Llamar a la función que crea las tablas
    insert_data()  # Llamar a la función que inserta los datos de ejemplo
# init_db
