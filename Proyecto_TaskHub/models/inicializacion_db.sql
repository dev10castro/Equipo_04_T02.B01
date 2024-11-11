/* https://www.postgresqltutorial.com/ */

-- Crear la tabla de Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    email VARCHAR(255) PRIMARY KEY, -- El email será la clave primaria
    nombre_usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

create table if not exists Tarea(
	nombre varchar(255) primary key, -- nombre la tarea clave primaria
	description varchar(255),
	idUsuario VARCHAR(255) not null,
	activa boolean default true,
	FOREIGN KEY(idUsuario) references Usuarios(email) on delete cascade
);

-- Insertar datos de prueba en la tabla Usuarios
INSERT INTO Usuarios (email, nombre_usuario, password)
VALUES
('antonio@gmail.com', 'antonio', 'usuario0?'),
('david@gmail.com', 'david', 'usuario0?'),
('pedro@gmail.com', 'pedro', 'usuario0?');


-- Insertar tareas para Antonio con la columna activa especificada
INSERT INTO Tarea (nombre, description, idUsuario, activa) VALUES
('Revisión de documentos', 'Revisar y corregir los documentos enviados por el cliente.', 'antonio@gmail.com', TRUE),
('Preparar presentación mensual', 'Crear presentación para la reunión mensual de resultados.', 'antonio@gmail.com', TRUE),
('Actualizar base de datos', 'Actualizar la base de datos con los nuevos registros de clientes.', 'antonio@gmail.com', FALSE),
('Reunión con el equipo', 'Coordinar reunión semanal con el equipo de desarrollo.', 'antonio@gmail.com', TRUE),
('Enviar reporte de ventas', 'Elaborar y enviar el reporte de ventas mensual al gerente.', 'antonio@gmail.com', TRUE),
('Investigación de mercado', 'Analizar las tendencias del mercado para ajustar la estrategia.', 'antonio@gmail.com', FALSE),
('Responder correos pendientes', 'Revisar y responder los correos electrónicos recibidos en la semana.', 'antonio@gmail.com', TRUE);

-- Insertar tareas para David con la columna activa especificada
INSERT INTO Tarea (nombre, description, idUsuario, activa) VALUES
('Revisión de inventario', 'Revisar el inventario de productos en el almacén.', 'david@gmail.com', TRUE),
('Planificación de producción', 'Planificar las necesidades de producción para el próximo mes.', 'david@gmail.com', TRUE),
('Capacitación del personal', 'Organizar una sesión de capacitación para el nuevo equipo.', 'david@gmail.com', FALSE),
('Análisis de costos', 'Analizar los costos de producción y buscar áreas de mejora.', 'david@gmail.com', TRUE),
('Actualización de precios', 'Actualizar los precios de los productos según los nuevos costos.', 'david@gmail.com', TRUE),
('Contacto con proveedores', 'Revisar y confirmar las órdenes de compra con los proveedores.', 'david@gmail.com', TRUE),
('Elaboración de informe trimestral', 'Crear un informe con el desempeño del área en el trimestre.', 'david@gmail.com', FALSE),
('Supervisión del proceso', 'Supervisar el proceso de ensamblaje en la planta.', 'david@gmail.com', TRUE);

-- Insertar tareas para Pedro con la columna activa especificada
INSERT INTO Tarea (nombre, description, idUsuario, activa) VALUES
('Diseño de campaña publicitaria', 'Crear el diseño de la nueva campaña de marketing digital.', 'pedro@gmail.com', TRUE),
('Revisión de redes sociales', 'Analizar el rendimiento de las publicaciones en redes sociales.', 'pedro@gmail.com', FALSE),
('Creación de contenido', 'Desarrollar contenido para el blog de la empresa.', 'pedro@gmail.com', TRUE),
('Revisión de SEO', 'Optimizar el SEO del sitio web de la empresa.', 'pedro@gmail.com', TRUE),
('Coordinación con diseñadores', 'Reunirse con el equipo de diseño para revisar avances.', 'pedro@gmail.com', TRUE),
('Análisis de métricas', 'Revisar las métricas de tráfico y conversión del sitio web.', 'pedro@gmail.com', FALSE);
