# Generated by Django 3.2.8 on 2021-10-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0006_coupon_orderedcourses_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedcourses',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
