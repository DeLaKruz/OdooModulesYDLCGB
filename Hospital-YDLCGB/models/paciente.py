from odoo import fields, api, models
from odoo.exceptions import ValidationError

class pacienteModel(models.Model):
    _name = 'hospital_ydlcgb.paciente'
    _description = 'Paciente de este hospital.'
    _rec_name = 'nombre'
    
    nombre = fields.Char(String="Nombre del paciente")
    apellidos = fields.Char(String="Apellidos del paciente")
    sintomas = fields.Char(String="Sintomas")