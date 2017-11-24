# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Ingredient(models.Model):
    label = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.label


class RecipeManager(models.Manager):
    def for_ingredients(self, ingredients):
        """Return a queryset of all recipes that fit the provided ingredients."""
        ids = map(int, ingredients)
        missing_ingredients = (Ingredient.objects.all().exclude(id__in=ids))
        return self.all().exclude(ingredients__in=missing_ingredients)


class Recipe(models.Model):
    label = models.CharField(max_length=128, unique=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    objects = RecipeManager()

    def __str__(self):
        return self.label
