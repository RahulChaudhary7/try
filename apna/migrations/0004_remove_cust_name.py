# Generated by Django 4.2.2 on 2023-12-14 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apna', '0003_cust_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cust',
            name='name',
        ),
    ]
