# Generated by Django 3.2.8 on 2021-10-22 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0003_auto_20211022_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freearticle',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.author'),
        ),
    ]
