# -*- coding: utf-8 -*-
from odoo import api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        context = self.env.context
        property_id = context.get('property_id')
        if property_id:
            partner_ids = self.env['product.template'].search(
                [('id', '=', property_id)]).mapped('customer_id').ids
            args += [('id', 'in', partner_ids)]
        res = super(ResPartner, self)._name_search(
            name=name, args=args, operator=operator, limit=limit)
        return res
