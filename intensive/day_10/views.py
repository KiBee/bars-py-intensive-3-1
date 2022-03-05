from django.http import JsonResponse
import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def eval_expr(expr):
    """
    eval expr и eval - функции для безопасного подсчета
    выражения в строке (без использования eval())
    """

    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def calc(request):
    """
    Представление которому в параметре запроса maths через разделитель перечисляются простейшие арифметические операции
    например maths=3*3,10-2,10/5
    по умолчанию в качестве символа разделителя выступает сивол запятой.
    В необязательном параметре delimiter указывается символ разделителя арифметических операций
    например calc/?maths=3*3;10-2;10/5&delimiter=;

    Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
    """

    dict_request = dict(request.GET)
    delimeter = dict_request.get('delimiter')[0] if dict_request.get('delimiter') else ','
    expressions_list = dict_request['maths'][0].split(delimeter)
    answers_list = list(map(eval_expr, expressions_list))

    response = JsonResponse({x: y for x, y in list(zip(expressions_list, answers_list))})

    return response
