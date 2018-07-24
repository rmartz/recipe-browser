import { Ingredient } from './ingredient.model';

export class Recipe {
  constructor(label: string, ingredients: string[]) {
    this.label = label;
    this.ingredients = ingredients.map(ingred => new Ingredient(ingred));
  }

  label: string;
  ingredients: Ingredient[];
}
