import json

from django.db.models import (
    F,
    Q,
    Count,
    Value,
)
from django.http import (
    JsonResponse,
)
from django.shortcuts import (
    render,
)
from django.views import (
    View,
)

from recipes.models import CookStep, RecipeProduct
from users.models import Author, CustomUser


class Task1View(View):
    """
    Вывести список всех рецептов. Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта.
    """

    def get(self, request, **kwargs):
        recipes = Author.objects.filter(
            ~Q(userrecipe__recipe__isnull=True)
        ).values_list(
            'email',
            'userrecipe__recipe__title',
            'userrecipe__recipe__description'
        )
        recipes = list(recipes)

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строку ниже
        # return render(request, 'task.html', {'json_data': json.dumps(dict(recipes=recipes), ensure_ascii=False)})

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse

        return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False))


class Task2View(View):
    """
    Вывести детальную информацию рецепта с идентификатором 1.
    Нужно получить информацию о самом рецепте, о шагах приготовления, списке необходимых продуктов для приготовления

    Шаги представляют собой список:
        - Название шага;
        - Описание шага.

    Продукты представляют собой список:
        - Название продукта;
        - Описание продукта;
        - Количество продукта;
        - Аббревиатура единицы измерения продукта.
    """

    def get(self, request, **kwargs):
        steps = CookStep.objects.filter(
            recipe__id=1,
        ).values_list(
            'title',
            'description',
        )
        steps = list(steps)

        products = RecipeProduct.objects.filter(
            recipe__id=1,
        ).values_list(
            'product__title',
            'product__description',
            'count',
            'unit__abbreviation',
        )
        products = list(products)

        recipe_data = {
            'steps': steps,
            'products': products,
        }

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        # return render(
        #     request=request,
        #     template_name='task.html',
        #     context={'json_data': json.dumps(dict(recipe_data=recipe_data), ensure_ascii=False, default=str)},
        # )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        return JsonResponse(dict(recipe_data=recipe_data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task3View(View):
    """
    Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию.
    Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта;
        - Количество лайков.
    """

    def get(self, request, **kwargs):
        recipes = Author.objects.filter(
            ~Q(userrecipe__recipe__isnull=True)
        ).annotate(
            like_count=Count(
                'userrecipe__recipe__vote',
                filter=Q(userrecipe__recipe__vote__is_like__exact=True),
            )
        ).order_by(
            '-like_count',
        ).values_list(
            'email',
            'userrecipe__recipe__title',
            'userrecipe__recipe__description',
            'like_count',
        )
        recipes = list(recipes)

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        # return render(
        #     request=request,
        #     template_name='task.html',
        #     context={'json_data': json.dumps(dict(recipes=recipes), ensure_ascii=False, default=str)},
        # )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse

        return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task4View(View):
    """
    Вывести списки TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонке - Автор или Пользователь.

    Элементом списка авторов будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество рецептов.

    Элементом списка пользователей будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество лайков.
1
    """

    def get(self, request, **kwargs):
        authors = Author.objects.annotate(
            user_role=Value('Автор'),
            recipes_count=Count(
                'userrecipe__recipe',
                filter=~Q(userrecipe__recipe__isnull=True))
        ).order_by(
            '-recipes_count',
            'email',
        ).values_list(
            'user_role',
            'email',
            'recipes_count',
        )[:3]
        authors = list(authors)

        voters = CustomUser.objects.annotate(
            user_role=Value('Пользователь'),
            like_count=Count(
                'vote__is_like',
                filter=Q(vote__is_like=True))
        ).order_by(
            '-like_count',
            'email',
        ).values_list(
            'user_role',
            'email',
            'like_count',
        )[:3]
        voters = list(voters)

        data = {
            'authors': authors,
            'voters': voters,
        }

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        # return render(
        #     request=request,
        #     template_name='task.html',
        #     context={'json_data': json.dumps(dict(data=data), ensure_ascii=False, default=str)},
        # )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        return JsonResponse(dict(data=data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task5View(View):
    """
    Все продукты указаны для приготовления одной порции блюда. Нужно вывести список необходимых продуктов для
    приготовления блюда с идентификатором 3 в количестве пяти порций.

    Элементом списка продуктов будет являться список, содержащий следующие значения:
        - Название рецепта;
        - Описание рецепта;
        - Название продукта;
        - Количество;
        - Аббревиатура единицы измерения.
    """

    def get(self, request, **kwargs):
        recipe_products = RecipeProduct.objects.filter(
            recipe__id=3,
        ).annotate(
            count_x5=F('count') * 5
        ).values_list(
            'recipe__title',
            'recipe__description',
            'product__title',
            'count_x5',
            'unit__abbreviation'
        )
        recipe_products = list(recipe_products)

        # Если есть необходимость посмотреть на выполняемые запросы, план запросов через браузер, то нужно
        # раскомментировать строки ниже
        # return render(
        #     request=request,
        #     template_name='task.html',
        #     context={'json_data': json.dumps(dict(recipe_products=recipe_products), ensure_ascii=False, default=str)},
        # )

        # В тестах проверяется формируемый JSON, поэтому нужно возвращать JsonResponse
        return JsonResponse(
            data=dict(recipe_products=recipe_products), json_dumps_params=dict(ensure_ascii=False, default=str),
        )
