from odoo import fields, api, models
from odoo.exceptions import ValidationError

class moduloModel(models.Model):
    _name = 'instituto_ydlcgb.modulo'
    _description = 'Modulo a estudiar.'

    nombremodulo = fields.Char(String="Nombre del modulo.")
    horasmodulo = fields.Integer(String="Horas del modulo")

    relacion_profesor = fields.Many2one('instituto_ydlcgb.profesor',String="Profesor que imparte el módulo.")
    relacion_alumno = fields.Many2many('instituto_ydlcgb.alumno',String="Alumno que estudia el módulo.")
    