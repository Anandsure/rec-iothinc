# Generated by Django 3.0 on 2019-12-05 13:11

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
                ('reg', models.CharField(blank=True, default='', max_length=100)),
                ('skills', models.IntegerField(max_length=10)),
                ('capability', models.IntegerField(max_length=10)),
                ('depth', models.IntegerField(max_length=10)),
                ('tech', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('manage', models.BooleanField(default=False)),
                ('final_bool', models.BooleanField(default=False)),
                ('final_review', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
