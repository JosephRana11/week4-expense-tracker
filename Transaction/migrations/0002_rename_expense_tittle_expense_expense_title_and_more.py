# Generated by Django 4.2.4 on 2023-08-30 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense_tittle',
            new_name='expense_title',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='income_tittle',
            new_name='income_title',
        ),
    ]