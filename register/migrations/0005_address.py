# Generated by Django 2.2.4 on 2019-08-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20190809_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.TextField(default='address')),
            ],
        ),
    ]
