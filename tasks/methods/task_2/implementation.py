from tasks.common import MyException


class ClassFather:
    registered_list = []
    _name = None

    def get_name(self, ):
        if self not in self.registered_list or self._name is None:
            raise MyException
        else:
            return self._name

    def register(self):
        if self._name is None:
            raise MyException
        self.registered_list.append(self)
        pass


class User1(ClassFather):
    _name = 'Huey'

class User2(ClassFather):
    _name = 'Dewey'
