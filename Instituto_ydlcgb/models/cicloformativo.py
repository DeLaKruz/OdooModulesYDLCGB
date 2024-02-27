from odoo import fields, api, models
from odoo.exceptions import ValidationError

class cicloformativoModel(models.Model):
    _name = 'instituto_ydlcgb.cicloformativo'
    _description = 'Ciclo formativo del instituto.'

    nombre_ciclo = fields.Char(String="Nombre del modulo.")
    modulos_ciclo = fields.Many2one('instituto_ydlcgb.modulo',String="Módulos del ciclo.")
