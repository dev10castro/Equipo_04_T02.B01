/* https://www.postgresqltutorial.com/ */

-- Crear la tabla de Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    email VARCHAR(255) PRIMARY KEY, -- El email será la clave primaria
    nombre_usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Crear la tabla de Tarea con la columna estado
CREATE TABLE IF NOT EXISTS Tarea (
    nombre VARCHAR(255) PRIMARY KEY, -- nombre de la tarea clave primaria
    description VARCHAR(255),
    idUsuario VARCHAR(255) NOT NULL,
    activa BOOLEAN DEFAULT TRUE,
    estado VARCHAR(50) DEFAULT 'Pendiente', -- Nuevo atributo 'estado'
    FOREIGN KEY (idUsuario) REFERENCES Usuarios(email) ON DELETE CASCADE
);

-- Insertar datos de prueba en la tabla Usuarios
INSERT INTO Usuarios (email, nombre_usuario, password)
VALUES
('antonio@gmail.com', 'antonio', 'usuario0?'),
('david@gmail.com', 'david', 'usuario0?'),
('pedro@gmail.com', 'pedro', 'usuario0?');

-- Insertar tareas para Antonio con las columnas activa y estado especificadas
INSERT INTO Tarea (nombre, description, idUsuario, activa, estado) VALUES
('Revisión de documentos', 'Revisar y corregir los documentos enviados por el cliente.', 'antonio@gmail.com', TRUE, 'Pendiente'),
('Preparar presentación mensual', 'Crear presentación para la reunión mensual de resultados.', 'antonio@gmail.com', TRUE, 'En proceso'),
('Actualizar base de datos', 'Actualizar la base de datos con los nuevos registros de clientes.', 'antonio@gmail.com', FALSE, 'Finalizado'),
('Reunión con el equipo', 'Coordinar reunión semanal con el equipo de desarrollo.', 'antonio@gmail.com', TRUE, 'Pendiente'),
('Enviar reporte de ventas', 'Elaborar y enviar el reporte de ventas mensual al gerente.', 'antonio@gmail.com', TRUE, 'Pendiente'),
('Investigación de mercado', 'Analizar las tendencias del mercado para ajustar la estrategia.', 'antonio@gmail.com', FALSE, 'Finalizado'),
('Responder correos pendientes', 'Revisar y responder los correos electrónicos recibidos en la semana.', 'antonio@gmail.com', TRUE, 'En proceso');

-- Insertar tareas para David con las columnas activa y estado especificadas
INSERT INTO Tarea (nombre, description, idUsuario, activa, estado) VALUES
('Revisión de inventario', 'Revisar el inventario de productos en el almacén.', 'david@gmail.com', TRUE, 'Pendiente'),
('Planificación de producción', 'Planificar las necesidades de producción para el próximo mes.', 'david@gmail.com', TRUE, 'Pendiente'),
('Capacitación del personal', 'Organizar una sesión de capacitación para el nuevo equipo.', 'david@gmail.com', FALSE, 'Finalizado'),
('Análisis de costos', 'Analizar los costos de producción y buscar áreas de mejora.', 'david@gmail.com', TRUE, 'En proceso'),
('Actualización de precios', 'Actualizar los precios de los productos según los nuevos costos.', 'david@gmail.com', TRUE, 'Pendiente'),
('Contacto con proveedores', 'Revisar y confirmar las órdenes de compra con los proveedores.', 'david@gmail.com', TRUE, 'Pendiente'),
('Elaboración de informe trimestral', 'Crear un informe con el desempeño del área en el trimestre.', 'david@gmail.com', FALSE, 'Finalizado'),
('Supervisión del proceso', 'Supervisar el proceso de ensamblaje en la planta.', 'david@gmail.com', TRUE, 'En proceso');

-- Insertar tareas para Pedro con las columnas activa y estado especificadas
INSERT INTO Tarea (nombre, description, idUsuario, activa, estado) VALUES
('Diseño de campaña publicitaria', 'Crear el diseño de la nueva campaña de marketing digital.', 'pedro@gmail.com', TRUE, 'Pendiente'),
('Revisión de redes sociales', 'Analizar el rendimiento de las publicaciones en redes sociales.', 'pedro@gmail.com', FALSE, 'Finalizado'),
('Creación de contenido', 'Desarrollar contenido para el blog de la empresa.', 'pedro@gmail.com', TRUE, 'Pendiente'),
('Revisión de SEO', 'Optimizar el SEO del sitio web de la empresa.', 'pedro@gmail.com', TRUE, 'En proceso'),
('Coordinación con diseñadores', 'Reunirse con el equipo de diseño para revisar avances.', 'pedro@gmail.com', TRUE, 'Pendiente'),
('Análisis de métricas', 'Revisar las métricas de tráfico y conversión del sitio web.', 'pedro@gmail.com', FALSE, 'Finalizado');
