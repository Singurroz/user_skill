# -*- coding: utf-8 -*-
import base64
import io

from odoo import models, fields, exceptions, api


class UserSkill(models.Model):
    _name = 'user_skill.user_skill'
    _description = 'user_skill.user_skill'
    _inherits = {'res.partner': 'partner_id', 'res.company': 'company_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade', string='Partner')
    skill = fields.Char(string='Skill')
    years = fields.Integer(string='Años', default='0')
    percent = fields.Float(string='Porcentaje (%)', default='0.0')
    company_id = fields.Many2one('res.company', string='Compania')

    _sql_constraints = [
        ('partner_id_unique', 'UNIQUE(partner_id)', 'Registro existente'),
    ]

    def name_get(self):
        skill_list = []
        for skill in self:
            name = skill.partner_id.name + ' ' + skill.skill + ' ' + str(skill.percent)
            skill_list.append((skill.id, name))
        return skill_list


class UploadFile(models.TransientModel):
    _name = 'user_skill.upload_file'

    upload_file = fields.Binary(string='Subir fichero', required=True)
    file_name = fields.Char(string='Nombre del fichero')

    def import_file(self):
        if self.file_name:
            if '.csv' not in self.file_name:
                raise exceptions.ValidationError('El archivo debe ser un CSV')
            file = self.read_file_from_binary(self.upload_file)
            lines = file.split('\n')
            for line in lines:
                elements = line.split(';')
                if len(elements) > 1:
                    self.env['user_skill.user_skill'].create({
                        'partner_id': elements[0],
                        'name': elements[1],
                        'skill': elements[2],
                        'years': 0,
                        'percent': 0.0,
                        'company_id': elements[5],
                    })

    def read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            print(str(e))
            raise e