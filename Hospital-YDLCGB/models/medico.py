from odoo import fields, api, models
from odoo.exceptions import ValidationError

class medicoModel(models.Model):
    _name = 'hospital_ydlcgb.medico'
    _description = 'Medico de este hospital.'
    _rec_name = 'nombre'

    nombre = fields.Char(String="Nombre del paciente")
    apellidos = fields.Char(String="Apellidos del paciente")
    numero_colegiado = fields.Integer(String="Numero de colegiado")
    imagen = fields.Image(String="Foto Medico", max_width=100, max_height=100)
    pacientes = fields.Many2many('hospital_ydlcgb.paciente',String="Pacientes")