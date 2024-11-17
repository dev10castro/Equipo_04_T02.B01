# Archivo: T02_PR01/models/tarea.py

class Tarea:
    """
    Clase que representa una tarea.
    """

    def __init__(self, id, nombre, descripcion, idusuario, activa):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._idusuario = idusuario
        self._activa = activa

    # Getters
    @property
    def id(self):
        return self._id

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

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

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

    def __repr__(self):
        return (f"Tarea(id={self._id}, nombre={self._nombre}, "
                f"descripcion={self._descripcion}, idusuario={self._idusuario}, activa={self._activa})")
