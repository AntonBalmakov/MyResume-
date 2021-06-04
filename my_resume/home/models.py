from django.db import models


class PageHit(models.Model):
    url = models.CharField(unique=True, max_length=200)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'счётчик'
        verbose_name_plural = 'счётчики'

    def __str__(self):
        return self.url


class Name(models.Model):
    """
    Имя Фамилия Фото

    """
    name = models.TextField(max_length=15, name='name')
    surname = models.TextField(max_length=15, name='surname')
    img = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имя'


class Skills(models.Model):
    """
    Навыки

    """
    skill = models.TextField(max_length=200, name='skill')

    def __str__(self):
        return "%s" % self.skill

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Study(models.Model):
    """
    Обучение

    """
    study_head = models.TextField(max_length=50, name='study_head')
    study_center = models.TextField(max_length=200, name='study_center')
    study_date = models.DateField(name='study_date', blank=True, null=True)
    study_finish_date = models.DateField(name='study_finish_date', blank=True, null=True)

    # def __str__(self):
    #     return "%s" % self.study_center

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'


class Himself(models.Model):
    """
    О себе

    """
    himself = models.TextField(max_length=300, name='himself')

    class Meta:
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'


class Certificates(models.Model):
    """
    Сертификаты

    """
    name_certif = models.TextField(max_length=100, name='name_certif', null=True)
    certificates = models.ImageField(upload_to='media', name='certificates')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Projects(models.Model):
    """
    Проекты

    """
    name_proj = models.TextField(max_length=100, name='name_proj', null=True)
    project = models.ImageField(upload_to='media')


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Contact (models.Model):
    """
    Реализация связи со мной через телеграмм.

    """
    name = models.TextField(max_length=50, name='Имя Hr')
    message_hr = models.TextField(max_length=50, name='Сообщение')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'