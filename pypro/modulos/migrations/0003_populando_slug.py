# Generated by Django 3.1.2 on 2020-10-08 11:27

from django.db import migrations
from django.utils.text import slugify


def popular_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'modulo')
    for m in Modulo.objects.all():
        m.slug = slugify(m.titulo)
        m.save()


class Migration(migrations.Migration):
    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]
