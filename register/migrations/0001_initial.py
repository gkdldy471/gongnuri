# Generated by Django 2.2.3 on 2019-08-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.TextField()),
                ('tele_num', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]