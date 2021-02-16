# -*- coding: utf-8 -*-
from odoo import api, models, fields


class HelpdeskTicketType(models.Model):
    _inherit = 'helpdesk.ticket.type'

    team_id = fields.Many2one('helpdesk.team', 'Helpdesk Team')


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    property_id = fields.Many2one('product.template', 'Property')
