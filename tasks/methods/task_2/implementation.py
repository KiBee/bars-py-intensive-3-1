from tasks.common import MyException


class ClassFather:
    _name = None
    registered_list = []

    @classmethod
    def get_name(cls):
        if cls not in cls.registered_list:
            raise MyException
        else:
            return cls._name

    @classmethod
    def register(cls):
        if issubclass(cls, ClassFather) and cls is not ClassFather:
            cls.registered_list.append(cls)
        else:
            raise MyException


class User1(ClassFather):
    _name = 'Billy'


class User2(ClassFather):
    _name = 'Dewey'
