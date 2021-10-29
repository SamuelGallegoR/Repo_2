#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Programador(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido
        self.titulo = "Programador"

    def __str__(self):
        return str(self.titulo) + " " + str(self.nombre) + " " + str(self.apellido)


p1 = Programador("Samuel", "Gallego")
