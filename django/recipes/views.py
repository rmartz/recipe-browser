# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count

from rest_framework import viewsets

from recipes.models import Recipe, Ingredient
from recipes.serializers import RecipeSerializer, IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        queryset = Recipe.objects.all()
        if 'limit_to' in self.request.query_params:
            ingredients = self.request.query_params['limit_to'].split(',')
            queryset = Recipe.objects.for_ingredients(filter(None, ingredients))

        if 'has_ingredient' in self.request.query_params:
            ingredient = self.request.query_params['has_ingredient']
            queryset = queryset.filter(ingredients=ingredient)

        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        if 'suggest_with' in self.request.query_params:
            ingredients = self.request.query_params['suggest_with'].split(',')
            ids = map(int, ingredients)
            # Since children satisfy their parents, expand to include ancestors
            inventory = Ingredient.objects.include_ancestors(ids)
            # Remove provided ingredients since they can't be suggestions for
            # themselves
            queryset = queryset.exclude(id__in=inventory)

            # Filter for ingredients that belong to a recipe that has one of
            # the suggestion prompt ingredients. This looks really convoluted,
            # but it makes it so the suggestion weight below scales with
            # number of shared ingredients... a recipe it has two ingredients
            # in common with will be weighted higher that one it doesn't.
            queryset = queryset.filter(
                recipeingredient__recipe__recipeingredient__ingredient_id__in=inventory)  # NOQA

        queryset = queryset.annotate(
            weight=Count('recipes'),
        )

        return queryset
