from odoo import fields, api, models
from odoo.exceptions import ValidationError

class alumnoModel(models.Model):
    _name = 'instituto_ydlcgb.alumno'
    _description = 'Alumno del instituto.'

    _rec_name = "nombre"
    nombre = fields.Char(String="Nombre del alumno")
    apellidos = fields.Char(String="Apellidos del alumno")
    DNI = fields.Char(String="DNI del alumno")
    modulos_estudiados = fields.Many2many('instituto_ydlcgb.modulo',String="Modulos que estudia el alumno.")