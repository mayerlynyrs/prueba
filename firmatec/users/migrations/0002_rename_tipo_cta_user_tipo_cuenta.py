# Generated by Django 3.2.3 on 2021-08-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tipo_cta',
            new_name='tipo_cuenta',
        ),
    ]