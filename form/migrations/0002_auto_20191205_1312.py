# Generated by Django 3.0 on 2019-12-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='capability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='depth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='skills',
            field=models.IntegerField(),
        ),
    ]
