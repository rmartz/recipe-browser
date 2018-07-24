import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Ingredient } from '../models/ingredient.model';
import { Recipes } from './recipes.service';

@Injectable()
export class Ingredients {

  private _ingredients: Observable<Ingredient[]>;

  constructor(recipeService: Recipes) {
    this._ingredients = recipeService.list().pipe(
      map(recipes => {
        const ingredients = new Set<Ingredient>();
        recipes.forEach(recipe => {
          recipe.ingredients.forEach(ingredient => {
            ingredients.add(ingredient);
          });
        });
        return Array.from(ingredients.values());
      })
    );
  }

  public list(): Observable<Ingredient[]> {
    return this._ingredients;
  }
}
