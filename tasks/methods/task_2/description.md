Реализовать класс ClassFather с методом *get_name* и *register*, которые будут 
выполняться только для наследников(в противном случае выбрасывать исключение *MyException*). 
Наследники должны заранее зарегистрироваться 
в ClassFather посредством метода *register*. Если наследник не зарегистрирован и 
вызывается метод *get_name*, требуется выбросить исключение *MyException*, если 
зарегистрирован - возвращается атрибут *_name* класса наследника.