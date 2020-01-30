import requests
import json
from datetime import datetime
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
    onliner_delivery_status = fields.Selection(STATUSES)
    updated_at = fields.Datetime('Last update date')


class OnlinerCart(models.Model):
    _name = 'onliner.cart'

    # key = fields.Char()
    # status = fields.Selection(STATUSES)
    # orders_info = fields.Text("Orders Info")
    # positions_count = fields.Integer('Positions quantity')
    # payment_type = fields.Selection(PAYMENT_TYPES)

    #TODO запрос на "списока" ордеров с онлайенра -> создать новые sale.orders с прокинутым уникальным ключем ->
    # запрос на информацию о конкретном заказе через ключ -> добавление дополнительной информации в SO ->
    # редектирование (обновление статусов заказа в зависимости от текущего статуса) ->
    # кнопка для запроса на обновление статуса и обработчик ответов -> получение обновленного статуса оплаты(вероятнее всего через крон)

    def get_orders_info(self):
        products_ids = self.env['product.product']
        sale_order_ids = self.env['sale.order']
        url = 'https://cart.api.onliner.by/oreders/?include=shop,positions'
        token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
        headers = {'Accept': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        response_request = requests.get(url, headers)
        response_summary = json.loads(response_request.content.decode('utf-8'))
        if response_summary:
            prdct_ids = []
            keys = []
            # statuses = []
            # creation_dates = []
            for i in response_summary['orders']:
                status = i['status']
                prdct_id = i['positions']['product']['id']
                products_id = products_ids.search([('id', '=', prdct_id)])
                key = i['key']
                creation_date = i['created_at']
                # creation_dates.append(creation_date)
                # statuses.append(status)
                prdct_ids.append(prdct_id)
                keys.append(key)
                for key in keys:
                    sale_order_id = sale_order_ids.create({
                        'order_id': key,
                        'key': key,
                        # 'updated_at': datetime.strptime(creation_date,  "%n-%d-%Y %H:%M:%S"),

                    })
                    for prdct_id in prdct_ids:
                        products_ids += products_ids.search([('id', '=', prdct_id)])
                        for item in response_summary['orders']['positions']:
                            if item['product']['id'] and products_id:
                                self.env['sale.order.line'].create({
                                    'product_id': products_id.id,
                                    'order_id': sale_order_id.id,
                                    'name': products_id.name,
                                    'product_code': products_id.default_code,
                                    'product_uom_qty': item['quantity'],
                                    'price_unit': products_id.lst_price,
                                })
                    sale_order_ids += sale_order_id

    def get_order_info(self):
        products_ids = self.env['product.product']
        sale_order_ids = self.env['sale.order']
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
                        "status": "new",
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
                                    "id": 607690,
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
            prdct_ids = []
            keys = []
            # creation_dates = []
            for i in full_orders_data['orders']:
                prdct_id = i['positions']['product']['id']
                products_id = products_ids.search([('id', '=', prdct_id)])
                key = i['key']
                # creation_date = i['created_at']
                # creation_dates.append(creation_date)
                prdct_ids.append(prdct_id)
                keys.append(key)
                for key in keys:
                    sale_order_id = sale_order_ids.create({
                        'order_id': key,
                        'key': key,
                        # 'date_order': datetime.strptime(creation_date, "%n-%d-%Y %H:%M:%S")
                    })
                    for prdct_id in prdct_ids:
                        products_ids += products_ids.search([('id', '=', prdct_id)])
                        for item in full_orders_data['orders']['positions']:
                            if item['product']['id'] and products_id:
                                self.env['sale.order.line'].create({
                                    'product_id': products_id.id,
                                    'order_id': sale_order_id.id,
                                    'name': products_id.name,
                                    'product_code': products_id.default_code,
                                    'product_uom_qty': item['quantity'],
                                    'price_unit': products_id.lst_price,
                                })
                    sale_order_ids += sale_order_id


    # # TODO нужна ли отформатированная информация(на данный момент используется только поле 'key' и то из исходного словаря)
        # total_info = 'Количество заказов: {}'.format(orders_data['total'])
        #
        # page_info = '\nПарамметры страницы:\nОграничение: {},\n Количество элементов: {},\nТекущий элемент: {},\
        #              \n Последний элемент: {}\n'.format(orders_data['page']['limit'], orders_data['page']['items'],
        #                                                 orders_data['page']['current'], orders_data['page']['last'])
        #
        # orders_info = '\nЗаказы:\n'
        # for i in orders_data['orders']:
        #     orders_info += ('\nУникальный код заказа: {},\nСтроковый код статуса: {},\nВремя создания заказа: {},\
        #               \nВремя изменения заказа: {},\nВремя, до которого магазин должен обработать заказ: {},\
        #               \nСколько секунд осталось до окончания обработки заказа или 0, если время обработки истекло: {},\
        #               \nКоличество позиций в заказе: {}, Общее количество товаров в заказе: {},\
        #               \nОбщая стоимость заказа: {},\nОбщий комментарий пользователя к данному заказу: {},\
        #               \nИмена товаров в заказе: {},\nID позиции в заказе: {}'.format(i['key'], i['status'],
        #                                                                              i['created_at'], i['updated_at'],
        #                                                                              i['process_deadline'],
        #                                                                              i['process_time_left'],
        #                                                                              i['positions_count'],
        #                                                                              i['total_quantity'], i['order_cost'],
        #                                                                              i['comment'], i['product_names'],
        #                                                                              i['positions.entry_id']))
        #
        # full_info = '{}{}{}'.format(total_info, page_info, orders_info)
        # print(full_info)


