# Generated by Django 3.1 on 2020-10-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201012_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnote',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
