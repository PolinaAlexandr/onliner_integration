from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    icode_integration_by_integration_token = fields.Char()

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res['icode_onliner_by_integration_token'] = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token',
                                                                                 default='')

        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('icode_onliner_by_integration.token', self.icode_onliner_by_integration_token)

        super(ResConfigSettings, self).set_values()