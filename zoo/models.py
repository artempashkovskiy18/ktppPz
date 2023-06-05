from django.contrib.auth.models import User, Group
from django.db import models


def get_group(name):
    try:
        return Group.objects.get(name=name)
    except Group.DoesNotExist:
        return None


class Account(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    phone = models.CharField('phone', max_length=250)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Excursions(models.Model):
    date = models.DateField('date')
    time = models.TimeField('time')
    phone = models.CharField('phone', max_length=250)
    name = models.CharField('name', max_length=250, default='')
    peopleAmount = models.IntegerField('amount of people')
    guide = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)
    isFinished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} {self.phone}'

    class Meta:
        verbose_name = 'Excursion'
        verbose_name_plural = 'Excursions'
        ordering = ['date']
