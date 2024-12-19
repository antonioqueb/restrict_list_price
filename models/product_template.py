from odoo import models, fields, api
from odoo.exceptions import AccessError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('list_price')
    def _compute_list_price_restricted(self):
        for record in self:
            if self.env.user.has_group('restrict_list_price.group_price_viewers'):
                record.list_price_restricted = record.list_price
            else:
               record.list_price_restricted = 0.0

    list_price_restricted = fields.Float(
        string='Precio de Venta',
        compute='_compute_list_price_restricted',
        readonly=True,
        store=True,
        help="Precio de venta, visible solo para miembros del grupo 'Price Viewers'"
    )