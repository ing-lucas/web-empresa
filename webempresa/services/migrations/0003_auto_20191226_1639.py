# Generated by Django 2.2.7 on 2019-12-26 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20191226_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'sevicio', 'verbose_name_plural': 'servicios'},
        ),
    ]