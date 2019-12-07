# Generated by Django 3.0 on 2019-12-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('register_number', models.CharField(blank=True, default='', max_length=100)),
                ('email_id', models.CharField(max_length=253)),
                ('phone', models.IntegerField()),
                ('tech', models.BooleanField(default=False)),
                ('mgt', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
