# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Ingredient(models.Model):
    label = models.CharField(max_length=128, unique=True)
    parent = models.ForeignKey('recipes.Ingredient',
                               models.SET_NULL,
                               blank=True,
                               null=True)

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
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='recipes',
                                         through='RecipeIngredient')

    objects = RecipeManager()

    def __str__(self):
        return self.label


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    optional = models.BooleanField(default=False)
    quantity = models.CharField(max_length=32)

    def __str__(self):
        return "{} - {}".format(self.recipe.label, self.ingredient.label)
