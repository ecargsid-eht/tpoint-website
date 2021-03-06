# Generated by Django 3.2.8 on 2021-10-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawork', '0002_auto_20211021_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='freearticle',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datawork.subjectfield'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procourses',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datawork.subjectfield'),
            preserve_default=False,
        ),
    ]
