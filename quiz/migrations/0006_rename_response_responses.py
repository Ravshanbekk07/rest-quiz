# Generated by Django 4.2.5 on 2023-10-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='Responses',
        ),
    ]
