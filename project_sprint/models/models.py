# from odoo import models, fields, api


# class addon_ariel_template(models.Model):
#     _name = 'addon_ariel_template.addon_ariel_template'
#     _description = 'addon_ariel_template.addon_ariel_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
