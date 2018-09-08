import { Injectable } from '@angular/core';
import { map, switchMap } from 'rxjs/operators';
import { Observable, fromEvent, of, concat } from 'rxjs';

import { Recipe, RecipeWeight } from '../models/recipe.model';
import { Ingredients } from './ingredients.service';
import { Recipes } from './recipes.service';

@Injectable()
export class Suggestion {
  private _suggestedRecipes: Observable<RecipeWeight[]>;

  constructor(protected ingredients: Ingredients,
              protected recipes: Recipes) {

    this._suggestedRecipes = recipes.filtered().pipe(
      switchMap<Recipe[], RecipeWeight[]>(list => {
        // Whenever a blacklistChange event is triggered, re-filter all recipes
        return concat(
          // Concat an empty observable so we can build filtered recipes prior to any events
          of(this),
          fromEvent(document, 'favoriteChange')
        ).pipe(
          map<any, RecipeWeight[]>(() => {
            return list.map(recipe => {
              const weight = recipe.ingredients.filter(ingredient => ingredient.favorited).length;
              return new RecipeWeight(recipe, weight);
            }).sort((a, b) => b.weight - a.weight);
          })
        );
      })
    );
  }

  public suggestedRecipes(): Observable<RecipeWeight[]> {
    return this._suggestedRecipes;
  }
}
