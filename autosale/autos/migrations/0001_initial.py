# Generated by Django 2.1.4 on 2018-12-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('owner', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
            ],
        ),
    ]
