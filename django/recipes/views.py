# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Case, Count, F, IntegerField, When

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
            # Find all recipes that use the base ingredients
            recipes = Recipe.objects.filter(
                recipeingredient__ingredient__in=ids)

            # Remove provided ingredients since they can't be suggestions for
            # themselves
            queryset = queryset.exclude(id__in=ids)

            # Annotate a count of the recipes remaining ingredients share with
            # provides ingredients
            queryset = queryset.annotate(
                weight=Count(Case(
                    When(recipeingredient__recipe__in=recipes,
                         then=F('recipeingredient__recipe__id')),
                    output_field=IntegerField()),
                    distinct=True))
        else:
            queryset = queryset.annotate(
                weight=Count('recipes'),
            )

        return queryset
