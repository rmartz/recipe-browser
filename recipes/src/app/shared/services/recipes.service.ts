import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { Ingredient } from '../models/ingredient.model';
import { Recipe } from '../models/recipe.model';

@Injectable()
export class Recipes {

  private _recipes: BehaviorSubject<Recipe[]>;

  constructor() {
    const ingred1 = new Ingredient('Ingredient 1');
    const ingred2 = new Ingredient('Ingredient 2');
    this._recipes = new BehaviorSubject<Recipe[]>([
      new Recipe('Recipe 1', [ingred1]),
      new Recipe('Recipe 2', [ingred1, ingred2])
    ]);
  }

  public list(): Observable<Recipe[]> {
    return this._recipes.asObservable();
  }
}
