# Generated by Django 3.0.4 on 2020-03-06 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200306_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bio',
        ),
    ]
