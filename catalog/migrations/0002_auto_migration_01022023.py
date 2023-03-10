# Generated by Django 3.2 on 2022-04-06 13:13
from django.db import transaction
from django.db import migrations
from django.utils.translation import gettext_lazy as _

category_data = [
    {'name': _('Camiseta')},
    {'name': _('Gorro')},
]

brand_data = [
    {'name': _('Zara')},
    {'name': _('H&M')},
    {'name': _('Nike')},
    {'name': _('Adidas')},
]

color_data = [
    {'name': 'Blanco', 'code': ''},
    {'name': 'Negro', 'code': ''},
    {'name': 'Azul', 'code': ''},
    {'name': 'Rojo', 'code': ''},
]


def insert_data(apps, schema_editor):
    category = apps.get_model('catalog', 'Category')
    for data in category_data:
        try:
            with transaction.atomic():
                category.objects.create(**data)
        except:
            pass

    brand = apps.get_model('catalog', 'Brand')
    for data in brand_data:
        try:
            with transaction.atomic():
                brand.objects.create(**data)
        except:
            pass

    color = apps.get_model('catalog', 'Color')
    for data in color_data:
        try:
            with transaction.atomic():
                color.objects.create(**data)
        except:
            pass


def revert_insert_data(apps, schema_editor):
    category = apps.get_model('catalog', 'Category')
    for data in category_data:
        try:
            category.objects.filter(name=data['name']).delete()
        except:
            pass

    brand = apps.get_model('catalog', 'Brand')
    for data in brand_data:
        try:
            brand.objects.filter(name=data['name']).delete()
        except:
            pass

    color = apps.get_model('catalog', 'Color')
    for data in color_data:
        try:
            color.objects.filter(name=data['name']).delete()
        except:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data, revert_insert_data),
    ]
