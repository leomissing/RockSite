from django.db import models


class reservasions(models.Model):
    name = models.CharField(max_length = 50)
    time =  models.DateTimeField()

    def __str__(self):
        return self.name


class zapis(models.Model):
    name = models.CharField(max_length = 50)
    START_CHOICES = (
    ('17:00','17:00'),
    ('18:30','18:30'),
    ('20:00','20:00'),
    ('21:30','21:30')
    )
    start_time =  models.CharField(max_length=50, choices=START_CHOICES, verbose_name='время начала')
    DAYS_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота','Суббота'),
        ('Воскресенье','Воскресенье')
        )
    week_day = models.CharField( max_length=50, choices=DAYS_CHOICES,  verbose_name='День недели')

    def __str__(self):
        return self.name
