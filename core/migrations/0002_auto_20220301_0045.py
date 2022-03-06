# Generated by Django 3.2 on 2022-02-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='Guardian_phone',
            field=models.CharField(default=1, max_length=11, verbose_name='অভিভাবক মোবাইল নম্বর'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='মোবাইল নম্বর'),
        ),
    ]