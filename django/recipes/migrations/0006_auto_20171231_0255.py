# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
