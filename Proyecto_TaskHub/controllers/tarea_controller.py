from models.crud_tarea import CRUDTarea  # CRUD para la gestión de tareas
from models.Tarea import Tarea  # Modelo de Tarea


class TareaController:
    """
    Controlador que maneja las operaciones relacionadas con las tareas,
    vinculadas a un usuario específico.
    """

    def __init__(self):
        """
        Inicializa el controlador de tareas con una instancia de CRUDTarea.
        """
        # Instancia del CRUD para realizar operaciones con la base de datos
        self.crud_tarea = CRUDTarea()
    # __init__

    def obtener_tareas_por_usuario(self, idusuario):
        """
        Método para obtener todas las tareas asociadas a un usuario.

        :param idusuario: ID del usuario cuyas tareas se desean obtener.
        :return: Lista de objetos Tarea o lista vacía si no hay tareas.
        """
        try:
            return self.crud_tarea.listar_tareas_por_usuario(idusuario)
        except Exception as error:
            print(f"Error al obtener tareas para el usuario {idusuario}: {error}")
            return []
    # obtener_tareas_por_usuario

    def agregar_tarea(self, idusuario, nombre, descripcion, activa=True, estado="Pendiente"):
        """
        Método para agregar una nueva tarea a la base de datos.

        :param idusuario: ID del usuario al que se vinculará la tarea.
        :param nombre: Nombre de la tarea.
        :param descripcion: Descripción de la tarea.
        :param activa: Indica si la tarea está activa o no (por defecto, True).
        :param estado: Estado inicial de la tarea (por defecto, "Pendiente").
        :return: True si la tarea fue agregada correctamente, False en caso de error.
        """
        try:
            return self.crud_tarea.crear_tarea(idusuario, nombre, descripcion, activa, estado)
        except Exception as error:
            print(f"Error al agregar tarea: {error}")
            return False
    # agregar_tarea

    def eliminar_tarea(self, idtarea):
        """
        Método para eliminar una tarea específica.

        :param idtarea: ID de la tarea a eliminar.
        :return: True si la tarea fue eliminada correctamente, False en caso de error.
        """
        try:
            return self.crud_tarea.eliminar_tarea(idtarea)
        except Exception as error:
            print(f"Error al eliminar tarea con ID {idtarea}: {error}")
            return False
    # eliminar_tarea

    def actualizar_tarea(self, idtarea, nombre=None, descripcion=None, activa=None, estado=None):
        """
        Método para actualizar una tarea existente.

        :param idtarea: ID de la tarea a actualizar.
        :param nombre: Nuevo nombre de la tarea (opcional).
        :param descripcion: Nueva descripción de la tarea (opcional).
        :param activa: Nuevo estado de la tarea (opcional).
        :param estado: Nuevo estado de la tarea (Pendiente, En proceso, Realizado) (opcional).
        :return: True si la tarea fue actualizada correctamente, False en caso de error.
        """
        try:
            return self.crud_tarea.actualizar_tarea(idtarea, nombre, descripcion, activa, estado)
        except Exception as error:
            print(f"Error al actualizar tarea con ID {idtarea}: {error}")
            return False
    # actualizar_tarea

    def cambiar_estado_tarea(self, idtarea, nuevo_estado):
        """
        Método para cambiar el estado de una tarea específica.

        :param idtarea: ID de la tarea cuyo estado se desea cambiar.
        :param nuevo_estado: Nuevo estado de la tarea (Pendiente, En proceso, Realizado).
        :return: True si el estado fue actualizado correctamente, False en caso de error.
        """
        try:
            if nuevo_estado not in ["Pendiente", "En proceso", "Realizado"]:
                raise ValueError("Estado no válido. Debe ser 'Pendiente', 'En proceso' o 'Realizado'.")
            return self.crud_tarea.actualizar_estado_tarea(idtarea, nuevo_estado)
        except Exception as error:
            print(f"Error al cambiar el estado de la tarea con ID {idtarea}: {error}")
            return False
    # cambiar_estado_tarea

    def obtener_tarea_por_id(self, idtarea):
        """
        Método para obtener una tarea específica por su ID.

        :param idtarea: ID de la tarea a obtener.
        :return: Objeto Tarea si se encuentra, None en caso contrario.
        """
        try:
            return self.crud_tarea.obtener_tarea_por_id(idtarea)
        except Exception as error:
            print(f"Error al obtener la tarea con ID {idtarea}: {error}")
            return None
    # obtener_tarea_por_id
