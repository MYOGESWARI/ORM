# Generated by Django 5.1.2 on 2024-10-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('cid', models.CharField(max_length=20, primary_key='eid', serialize=False)),
                ('accountnumber', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]