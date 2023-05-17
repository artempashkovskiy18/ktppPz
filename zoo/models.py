from django.db import models


class Excursions(models.Model):

    date = models.DateField('date')
    time = models.TimeField('time')
    phone = models.CharField('phone', max_length=250)
    name = models.CharField('name', max_length=250,default='')
    peopleAmount = models.IntegerField('amount of people')

    def __str__(self):
        return f'{self.date} {self.phone}'

    class Meta:
        verbose_name = 'Excursion'
        verbose_name_plural = 'Excursions'
        ordering = ['date']
