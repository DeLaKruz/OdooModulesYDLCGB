from odoo import fields, api, models
from odoo.exceptions import ValidationError

class diagnosticoModel(models.Model):
    _name = 'hospital_ydlcgb.diagnostico'
    _description = 'Diagnostico realizado en este hospital.'
    
    tipo_diagnostico = fields.Char(String="Diagnostico")
    fecha_diagnostico = fields.Date(String="Fecha del diagnostico")

    relacion_medico = fields.Many2one('hospital_ydlcgb.medico',String="El medico que diagnostica")
    relacion_paciente = fields.Many2one('hospital_ydlcgb.paciente',String="Paciente atendido") 