# Generated by Django 3.1.7 on 2021-06-18 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_brand'),
        ('room', '0004_auto_20210614_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomwishlistproduct',
            name='voted_by',
            field=models.ManyToManyField(related_name='voted_products', through='room.WishlistProductVote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roomorder',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('unconfirmed', 'Unconfirmed'), ('unfulfilled', 'Unfulfilled'), ('partially_fulfilled', 'Partially fulfilled'), ('partially_returned', 'Partially returned'), ('returned', 'Returned'), ('fulfilled', 'Fulfilled'), ('canceled', 'Canceled')], default='unfulfilled', max_length=32),
        ),
        migrations.AlterField(
            model_name='roomorderline',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('unconfirmed', 'Unconfirmed'), ('unfulfilled', 'Unfulfilled'), ('partially_fulfilled', 'Partially fulfilled'), ('partially_returned', 'Partially returned'), ('returned', 'Returned'), ('fulfilled', 'Fulfilled'), ('canceled', 'Canceled')], default='unfulfilled', max_length=32),
        ),
        migrations.AlterUniqueTogether(
            name='roomorderline',
            unique_together={('order', 'variant')},
        ),
    ]
