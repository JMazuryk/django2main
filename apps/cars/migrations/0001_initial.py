# Generated by Django 4.1.1 on 2022-09-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body', models.CharField(max_length=20)),
                ('engine', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]