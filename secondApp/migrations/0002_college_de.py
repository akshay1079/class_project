# Generated by Django 3.0.7 on 2020-07-13 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_De',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rn', models.IntegerField()),
                ('brnch', models.CharField(max_length=30)),
                ('addr', models.CharField(max_length=30)),
                ('yr', models.IntegerField()),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='secondApp.college')),
            ],
        ),
    ]