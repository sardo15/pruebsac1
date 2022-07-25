from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    invoice_document_type = fields.Selection([('boleta','Boleta'),('factura','Factura')],"Tipo de documento elegido por el cliente")
    