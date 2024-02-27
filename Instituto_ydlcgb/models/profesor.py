from odoo import fields, api, models
from odoo.exceptions import ValidationError

class alumnoModel(models.Model):
    _name = 'instituto_ydlcgb.profesor'
    _description = 'Profesor del instituto.'
    _rec_name = 'nombre'

    nombre = fields.Char(String="Nombre del profesor")
    apellidos = fields.Char(String="Apellidos del profesor")
    DNI = fields.Char(String="DNI del profesor")
    modulos_impartidos = fields.One2many('instituto_ydlcgb.modulo','relacion_profesor',String="Módulos que imparte el profesor.")
    ref_alu = fields.Many2many('instituto_ydlcgb.alumno',related='modulos_impartidos.relacion_alumno', String="Almunos y porfesores", readonly=True)