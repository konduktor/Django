# Generated by Django 3.0.8 on 2020-08-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200801_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Выспокий приоритет'), (2, 'Средний приоритет'), (3, 'Низский приоритет')], default=2, verbose_name='Приоритет'),
        ),
    ]
