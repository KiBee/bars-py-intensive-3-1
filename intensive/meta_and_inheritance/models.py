from django.db import models
from django.db.models import (
    Q
)


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """

    def get_queryset(self):
        """
        Переопределенный кверисет возвращающий всех сотрудников без директоров
        """

        result = super().get_queryset().filter(director__isnull=True)
        return result


class CommonOffice(models.Model):
    """
    Абстрактная модель офиса
    """

    address = models.TextField('Адрес')
    mail = models.CharField('Адрес почты', max_length=30, )

    class Meta:
        abstract = True


class EducationOffice(CommonOffice):
    """
    Учебный офис
    """

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'education_office'


class GeneralOffice(CommonOffice):
    """
    Головной офис
    """

    name = models.TextField('Название головного офиса ')

    class Meta:
        db_table = 'office'


class Department(models.Model):
    """
    Подразделение
    """

    name = models.CharField('Наименование', max_length=30)

    education_office = models.ForeignKey(EducationOffice, on_delete=models.SET_NULL, null=True)
    office = models.ForeignKey(GeneralOffice, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'department'


class Person(models.Model):
    """
    Физическое лицо
    """

    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=30)

    class Meta:
        abstract = True


class Worker(Person):
    """
    Сотрудник
    """

    objects = WorkerManager()
    objects_all = models.Manager()
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_status(self):
        return f'{self.first_name} работает с {self.startwork_date}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'
        indexes = [
            models.Index(name='idx_fname__startw_date__isnull',
                         fields=['first_name', 'startwork_date'],
                         condition=~Q(startwork_date__isnull=True),
                         ),
        ]


class OrderedWorker(Worker):
    """
    Proxy-модель сотрудников упорядоченных по фамилии и дате приема на работу
    """

    @property
    def startwork_year(self):
        """
        Получить значение года приема на работу
        """
        result = self.startwork_date.year if self.startwork_date else None
        return result

    class Meta:
        """
        Сортировка по фамилии(first_name) и дате выхода на работу(startwork_date)
        """

        ordering = ['first_name', 'startwork_date']

        proxy = True


class Director(Worker):
    """
    Директор
    """

    objects = models.Manager()
    grade = models.IntegerField('Оценка', default=1)

    class Meta(Worker.Meta):
        db_table = 'directors'
        verbose_name = 'Директор'
