# Generated by Django 3.0.8 on 2020-08-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200806_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Описание'),
        ),
    ]
