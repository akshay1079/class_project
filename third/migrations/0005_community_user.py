# Generated by Django 3.0.7 on 2020-07-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0004_cars_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('user', models.ManyToManyField(to='third.User')),
            ],
        ),
    ]
