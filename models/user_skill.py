# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UserSkill(models.Model):
    _name = 'user_skill.user_skill'
    _description = 'user_skill.user_skill'
    _inherits = {'res.partner': 'partner_id', 'res.company': 'company_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade', string='Partner')
    name = fields.Char(string='NAME')
    skill = fields.Char(string='Skill')
    years = fields.Integer(string='Años')
    percent = fields.Float(string='Porcentaje')
    company_id = fields.Many2one('res.company', string='Compania')
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
