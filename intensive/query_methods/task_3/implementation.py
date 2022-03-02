from decimal import (
    Decimal,
)

from django.db.models import (
    Sum,
    F,
)

from ..models import *


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    result = Order.objects.filter(
        date_formation__gte=begin,
        date_formation__lte=end,
        orderitem__product__productcost__begin__lte=F('date_formation'),
        orderitem__product__productcost__end__gte=F('date_formation')

    ).annotate(
        order_sum=Sum(F('orderitem__product__productcost__value') * F('orderitem__count'))
    ).order_by(
        '-order_sum',
        '-number'
    ).first()

    result = (str(result.id), Decimal(int(result.order_sum))) if result else None

    return result
