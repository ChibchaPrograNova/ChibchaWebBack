# Generated by Django 4.2.7 on 2023-11-27 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_remove_domain_created_at'),
        ('Pay', '0005_remove_pay_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='id_Distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.distributor'),
        ),
    ]
