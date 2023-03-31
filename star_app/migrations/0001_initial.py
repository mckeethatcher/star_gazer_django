# Generated by Django 4.1.7 on 2023-03-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('astronomer', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('coordinates', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
