# Generated by Django 4.2.1 on 2023-06-02 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0005_excursions_guide_excursions_isfinished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursions',
            name='guide',
            field=models.OneToOneField(limit_choices_to={'user__groups': ()}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='zoo.account'),
        ),
    ]