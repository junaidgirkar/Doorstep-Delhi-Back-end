# Generated by Django 3.1.7 on 2021-04-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='value',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]