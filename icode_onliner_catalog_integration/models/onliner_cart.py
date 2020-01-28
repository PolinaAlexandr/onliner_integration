from odoo import fields, models, api


class OnlinerCart(models.Model):
    _name = 'onliner.cart'

# def_from_request():
# summary_url = 'https://b2bapi.onliner.by/positions/{}?access-token={}'
#          headers = {'Content-Type': 'application/json'
#          token = self.env['ir.config_parameter'].sudo().get_param('icode_onliner_by_integration.token', default='')
#          # response_egr = requests.get(egr_url.format(unp, token))
#          # res_egr = json.loads(response_egr.content.decode('utf-8'))
#          response_summary = requests.get(summary_url.format(unp, token))
#          res_summary = json.loads(response_summary.content.decode('utf-8'))
#          # print(res_egr)
#          # return res_egr
#          print(res_summary)
#          return res_summary
#
def set_cart_value():
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

    total_info = 'Количество заказов: {}'.format(orders_data['total'])

    page_info = '\nПарамметры страницы:\nОграничение: {},\n Количество элементов: {},\nТекущий элемент: {},\
                 \n Последний элемент: {}\n'.format(orders_data['page']['limit'], orders_data['page']['items'],
                                                    orders_data['page']['current'], orders_data['page']['last'])

    orders_info = '\nЗаказы:\n'
    for i in orders_data['orders']:
        orders_info += ('\nУникальный код заказа: {},\nСтроковый код статуса: {},\nВремя создания заказа: {},\
                  \nВремя изменения заказа: {},\nВремя, до которого магазин должен обработать заказ: {},\
                  \nСколько секунд осталось до окончания обработки заказа или 0, если время обработки истекло: {},\
                  \nКоличество позиций в заказе: {}, Общее количество товаров в заказе: {},\nОбщая стоимость заказа: {},\
                  \nОбщий комментарий пользователя к данному заказу: {},\nИмена товаров в заказе: {},\
                  \nID позиции в заказе: {}'.format(i['key'], i['status'], i['created_at'], i['updated_at'],
                                                    i['process_deadline'], i['process_time_left'], i['positions_count'],
                                                    i['total_quantity'], i['order_cost'], i['comment'], i['product_names'],
                                                    i['positions.entry_id']))

    full_info='{}{}{}'.format(total_info, page_info, orders_info)
    print(full_info)


