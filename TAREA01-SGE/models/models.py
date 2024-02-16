# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="tarea"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    tarea = fields.Char()
    prioridad = fields.Integer()
    #Indicamos que este valor es computado y se computara con la funcion "_value_urgente"
    #Con store=True indicamos que pese a ser computado, cada vez que se compute se guarde en la base de datos
    #esto se hace para que podamos utilizar el campo en busquedas, filtrados y ordenaciones
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    portada = fields.Image(string="Foto Tarea", max_width=175, max_height=175)

    date_assign = fields.Date(string="Fecha inicio")
    date_end = fields.Date(string="Fecha fin")

    #Este es un ejemplo de "valor computado." Este computo depende de la variable prioridad.
    #La dependencia se indica mediante el decorador
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente.
    #Recibe "self" que se refiere al modelo completo (no a un registro solo)
    def _value_urgente(self):
        #Para cada registro... (recordamos, self es el modelo, no un registro)
        for record in self:
            #Si la prioridad es mayor que 50, se considera urgente, en otro caso no lo es
            if record.prioridad>50:
                record.urgente = True
            else:
                record.urgente = False

    
    @api.constrains('date_end')
    @api.depends('date_assign')
    def _check_release_date(self):
        for record in self:
            if record.date_end < record.date_assign:
                raise models.ValidationError('La fecha no puede ser antes, no tiene sentido xd.')

