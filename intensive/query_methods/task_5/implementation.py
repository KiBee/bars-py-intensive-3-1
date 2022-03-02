from decimal import (
    Decimal,
)

from django.db.models import (
    Avg,
    Sum,
    F
)

from ..models import *


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """

    result = Order.objects.filter(
        date_formation__gte=begin,
        date_formation__lte=end,
        orderitem__product__productcost__begin__lte=F('date_formation'),
        orderitem__product__productcost__end__gte=F('date_formation')
    ).exclude(
        orderitem__product__name=product
    ).annotate(
        order_sum=Sum(F('orderitem__product__productcost__value') * F('orderitem__count'))
    ).aggregate(
        Avg('order_sum')
    )

    result = result['order_sum__avg'] if result['order_sum__avg'] else Decimal(0)

    return result
