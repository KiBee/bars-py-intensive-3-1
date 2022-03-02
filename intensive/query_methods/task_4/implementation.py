from django.db.models import (
    Sum,
    Max,
)

from ..models import *


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """

    result = Product.objects.filter(
        orderitem__order__date_formation__gte=begin,
        orderitem__order__date_formation__lte=end,
    ).annotate(
        count_sum=Sum('orderitem__count')
    )

    max_count = result.aggregate(Max('count_sum'))['count_sum__max']

    result = list(
        result.filter(
            count_sum=max_count,
        ).values_list(
            'name',
            'count_sum',
        )
    )

    return result
