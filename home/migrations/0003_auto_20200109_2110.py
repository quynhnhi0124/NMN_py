# Generated by Django 2.2.7 on 2020-01-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='grade',
            field=models.IntegerField(),
        ),
    ]