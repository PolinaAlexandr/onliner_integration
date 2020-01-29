import requests
import json
from odoo import fields, models, api

STATUSES = [
    ('1', 'new'),
    ('2', 'processing'),
    ('3', 'confirmed'),
    ('4', 'shipping')
]

PAYMENT_TYPES = [
    ('1', 'cash'),
    ('2', 'terminal'),
    ('3', 'cashless')
]


class SaleOrderOnlinerKey(models.Model):
    _inherit = 'sale.order'

    key = fields.Char('Onliner Order Key')


class OnlinerCart(models.Model):
    _name = 'onliner.cart'

    key = fields.Char()
    status = fields.Selection(STATUSES)
    orders_info = fields.Text("Orders Info")
    positions_count = fields.Integer('Positions quantity')
    payment_type = fields.Selection(PAYMENT_TYPES)

    # def get_orders_info(self):
    #   url = 'https://cart.api.onliner.by/oreders'
    #   token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
    #   headers = {'Accept': 'application/json',
    #              'Authorization': 'Bearer {}'.format(token)}
    #   response_request = requests.get(url, headers)
    #   response_summary = json.loads(response_request.content.decode('utf-8'))
    #   return response_summary

    # def get_each_order_info(self, response_summary):
    #     keys = []
    #     for i in response_summary['orders']:
    #         key = i['key']
    #         keys.append(key)
    #         for key in keys:
    #             url = 'https://cart.api.onliner.by/oreders/{}'.format(key)
    #             token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token',
    #             default='')
    #             headers = {'Accept': 'application/json',
    #                        'Authorization': 'Bearer {}'.format(token)
    #                        }
    #             response_request = requests.get(url, headers)
    #             new_response_summary = json.loads(response_request.content.decode('utf-8'))
    #             return new_response_summary


    def get_orders_info(self):
        orders_data = {
            "total": 3,
            "page": {
                "limit": 50,
                "items": 3,
                "current": 1,
                "last": 1
            },
            "orders": [
                {
                    "key": "shop1_4",
                    "status": "new",
                    "created_at": "2015-10-04T10:00:00+03:00",
                    "updated_at": "2015-10-04T10:00:00+03:00",
                    "process_deadline": "2015-10-04T10:20:00+03:00",
                    "process_time_left": 60,
                    "positions_count": 0,
                    "order_cost": {
                        "amount": "0",
                        "currency": "BYN",
                        "converted": {
                            "BYN": {
                                "amount": "0.00",
                                "currency": "BYN"
                            }
                        }
                    },
                    "total_quantity": 0,
                    "comment": "",
                    "product_names": []
                },
                {
                    "key": "shop1_2",
                    "status": "confirmed",
                    "created_at": "2015-10-02T10:00:00+03:00",
                    "updated_at": "2015-10-02T10:00:00+03:00",
                    "process_deadline": "2015-10-04T10:20:00+03:00",
                    "process_time_left": 60,
                    "positions_count": 2,
                    "total_quantity": 2,
                    "order_cost": {
                        "amount": "30.00",
                        "currency": "BYN",
                        "converted": {
                            "BYN": {
                                "amount": "30.00",
                                "currency": "BYN"
                            }
                        }
                    },
                    "comment": "Доставка с 9 до 18",
                    "product_names": ["Apple iPhone 1", "Apple iPhone 2"]
                },
                {
                    "key": "shop1_1",
                    "status": "confirmed",
                    "created_at": "2015-10-01T10:00:00+03:00",
                    "updated_at": "2015-10-01T10:00:00+03:00",
                    "process_deadline": "2015-10-04T10:20:00+03:00",
                    "process_time_left": 60,
                    "positions_count": 1,
                    "total_quantity": 1,
                    "order_cost": {
                        "amount": "10.00",
                        "currency": "BYN",
                        "converted": {
                            "BYN": {
                                "amount": "10.00",
                                "currency": "BYN"
                            }
                        }
                    },
                    "comment": "",
                    "product_names": ["Apple iPhone 1"]
                }
            ]
        }
        # TODO нужна ли отформатированная информация(на данный момент используется только поле 'key' и то из исходного словаря)
        total_info = 'Количество заказов: {}'.format(orders_data['total'])

        page_info = '\nПарамметры страницы:\nОграничение: {},\n Количество элементов: {},\nТекущий элемент: {},\
                     \n Последний элемент: {}\n'.format(orders_data['page']['limit'], orders_data['page']['items'],
                                                        orders_data['page']['current'], orders_data['page']['last'])

        orders_info = '\nЗаказы:\n'
        for i in orders_data['orders']:
            orders_info += ('\nУникальный код заказа: {},\nСтроковый код статуса: {},\nВремя создания заказа: {},\
                      \nВремя изменения заказа: {},\nВремя, до которого магазин должен обработать заказ: {},\
                      \nСколько секунд осталось до окончания обработки заказа или 0, если время обработки истекло: {},\
                      \nКоличество позиций в заказе: {}, Общее количество товаров в заказе: {},\
                      \nОбщая стоимость заказа: {},\nОбщий комментарий пользователя к данному заказу: {},\
                      \nИмена товаров в заказе: {},\nID позиции в заказе: {}'.format(i['key'], i['status'],
                                                                                     i['created_at'], i['updated_at'],
                                                                                     i['process_deadline'],
                                                                                     i['process_time_left'],
                                                                                     i['positions_count'],
                                                                                     i['total_quantity'], i['order_cost'],
                                                                                     i['comment'], i['product_names'],
                                                                                     i['positions.entry_id']))

        full_info = '{}{}{}'.format(total_info, page_info, orders_info)
        print(full_info)

    def get_each_order_info(self, orders_data):
        selected_order_data = {
            "key": "qz2wa",
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
                "is_fake": false
            },
            "payment": {
                "type": "cash"
            },
            "created_at": "2015-10-14T17:20:28+03:00",
            "updated_at": "2015-10-14T17:20:28+03:00",
            "process_deadline": "2015-10-14T17:40:28+03:00",
            "is_new_flow": true,
            "status": "new",
            "positions_count": 1,
            "total_quantity": 2,
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
            "comment": "Доставка с 9 до 18"
        }

