# Generated by Django 3.2.2 on 2021-08-31 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('name',), 'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('name',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
    ]