# Generated by Django 2.2.7 on 2020-01-11 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField(max_length=100)),
                ('grade', models.IntegerField()),
                ('Exam', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
                ('User', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_lop10', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.LOP10')),
                ('question_thpt', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.THPTQG')),
            ],
        ),
    ]
