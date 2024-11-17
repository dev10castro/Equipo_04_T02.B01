# Archivo: T02_PR01/models/crud_tarea.py

from models import db  # Importa el módulo de conexión a la base de datos
from models.Tarea import Tarea  # Modelo para representar una tarea


class CRUDTarea:
    """
    Clase que implementa operaciones CRUD para la tabla 'tarea' en la base de datos.
    """

    def listar_tarea_por_usuario(self, idusuario):
        """
        Obtiene todas las tarea asociadas a un usuario específico.

        :param idusuario: ID del usuario cuyas tarea se desean obtener.
        :return: Lista de objetos Tarea o lista vacía si no se encuentran resultados.
        """
        query = """
        SELECT id, nombre, description, idusuario, activa
        FROM tarea
        WHERE idusuario = %s
        """
        conn = db.connect_db()
        if conn is None:
            return []

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (idusuario,))
                resultados = cursor.fetchall()
                return [Tarea(*row) for row in resultados] if resultados else []
        except Exception as error:
            print(f"Error al obtener tarea para el usuario {idusuario}: {error}")
            return []
        finally:
            db.close_connection(conn)
    # listar_tarea_por_usuario

    def crear_tarea(self, idusuario, nombre, description, activa):
        """
        Crea una nueva tarea en la base de datos.

        :param idusuario: ID del usuario al que se vincula la tarea.
        :param nombre: Nombre de la tarea.
        :param description: Descripción de la tarea.
        :param activa: Estado de la tarea (True o False).
        :return: True si la tarea fue creada correctamente, False en caso de error.
        """
        query = """
        INSERT INTO tarea (nombre, description, idusuario, activa)
        VALUES (%s, %s, %s, %s)
        """
        conn = db.connect_db()
        if conn is None:
            return False

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (nombre, description, idusuario, activa))
                conn.commit()
                return True
        except Exception as error:
            print(f"Error al crear tarea: {error}")
            return False
        finally:
            db.close_connection(conn)
    # crear_tarea

    def eliminar_tarea(self, idtarea):
        """
        Elimina una tarea de la base de datos.

        :param idtarea: ID de la tarea que se desea eliminar.
        :return: True si la tarea fue eliminada correctamente, False en caso de error.
        """
        query = "DELETE FROM tarea WHERE id = %s"
        conn = db.connect_db()
        if conn is None:
            return False

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (idtarea,))
                conn.commit()
                return True
        except Exception as error:
            print(f"Error al eliminar tarea con ID {idtarea}: {error}")
            return False
        finally:
            db.close_connection(conn)
    # eliminar_tarea

    def actualizar_tarea(self, idtarea, nombre=None, description=None, activa=None):
        """
        Actualiza los detalles de una tarea en la base de datos.

        :param idtarea: ID de la tarea a actualizar.
        :param nombre: Nuevo nombre de la tarea (opcional).
        :param description: Nueva descripción de la tarea (opcional).
        :param activa: Nuevo estado de la tarea (True o False, opcional).
        :return: True si la tarea fue actualizada correctamente, False en caso de error.
        """
        updates = []
        params = []

        if nombre:
            updates.append("nombre = %s")
            params.append(nombre)
        if description:
            updates.append("description = %s")
            params.append(description)
        if activa is not None:
            updates.append("activa = %s")
            params.append(activa)

        # Si no hay cambios, no ejecutar la consulta
        if not updates:
            return False

        query = f"UPDATE tarea SET {', '.join(updates)} WHERE id = %s"
        params.append(idtarea)

        conn = db.connect_db()
        if conn is None:
            return False

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return True
        except Exception as error:
            print(f"Error al actualizar tarea con ID {idtarea}: {error}")
            return False
        finally:
            db.close_connection(conn)
    # actualizar_tarea
