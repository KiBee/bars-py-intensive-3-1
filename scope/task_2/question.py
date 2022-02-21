"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
После выполнения кода выведется:
Test message
None

При вызове функции transmit_to_space() ей передается аргумент message, таким образом
message становится локальной переменной для transmit_to_space. При вызове функции data_transmitter()
в ней доступна переменная message, так как она является enclosing из-за того, что функция data_transmitter() находится
внутри функции transmit_to_space(). Таким образом "Test message" принтуется в функции data_transmitter(),
None же выводится по завершении transmit_to_space(), так как она ничего не возвращает.

"""