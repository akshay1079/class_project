# Generated by Django 3.0.7 on 2020-07-14 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('caddr', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=254)),
                ('cphone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pbatch_no', models.CharField(max_length=30)),
                ('pqty', models.IntegerField()),
                ('pprice', models.FloatField()),
                ('pseller', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcommerceApp.Customer')),
            ],
        ),
    ]
