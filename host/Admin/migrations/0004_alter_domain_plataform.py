# Generated by Django 4.2.7 on 2023-11-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_alter_distributor_bank_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='plataform',
            field=models.CharField(choices=[('Windows', 'Windows'), ('Unix', 'Unix')], default='', max_length=100),
        ),
    ]
