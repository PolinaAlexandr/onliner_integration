from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    name = fields.Selection([('brest_region', 'Brest Region'), ('vitebsk_region', 'Vitebsk Region'),
                             ('gomel_region', 'Gomel Region'), ('gordno_region', 'Gordno Region'),
                             ('mogilev_region', 'Mogilev Region'), ('minsk_region', 'Minsk Region')],
                            string="Delivery Region")
    code = fields.Char()
    type = fields.Selection([('no', 'no'), ('default', 'default'), ('custom', 'custom'), ('free', 'free')])
    currency_id = fields.Many2one('res.currency', domain=[('name', '=', 'BYN')])
    amount = fields.Monetary(currency_field='currency_id', domain=[('type', '=', 'custom')])
    # icode_onliner_by_integration_token = fields.Char()

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # res['name'] = self.env['ir.config_parameter'].sudo().get_param('name', default='')
        # res['icode_onliner_by_integration_token'] = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token',
        #                                                                          default='')

        return res

    @api.model
    def set_values(self):
        # self.env['ir.config_parameter'].sudo().set_param('icode_onliner_by_integration.token', self.icode_onliner_by_integration_token)

        super(ResConfigSettings, self).set_values()
