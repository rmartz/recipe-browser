import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { Ingredient } from '../models/ingredient.model';
import { Recipe } from '../models/recipe.model';

@Injectable()
export class Recipes {

  private _recipes: BehaviorSubject<Recipe[]>;

  constructor() {
    this._recipes = new BehaviorSubject<Recipe[]>([
      new Recipe('Recipe 1', ['Ingredient 1']),
      new Recipe('Recipe 2', ['Ingredient 1', 'Ingredient 2'])
    ]);
  }

  public list(): Observable<Recipe[]> {
    return this._recipes.asObservable();
  }
}
