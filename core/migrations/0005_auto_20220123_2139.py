# Generated by Django 3.2 on 2022-01-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220123_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Title',
            field=models.CharField(max_length=50, verbose_name='শীরনাম'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=500, verbose_name='বর্ণনা'),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_year',
            field=models.CharField(max_length=50, verbose_name='শীরনাম'),
        ),
    ]