# -*- coding: utf-8 -*-

from odoo import models, fields, exceptions, api


class Skill(models.Model):
    _name = 'user_skill.skill'

    programming_language = fields.Char(string='Lenguaje de Programación')
    framework = fields.Char(string='Framework')

    def name_get(self):
        skill_list = []
        for skill in self:
            name = skill.programming_language + ' ' + skill.framework
            skill_list.append((skill.id, name))
        return skill_list
