from odoo import models, fields, api


class ProductTemplateGetProductInfoWizard(models.TransientModel):
    _name = 'product.template.get_product_info_wizard'
    product_ids = fields.Many2many('product.template', string='Selected Products')
    names = fields.Char(string='Names')

    # TODO забрать дату из файла кнопки обработчика (?)
    # TODO убрать визард нахрен за неудобство в модификации


    def send_data(self):
        pass
#         url = "https://b2bapi.onliner.by/pricelists"
#         token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
#         header = {
#             'Accept': 'application/json',
#             'Content-Type': 'application/json',
#             'Authorization': token}
#         request = requests.put(url, data, headers=header)
#         return request
