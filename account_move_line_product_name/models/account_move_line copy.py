from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.parnter'
    
    invoice_document_type = fields.Char(string="Tipo de documento elegido por el cliente")
    
