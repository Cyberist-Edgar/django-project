# Generated by Django 3.0.3 on 2020-03-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200312_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='fileName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]