# Generated by Django 3.0.4 on 2020-03-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200310_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_bio',
            field=models.TextField(help_text='Enter a bio of the author', max_length=1000, null=True),
        ),
    ]
