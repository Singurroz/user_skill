# -*- coding: utf-8 -*-
from odoo import models, fields, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    number_skills = fields.Integer(string="Numero de Skills")

    def get_num_skill(self):
        pass

    # def create(self):