# Generated by Django 3.2.13 on 2022-05-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nybro23text',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
