# Generated by Django 4.1.4 on 2023-01-30 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_client_alter_user_role_event_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_contract', to='application.client'),
        ),
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(limit_choices_to={'client_contract__is_signed': True}, on_delete=django.db.models.deletion.CASCADE, to='application.client'),
        ),
    ]
