# Generated by Django 3.1 on 2020-10-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_conversation_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynote',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companynote',
            name='title',
            field=models.CharField(blank=True, default='Untitled', max_length=255, null=True),
        ),
    ]
