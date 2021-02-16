# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    customer_id = fields.Many2one('res.partner', 'Customer')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        context = self.env.context
        customer_id = context.get('customer_id')
        if customer_id:
            property_ids = self.search(
                [('customer_id', '=', customer_id)]).ids
            args += [('id', 'in', property_ids)]
        res = super(ProductTemplate, self)._name_search(
            name=name, args=args, operator=operator, limit=limit)
        return res
