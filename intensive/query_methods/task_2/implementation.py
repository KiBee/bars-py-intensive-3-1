from django.db.models import (
    Count,
    Min,
)

from ..models import *


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """

    result = Customer.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).values(
        'name',
    ).annotate(
        orders_count=Count('order'),
        orders_min_date=Min('order__date_formation'),
    ).order_by(
        '-orders_count',
        'orders_min_date',
        '-name'
    ).first()

    result = (result['name'], result['orders_count']) if result else None

    return result
