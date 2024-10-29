/* https://www.postgresqltutorial.com/ */

-- Crear la tabla de Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    email VARCHAR(255) PRIMARY KEY, -- El email será la clave primaria
    nombre_usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Insertar datos de prueba en la tabla Usuarios
INSERT INTO Usuarios (email, nombre_usuario, password)
VALUES 
('usuario1@example.com', 'usuario1', 'usuario0?'),
('usuario2@example.com', 'usuario2', 'usuario0?'),
('usuario3@example.com', 'usuario3', 'usuario0?');

-- Seleccionar todos los registros de la tabla Usuarios
SELECT * FROM Usuarios;

-- Eliminar todos los registros de la tabla Usuarios sin eliminar su estructura
TRUNCATE TABLE Usuarios;

-- Eliminar la tabla Usuarios si existe
DROP TABLE IF EXISTS Usuarios;
