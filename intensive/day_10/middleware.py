import json

from django.http import HttpResponse
from django.http import JsonResponse
import time

from django.utils.deprecation import (
    MiddlewareMixin,
)

from sys import (
    getsizeof,
)


class StatisticMiddleware():
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)

        request_time = time.time() - start_time

        print(f'Время запроса: {request_time:.5f} сек.')
        print(f'Размер ответа: {getsizeof(response)} байт')

        return response


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if type(response) == JsonResponse:
            responce_list = []
            for key, value in json.loads(response.content).items():
                responce_list.append(f'<p>{key} = {str(value)}</p>')

            response = HttpResponse(''.join(responce_list))

        return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """

    @staticmethod
    def process_exception(exception):
        return HttpResponse(f"Ошибка: {exception}")
