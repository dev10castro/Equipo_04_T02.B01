class Tarea:
    """
    Clase que representa una tarea.
    """

    def __init__(self, nombre, descripcion, idusuario, activa, estado):
        self._nombre = nombre
        self._descripcion = descripcion
        self._idusuario = idusuario
        self._activa = activa
        self._estado = estado

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def idusuario(self):
        return self._idusuario

    @property
    def activa(self):
        return self._activa

    @property
    def estado(self):
        return self._estado

    # Setters
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @idusuario.setter
    def idusuario(self, value):
        self._idusuario = value

    @activa.setter
    def activa(self, value):
        self._activa = value

    @estado.setter
    def estado(self, value):
        self._estado = value

    def __repr__(self):
        return (f"Tarea(nombre={self._nombre}, descripcion={self._descripcion}, "
                f"idusuario={self._idusuario}, activa={self._activa}, estado={self._estado})")
