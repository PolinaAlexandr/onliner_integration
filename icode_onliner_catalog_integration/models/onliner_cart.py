import requests
import json
from datetime import datetime
from odoo import fields, models, api, exceptions, _


class OnlinerCart(models.Model):
    _name = 'onliner.cart'

    #TODO запрос на "списока" ордеров с онлайенра -> создать новые sale.orders с прокинутым уникальным ключем ->
    # -> добавление дополнительной информации в SO(SO.line) ->
    # (обновление статусов заказа в зависимости от текущего статуса) кнопки ->
    # получение обновленного статуса оплаты(вероятнее всего через крон)

    @api.model
    def _get_orders_info(self):
        sale_order_ids = self.env['sale.order']
        invalid_status = {
            "message": "Validation failed",
            "errors": {
                "status": [
                    "Выбранное значение поля ошибочно"
                ]
            }
        }
        full_orders_data = {
                "total": 3,
                "page": {
                    "limit": 50,
                    "items": 3,
                    "current": 1,
                    "last": 1
                },
                "orders": [
                    {
                        "key": "43553",
                        "user_id": 1,
                        "contact": {
                            "name": "Пользователь Тестовый",
                            "first_name": "Пользователь",
                            "last_name": "Тестовый",
                            "email": "test@onliner.by",
                            "phone": "+375291234567"
                        },
                        "delivery": {
                            "city": "Минск",
                            "address": "пр-т Дзержинского, 55 д., 1a к., 607 кв., 2 под., 16 эт.",
                            "address_fields": {
                                "street": "пр-т Дзержинского",
                                "building": "55",
                                "apartment": "607",
                                "block": "1a",
                                "entrance": "2",
                                "floor": "16",
                                "comment": "Рабочий адрес"
                            },
                            "type": "courier_delivery",
                            "price": {
                                "amount": "3.00",
                                "currency": "BYN"
                            },
                            "days": 3,
                            "comment": "Курьер прибудет с 17:00 - 21:00",
                            "is_fake": False
                        },
                        "payment": {
                            "type": "online",
                            "status": "authorized"
                        },
                        "created_at": "2015-10-14T17:20:28+03:00",
                        "updated_at": "2015-10-14T17:20:28+03:00",
                        "process_deadline": "2015-10-14T17:40:28+03:00",
                        "process_time_left": 60,
                        "is_new_flow": True,
                        "status": "confirmed",
                        "positions_count": 1,
                        "total_quantity": 3,
                        "order_cost": {
                            "amount": "20.00",
                            "currency": "BYN",
                            "converted": {
                                "BYN": {
                                    "amount": "20.00",
                                    "currency": "BYN"
                                }
                            }
                        },
                        "comment": "",
                        "shop": {
                            "id": 668,
                            "url": "https://shop.api.onliner.by/shops/668",
                            "title": "Тестовый магазин",
                            "logo": "https://content.onliner.by/b2b/668/logotype/9be48fb27f5f8383ccb7a09c3336be8d.gif",
                            "html_url": "http://668.shop.onliner.by",
                            "reviews": {
                                "create_html_url": "http://668.shop.onliner.by/review/add"
                            }
                        },
                        "positions": [
                            {
                                "entry_id": 1,
                                "article": "NC900",
                                "position_price": {
                                    "amount": "1740.00",
                                    "currency": "BYN",
                                    "converted": {
                                        "BYN": {
                                            "amount": "1740.00",
                                            "currency": "BYN"
                                        }
                                    }
                                },
                                "quantity": 2,
                                "original_quantity": 2,
                                "is_credit": False,
                                "is_cashless": True,
                                "warranty": 12,
                                "comment": "Original. Запечатан. Never locked.Наличие цвета уточняйте. Полный заводской комплект. Поможем вырезать сим! Своевременная Доставка! Гарантия Минского СЦ!",
                                "producer": "Hon Hai Precision Industry Co. Ltd. (Foxconn) General Bonded Zone, East ZhenXing Rd., Zhengzhou Airport, Zhengzhou, Henan, China.",
                                "importer": "ООО ИМПОРТЕР",
                                "service_centers": "ООО Сервисный центр",
                                "delivery": {
                                    "town": {
                                        "delivery_price": {
                                            "amount": "0.00",
                                            "currency": "BYN",
                                            "converted": {
                                                "BYN": {
                                                    "amount": "0.00",
                                                    "currency": "BYN"
                                                }
                                            }
                                        },
                                        "time": 1
                                    },
                                    "country": {
                                        "delivery_price": {
                                            "amount": "5.00",
                                            "currency": "BYN",
                                            "converted": {
                                                "BYN": {
                                                    "amount": "5.00",
                                                    "currency": "BYN"
                                                }
                                            }
                                        },
                                        "time": 2
                                    }
                                },
                                "user_comment": "комментарий к заказу",
                                "product": {
                                    "id": 17,
                                    "key": "iphone6plus128gb",
                                    "name": "iPhone 6 Plus (128Gb)",
                                    "full_name": "Apple iPhone 6 Plus (128Gb)",
                                    "html_url": "http://catalog.onliner.by/mobile/apple/iphone6_128gb",
                                    "images": {
                                        "header": "https://content2.onliner.by/catalog/device/header/9ef7d6129330582a204ee2192b578c72.jpg",
                                        "icon": "https://content2.onliner.by/catalog/device/icon/d75663217c0b89622d66faada19c2aa7.jpg"
                                    },
                                    "description": "Apple iOS, экран 5.5\" IPS (1080x1920), ОЗУ 1 ГБ, флэш-память 128 ГБ, камера 8 Мп, аккумулятор 2915 мАч",
                                    "micro_description": "экран 5.5\" (1080x1920), ОЗУ 1 ГБ, флэш-память 128 ГБ",
                                    "url": "https://catalog.api.onliner.by/products/iphone6plus128gb",
                                    "reviews": {
                                        "create_html_url": "http://catalog.onliner.by/mobile/apple/iphone6_128gb/reviews/create"
                                    }
                                }
                            },
                        ]
                    },
                ]
            }
        if full_orders_data:
            for item in full_orders_data['orders']:
                onliner_order_key = item['key']
                onliner_delivery_state = item['status']
                contact = item['contact']
                payment_type = item['payment']['type']
                partner_id = self.env['res.partner'].search([('email', '=', contact['email'])])
                unique_key = self.env['sale.order'].search([('key', '=', onliner_order_key)])
                if not partner_id:
                    partner_id = partner_id.create({
                        'name': contact['name'],
                        'email': contact['email'],
                        'phone': contact['phone'],
                    })
                if not unique_key:
                    sale_order_id = sale_order_ids.create({
                        'name': _('New'),
                        'key': onliner_order_key,
                        'partner_id': partner_id.id,
                        'onliner_delivery_state': onliner_delivery_state,
                        'payment_type': payment_type,
                    })
                    for position in item['positions']:
                        ordered_product_id = position['product']['id']
                        product_id = self.env['product.product'].search([('id', '=', ordered_product_id)])
                        if product_id:
                            self.env['sale.order.line'].create({
                                'product_id': product_id.id,
                                'order_id': sale_order_id.id,
                                'name': product_id.product_tmpl_id.name,
                                'product_code': product_id.default_code,
                                'product_uom_qty': position['quantity'],
                                'price_unit': product_id.lst_price,
                            })
                    sale_order_ids += sale_order_id

    # @api.model
    # def get_orders_info(self):
    #     sale_order_ids = self.env['sale.order']
    #     url = 'https://cart.api.onliner.by/oreders/?include=shop,positions'
    #     token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
    #     headers = {'Accept': 'application/json',
    #                'Authorization': 'Bearer {}'.format(token)}
    #     response_request = requests.get(url, headers)
    #     shop_cancel_order
    #     if response_summary:
    #         for item in response_summary['orders']:
    #             onliner_order_key = item['key']
    #             onliner_delivery_state = item['status']
    #             contact = item['contact']
    #             partner_id = self.env['res.partner'].search([('email', '=', contact['email'])])
    #             unique_key = self.env['sale.order'].search([('key', '=', onliner_order_key)])
    #             if not partner_id:
    #                 partner_id = partner_id.create({
    #                     'name': contact['name'],
    #                     'email': contact['email'],
    #                     'phone': contact['phone'],
    #                 })
    #             if not unique_key:
    #                 sale_order_id = sale_order_ids.create({
    #                     'name': _('New'),
    #                     'key': onliner_order_key,
    #                     'partner_id': partner_id.id,
    #                     'onliner_delivery_state': onliner_delivery_state,
    #                 })
    #                 for position in item['positions']:
    #                     ordered_product_id = position['product']['id']
    #                     product_id = self.env['product.product'].search([('id', '=', ordered_product_id)])
    #                     if product_id:
    #                         self.env['sale.order.line'].create({
    #                             'product_id': product_id.id,
    #                             'order_id': sale_order_id.id,
    #                             'name': product_id.product_tmpl_id.name,
    #                             'product_code': product_id.default_code,
    #                             'product_uom_qty': position['quantity'],
    #                             'price_unit': product_id.lst_price,
    #                         })
    #                 sale_order_ids += sale_order_id
