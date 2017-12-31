# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q


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
        """Return all recipes that only use the provided ingredients."""
        ids = map(int, ingredients)
        missing_ingredients = Ingredient.objects.all().exclude(id__in=ids)

        # Exclude recipes that have a required missing ingredient
        unmatched_recipes = RecipeIngredient.objects.filter(
            optional=False,
            ingredient__in=missing_ingredients
        ).values('recipe')
        return self.all().exclude(id__in=unmatched_recipes)


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
    quantity = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return "{} - {}".format(self.recipe.label, self.ingredient.label)
