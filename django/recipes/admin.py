# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from recipes.models import (
    Ingredient,
    Recipe,
    RecipeIngredient,
)

for Model in (Ingredient,
              Recipe,
              RecipeIngredient):
    admin.site.register(Model)
