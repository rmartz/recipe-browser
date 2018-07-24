import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { Ingredient } from '../models/ingredient.model';

@Injectable()
export class Ingredients {

  private _ingredients: BehaviorSubject<Ingredient[]>;

  constructor() {
    this._ingredients = new BehaviorSubject<Ingredient[]>([
      new Ingredient('Test 1'),
      new Ingredient('Test 2')
    ]);
  }

  public list(): Observable<Ingredient[]> {
    return this._ingredients.asObservable();
  }
}
