import { Ingredient } from './ingredient.model';

export class Recipe {
  constructor(label: string, ingredients: Ingredient[]) {
    this.label = label;
    this.ingredients = ingredients;
  }

  label: string;
  ingredients: Ingredient[];
}
